import pandas as pd
import numpy as np
import scipy.optimize as sco
import joblib
from sklearn.covariance import LedoitWolf
import warnings 
warnings.filterwarnings("ignore", category=UserWarning)

class RoboAdvisorEngine:
    def __init__(self, model_path='model_rekomendasi.joblib'):
        """
        Inisialisasi engine: Meload model ML dan menyiapkan data pasar dari CSV.
        """
        # 1. LOAD MODEL MACHINE LEARNING
        try:
            model_pack = joblib.load(model_path)
            self.preprocessor = model_pack['preprocessor']
            self.pca = model_pack['pca']
            self.kmeans = model_pack['kmeans_model']
            self.features = model_pack['feature_names']
        except Exception as e:
            print(f"Gagal meload model: {e}")
            
        # 2. SETUP DATA PASAR & COVARIANCE MATRIX (LEDOIT-WOLF)
        self.aset_names = ['Saham', 'Emas', 'Obligasi', 'RDPU', 'Deposito']
        self.expected_returns_annual = self._generate_market_data()
        
        # Mapping Aturan Batas (Hard Constraints) per Cluster
        self.cluster_rules = {
            0: { # AGRESIF
                'nama': 'Agresif (Young & Hungry)',
                'bounds': ((0.10, 0.80), (0.0, 0.20), (0.0, 1.0), (0.0, 1.0), (0.0, 0.10))
            },
            1: { # KONSERVATIF 
                'nama': 'Konservatif (The Pragmatist)',
                'bounds': ((0.0, 0.15), (0.0, 0.20), (0.0, 1.0), (0.0, 1.0), (0.0, 0.10))
            },
            2: { # MODERAT 
                'nama': 'Moderat (Long-Term Planner)',
                'bounds': ((0.0, 0.40), (0.0, 0.20), (0.0, 1.0), (0.0, 1.0), (0.0, 0.15))
            }
        }

    def _generate_market_data(self):
            """
            Membaca data historis dari pelbagai CSV, menghitung return, 
            dan membuat matriks kovarians Ledoit-Wolf.
            """
            try:
                # ==========================================
                # 1. PROSES DATA SAHAM 
                # ==========================================
                saham_files = ["ADRO.csv", "ANTM.csv", "ASII.csv", "BBCA.csv", "BBNI.csv", "BBRI.csv", "BMRI.csv", "CUAN.csv", "ICBP.csv", "INCO.csv", "ISAT.csv", "MEDC.csv", "MYOR.csv", "PTBA.csv", "TLKM.csv" ] 
                
                list_return_saham = []
                
                for file in saham_files:
                    df = pd.read_csv(file)
                    
                    # Paksa semua header menjadi huruf besar (CAPSLOCK) supaya seragam
                    df.columns = df.columns.str.upper() 
                    
                    # Pastikan kolom DATE jadi datetime dan set sebagai index
                    df['DATE'] = pd.to_datetime(df['DATE'])
                    df = df.set_index('DATE')
                    
                    # Kira peratusan perubahan harian (return) dari harga CLOSE
                    ret = df['CLOSE'].pct_change()
                    list_return_saham.append(ret)
                    
                # Gabungkan semua saham bersebelahan antara satu sama lain
                df_saham_all = pd.concat(list_return_saham, axis=1)
                
                # Cari purata (mean) merentas lajur untuk dapatkan 1 nilai wakil saham setiap hari
                return_saham = df_saham_all.mean(axis=1)
                return_saham.name = 'Saham'

                # ==========================================
                # 2. PROSES DATA EMAS 
                # ==========================================
                df_emas = pd.read_csv('EMAS.csv') 
                
                df_emas.columns = df_emas.columns.str.upper()
                df_emas['DATE'] = pd.to_datetime(df_emas['DATE'])
                df_emas = df_emas.set_index('DATE')
                
                return_emas = df_emas['CLOSE'].pct_change()
                return_emas.name = 'Emas'

                # ==========================================
                # 3. GABUNGKAN SAHAM & EMAS (Inner Join by Date)
                # ==========================================
                # Jika ada hari di mana pasaran saham buka tapi emas tutup, .dropna() akan selaraskan
                df_returns = pd.concat([return_saham, return_emas], axis=1).dropna()

                # ==========================================
                # 4. TAMBAHKAN INSTRUMEN FIXED INCOME (Pendapatan Tetap)
                # ==========================================
                n_days = len(df_returns)
                np.random.seed(42)
                
                # Asumsi pulangan tahunan: Obligasi 7%, RDPU 5%, Deposito 4%
                df_returns['Obligasi'] = np.random.normal((0.07/252), 0.001, n_days) 
                df_returns['RDPU'] = 0.05 / 252      
                df_returns['Deposito'] = 0.04 / 252  
                
                # Susun ikut turutan
                df_returns = df_returns[['Saham', 'Emas', 'Obligasi', 'RDPU', 'Deposito']]

                # ==========================================
                # 5. KALKULASI LEDOIT-WOLF
                # ==========================================
                lw = LedoitWolf()
                lw.fit(df_returns)
                self.cov_matrix_annual = lw.covariance_ * 252
                
                expected_returns = df_returns.mean().values * 252
                return expected_returns
                
            except Exception as e:
                print(f"error saat memproses data pasar: {e}")
                print("Pastikan file CSV ada dan nama kolom sesuai.")
                return np.array([0.12, 0.08, 0.07, 0.05, 0.04])

    def _markowitz_objective(self, weights, risk_aversion, gamma=0.05):
        """
        Fungsi Utilitas Markowitz dengan L2 Regularization (Diversification Penalty).
        gamma: Kekuatan penalti. Semakin besar, portofolio akan semakin menyebar merata.
        """
        # 1. Hitung Ekspektasi Return Portofolio
        port_return = np.sum(self.expected_returns_annual * weights)
        
        # 2. Hitung Varians (Risiko) Portofolio
        port_variance = np.dot(weights.T, np.dot(self.cov_matrix_annual, weights))
        
        # 3. Hitung L2 Penalty (Sum of Squared Weights)
        l2_penalty = np.sum(weights**2)
        
        # 4. Fungsi Utilitas Baru
        utility = port_return - (0.5 * risk_aversion * port_variance) - (gamma * l2_penalty)
        
        return -utility # Diminimize oleh Scipy
 

    def predict_portfolio(self, user_data_dict):
        """Fungsi Prediksi dan Optimasi (Dipanggil dari UI Streamlit)"""
        df_input = pd.DataFrame([user_data_dict])
        df_input = df_input[self.features]
        
        # 1. ML Predict Cluster
        X_scaled = self.preprocessor.transform(df_input)
        X_pca = self.pca.transform(X_scaled)
        cluster_id = self.kmeans.predict(X_pca)[0]
        
        # 2. Setup Batasan MVO
        cluster_info = self.cluster_rules[cluster_id]
        bounds = cluster_info['bounds']
        
        user_risk_tol = max(user_data_dict.get('risk_tolerance', 1), 1)
        risk_aversion = 15 / user_risk_tol
        
        # 3. Optimasi Scipy
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1.0})
        init_guess = np.array([0.2, 0.2, 0.2, 0.2, 0.2]) 
        
        gamma_value = 0.05
        optimized = sco.minimize(
            self._markowitz_objective, 
            init_guess, 
            args=(risk_aversion, gamma_value), 
            method='SLSQP', 
            bounds=bounds, 
            constraints=constraints
        )
        weights = optimized.x
        
        exp_return = np.sum(self.expected_returns_annual * weights)
        exp_risk = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix_annual, weights)))
        
        return {
            'Cluster_ID': cluster_id,
            'Profil': cluster_info['nama'],
            'Alokasi': {self.aset_names[i]: round(weights[i] * 100, 2) for i in range(5)},
            'Proyeksi_Return_Tahunan': round(exp_return * 100, 2),
            'Proyeksi_Risiko': round(exp_risk * 100, 2)
        }

# ================= TESTING SCRIPT =================
if __name__ == "__main__":
    robo = RoboAdvisorEngine('model_rekomendasi.joblib')
    # Coba prediksi
    print(robo.predict_portfolio({
        'risk_tolerance': 4, 'monthly_income': 60000000.0,
        'investment_horizon': 12, 'age': 18, 'investment_goal': 'Wealth Growth'
    }))