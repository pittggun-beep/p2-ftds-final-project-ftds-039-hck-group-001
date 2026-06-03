import streamlit as st
import pandas as pd
import numpy as np
import scipy.optimize as optimize

st.set_page_config(page_title="EduInvest - Obligasi", layout="wide")

# ==========================================
# CORE ENGINE: Class BondAnalyzer
# ==========================================
class BondAnalyzer:
    def __init__(self, face_value, coupon_rate, years_to_maturity, frequency=2):
        self.face_value = face_value
        self.coupon_rate = coupon_rate
        self.years_to_maturity = years_to_maturity
        self.frequency = frequency
        self.periods = years_to_maturity * frequency
        self.coupon_payment = (face_value * coupon_rate) / frequency

    def calculate_price(self, ytm):
        rate = ytm / self.frequency
        cash_flows = [self.coupon_payment] * self.periods
        cash_flows[-1] += self.face_value
        price = sum([cf / (1 + rate)**(t+1) for t, cf in enumerate(cash_flows)])
        return price

    def calculate_ytm(self, current_price):
        def objective_function(ytm_guess):
            return self.calculate_price(ytm_guess) - current_price
        try:
            ytm = optimize.newton(objective_function, self.coupon_rate)
        except:
            ytm = 0.0
        return ytm

    def calculate_modified_duration(self, ytm):
        rate = ytm / self.frequency
        cash_flows = [self.coupon_payment] * self.periods
        cash_flows[-1] += self.face_value
        t_values = np.arange(1, self.periods + 1)
        pv_cash_flows = [cf / (1 + rate)**t for t, cf in zip(t_values, cash_flows)]
        
        sum_pv = sum(pv_cash_flows)
        if sum_pv == 0: return 0.0
            
        macaulay_duration = sum(t * pv / sum_pv for t, pv in zip(t_values, pv_cash_flows)) / self.frequency
        mod_duration = macaulay_duration / (1 + rate)
        return mod_duration

# ==========================================
# LAYOUT HALAMAN STREAMLIT
# ==========================================
st.title("📈 Level 4: Obligasi (Surat Utang)")
st.subheader("Jadilah 'Bank' bagi Negara atau Perusahaan dan dapatkan bunga rutin yang lebih tinggi dari deposito.")

st.divider()

# ==========================================
# BAGIAN 1: EDUKASI FUNDAMENTAL
# ==========================================
st.header("🧠 Mari Pahami Konsep Dasarnya")

st.info(
    "💡 **Apa itu Obligasi?**\n\n"
    "Obligasi adalah surat utang resmi. Ketika membeli obligasi, kamu sebenarnya **meminjamkan uang** "
    "kepada Negara atau Perusahaan. Sebagai gantinya, modalmu akan dikembalikan utuh saat jatuh tempo, "
    "plus kamu akan ditransfer imbalan (bunga) secara rutin."
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📖 3 Istilah Penting")
    st.markdown("""
    - **Pari (Nilai Nominal):** Modal pokok yang akan dikembalikan saat lunas. Di pasar sekunder, harga ini bisa dijual lebih mahal (*Premium*) atau lebih murah (*Discount*).
    - **Kupon:** Bunga atau pendapatan rutin yang kamu terima.
    - **Tenor:** Jangka waktu sejak obligasi dibeli sampai jatuh tempo.
    """)
    
with col2:
    st.markdown("### 🏢 4 Jenis Obligasi")
    st.markdown("""
    - **Pemerintah:** Paling aman sedunia karena dijamin kekuatan fiskal negara.
    - **Korporasi (BUMN/Swasta):** Bunga lebih tinggi, tapi risiko juga lebih tinggi.
    - **Syariah (Sukuk):** Dikelola pakai prinsip Islam (bagi hasil, tanpa riba).
    - **Daerah:** Diterbitkan Pemda untuk mendanai proyek infrastruktur lokal.
    """)

st.divider()

# ==========================================
# BAGIAN 2: RUMUS MATEMATIKA & HUKUM PASAR
# ==========================================
st.header("🧮 Hukum Jungkat-Jungkit Obligasi")
st.write("Harga obligasi bergerak berlawanan arah dengan Suku Bunga Pasar. Harga wajarnya dihitung dari nilai sekarang (*Present Value*) seluruh keuntungan di masa depan.")


st.latex(r"Price = \sum_{t=1}^{N} \frac{C}{(1+r)^t} + \frac{FV}{(1+r)^N}")
st.caption("**C** = Kupon, **FV** = Pari, **r** = Suku bunga pasar (YTM), **N** = Tenor.")


st.warning(
    "**Ingat Aturan Ini:**\n"
    "- Jika suku bunga BI **NAIK**, harga obligasi lamamu akan **TURUN**.\n"
    "- Jika suku bunga BI **TURUN**, harga obligasimu **NAIK** (Bisa dijual untung / *Capital Gain*)."
    )

st.divider()

# ==========================================
# BAGIAN 3: SIMULATOR INTERAKTIF
# ==========================================
st.header("🎛️ Simulator Obligasi & Risiko Suku Bunga")
st.write("Masukkan spesifikasi obligasi di sebelah kiri, lalu gunakan 3 tab di bawah untuk mensimulasikan hukum pasar di atas.")

col_input, col_sim = st.columns([1, 2])

with col_input:
    st.markdown("#### Spesifikasi Obligasimu")
    face_val = st.number_input("Nilai Pokok / Pari (Rp)", value=10_000_000, step=1_000_000)
    coupon = st.number_input("Kupon Tahunan (%)", value=6.5, step=0.1) / 100
    tenor = st.number_input("Sisa Tenor (Tahun)", value=10, step=1)
    
    bond = BondAnalyzer(face_value=face_val, coupon_rate=coupon, years_to_maturity=tenor)

with col_sim:
    tab1, tab2, tab3 = st.tabs([
        "Cek Harga Wajar", 
        "Hitung Keuntungan Asli (YTM)", 
        "Ukur Risiko (Duration)"
    ])

    with tab1:
        st.write("**Berapa harga jual obligasimu jika suku bunga pasar berubah?**")
        ytm_input = st.slider("Simulasi Suku Bunga Pasar (%)", min_value=1.0, max_value=15.0, value=7.0, step=0.1) / 100
        harga_wajar = bond.calculate_price(ytm_input)
        
        status = "Diskon (Lebih Murah) 📉" if harga_wajar < face_val else "Premium (Lebih Mahal) 📈" if harga_wajar > face_val else "Pari (Harga Sama) ⚖️"
        
        st.metric(label="Harga Jual Wajar Saat Ini", value=f"Rp {harga_wajar:,.0f}", delta=status, delta_color="off")

    with tab2:
        st.write("**Beli obligasi di pasar sekunder? Berapa bunga aslinya?**")
        harga_pasar = st.number_input("Harga Beli di Pasar Sekunder (Rp):", value=9_500_000, step=100_000)
        
        ytm_riil = bond.calculate_ytm(harga_pasar)
        if ytm_riil > 0:
            st.metric(label="Bunga Riil / Yield to Maturity (YTM)", value=f"{ytm_riil * 100:.2f}%")
            st.caption("Karena kamu beli di harga Diskon, keuntungan aslimu lebih besar dari persentase Kupon!")
        else:
            st.error("Kalkulasi gagal. Masukkan nominal harga pasar yang valid.")

    with tab3:
        st.write("**Seberapa sensitif obligasimu terhadap perubahan ekonomi?**")
        ytm_risk_input = st.number_input("Suku Bunga Pasar Saat Ini (%)", value=6.5, step=0.1) / 100
        mod_dur = bond.calculate_modified_duration(ytm_risk_input)
        
        st.metric(label="Modified Duration", value=f"{mod_dur:.2f} Tahun")
        st.warning(f"⚠️ Jika suku bunga acuan naik 1% saja, harga obligasimu akan **jatuh sekitar {mod_dur:.2f}%**.")

st.divider()

# ==========================================
# BAGIAN 4: TIPS PRO (HACKS)
# ==========================================
st.header("💡 Tips Pro: Jurus Anti Rugi")

st.success(
    "**Hold to Maturity (Pegang Sampai Lunas)**\n\n"
    "Jika kamu melihat harga obligasimu turun (merah) di aplikasi, **jangan panik dan jangan dijual!** "
    "Selama Negara/Perusahaan tersebut tidak bangkrut, saat jatuh tempo tiba, uang Pari (pokok) kamu akan dikembalikan 100% utuh, "
    "tak peduli seburuk apa pun harga pasar saat itu."
)