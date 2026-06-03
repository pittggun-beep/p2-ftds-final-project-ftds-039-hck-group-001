import streamlit as st
import pandas as pd

st.set_page_config(page_title="EduInvest by RencanaKita - Deposito", layout="wide")

st.title("💰 Level 1: Deposito")
st.subheader("Tempat paling aman untuk melindungi uangmu dari inflasi tanpa perlu pusing melihat harga turun.")

st.divider()

# ==========================================
# BAGIAN 1: EDUKASI FUNDAMENTAL
# ==========================================
st.header("🧠 Mari Pahami Konsep Dasarnya")

st.info(
    "📊 **Apa Itu Deposito?**\nDeposito adalah produk simpanan berjangka yang ditawarkan oleh bank. " 
    "Kamu menyimpan sejumlah uang untuk jangka waktu tertentu (misalnya 1 bulan, 3 bulan, 6 bulan, atau 1 tahun) dan mendapatkan bunga sebagai imbalannya."
    "Setelah jangka waktu berakhir, kamu bisa mencairkan uangmu beserta bunganya.")


st.info(
    "💡 **Analogi Sederhana:** Menyimpan uang di Deposito itu ibarat "
    "kamu menitipkan uang di brankas bank yang sangat aman, tapi uang itu tidak diam. "
    "Uangmu 'bekerja' dengan dipinjamkan ke bank atau negara dalam jangka sangat pendek, "
    "dan sebagai gantinya kamu dibayar menggunakan bunga rutin."
)


col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🥊 Musuh Terbesarmu: Inflasi")
    st.write(
        "Pernah sadar harga semangkuk mie ayam 5 tahun lalu lebih murah dari sekarang? Itulah inflasi. "
        "Kalau kamu cuma menyimpan uang di bawah kasur atau tabungan biasa yang bunganya nyaris 0%, "
        "nilai uangmu sebenarnya pelan-pelan 'dimakan' oleh inflasi. Deposito dan Pasar Uang adalah "
        "senjata paling dasar untuk melawan inflasi."
    )
    
with col2:
    st.markdown("### 🎯 Untuk Siapa Aset Ini?")
    st.write(
        "Instrumen ini sangat wajib dimiliki oleh tipe investor **Averse** (Sangat Menghindari Risiko) dan "
        "**Minimalist** (Lebih Suka Keamanan). Selain itu, ini adalah tempat terbaik untuk memarkir "
        "**Dana Darurat** karena sifatnya yang stabil dan grafiknya nyaris selalu naik perlahan tanpa *drawdown* (penurunan drastis)."
    )

st.markdown("### ⚖️ Plus & Minus")
col_plus, col_minus = st.columns(2)
with col_plus:
    st.success("**Kelebihan:**\n- **Risiko Sangat Rendah:** Uang di deposito bank umum dijamin oleh LPS (Lembaga Penjamin Simpanan).\n- **Stabil:** Bebas dari serangan panik pasar saham.\n- **Cocok untuk Rencana Jangka Pendek:** Karena mudah dicairkan setelah jatuh tempo, cocok untuk menabung jangka pendek.")
with col_minus:
    st.warning("**Kekurangan:**\n- **Return Terbatas:** Keuntungannya tidak akan membuatmu cepat kaya, fungsinya lebih ke 'menjaga' kekayaan.\n- **Pajak Cukup Besar:** Bunga deposito dikenakan potongan pajak sebesar 20% oleh pemerintah.\n- **Terkena Penalti Jika Dicairkan Dini:** Jika kamu mencairkan deposito sebelum jatuh tempo, biasanya akan dikenakan penalti berupa potongan bunga atau bahkan pokok.")

st.divider()

# ==========================================
# BAGIAN 2: Menghitung Bunga Deposito & Simulasi Pertumbuhan Dana
# ==========================================

st.header("🧮 Cara Menghitung Bunga Deposito")
st.write("Sebelum mencoba simulator, mari lihat rumus standar yang digunakan oleh bank untuk menghitung keuntunganmu:")

# Menggunakan fitur LaTeX dari Streamlit untuk menampilkan rumus dengan rapi
st.latex(r"B = P \times r \times \frac{t}{365}")

st.markdown("""
**Keterangan:**
* **$B$** = Jumlah bunga yang diperoleh (Rupiah)
* **$P$** = Setoran awal / Pokok deposito (*Principal*)
* **$r$** = Suku bunga per tahun (*Interest rate*)
* **$t$** = Jangka waktu penyimpanan (Hari)
* **365** = Jumlah hari dalam satu tahun (beberapa bank mungkin menggunakan 360 hari)
""")

st.divider()

st.header("🎛️ Simulator Pertumbuhan Dana")
st.write("Mari kita lihat kekuatan *Compounding Interest* (Bunga Berbunga) di dunia nyata. Gunakan *slider* di bawah untuk mensimulasikan perhitungan Deposito, lengkap dengan potongan pajak 20%.")

# Input Parameter dari User
st.markdown("#### 1. Masukkan Rencanamu")
input_col1, input_col2, input_col3 = st.columns(3)

with input_col1:
    nominal = st.slider(
        "Jumlah Deposito (Rp)", 
        min_value=1_000_000, 
        max_value=500_000_000, 
        value=10_000_000, 
        step=1_000_000
    )
with input_col2:
    tenor = st.slider(
        "Tenor / Jangka Waktu (Bulan)", 
        min_value=1, 
        max_value=60, 
        value=12, 
        step=1
    )
with input_col3:
    bunga = st.slider(
        "Suku Bunga / Tahun (%)", 
        min_value=1.0, 
        max_value=10.0, 
        value=5.0, 
        step=0.1
    )

# Kalkulasi Matematika Finansial
pajak_rate = 0.20
bunga_kotor = nominal * (bunga / 100) * (tenor / 12)
potongan_pajak = bunga_kotor * pajak_rate
bunga_bersih = bunga_kotor - potongan_pajak
total_pengembalian = nominal + bunga_bersih

st.markdown("#### 2. Estimasi Hasil Keuntunganmu")
# Menampilkan hasil dengan Metric UI Streamlit
res_col1, res_col2, res_col3 = st.columns(3)

res_col1.metric(label="Bunga Bersih (Milikmu)", value=f"Rp {bunga_bersih:,.0f}")
res_col2.metric(label="Pajak Negara (20%)", value=f"Rp {potongan_pajak:,.0f}")
res_col3.metric(label="Total Dana Saat Cair", value=f"Rp {total_pengembalian:,.0f}")

st.write("---")

# Visualisasi Grafik Pertumbuhan
st.markdown("#### 3. Proyeksi Pertumbuhan Uang Bulanan")
st.write("Grafik di bawah menunjukkan bagaimana uangmu bertambah setiap bulannya jika bunga tidak dicairkan, melainkan terus diakumulasikan (keajaiban *compounding*).")

# Menyiapkan data untuk grafik
data_bulan = []
for bulan in range(1, tenor + 1):
    # Asumsi bunga dihitung proporsional per bulan dari nominal awal setelah dipotong pajak
    bunga_bulan_ini = (nominal * (bunga / 100) * (1 / 12)) * (1 - pajak_rate)
    akumulasi = nominal + (bunga_bulan_ini * bulan)
    data_bulan.append({"Bulan ke-": bulan, "Total Saldo (Rp)": akumulasi})

df_grafik = pd.DataFrame(data_bulan).set_index("Bulan ke-")

# Render grafik garis
st.line_chart(df_grafik)

# ==========================================
# BAGIAN 3: Tips Pro: Memaksimalkan Keuntungan Deposito
# ==========================================
st.header("💡 Tips Pro: Memaksimalkan Keuntungan Deposito")

st.warning(
    "**1. Manfaatkan Bank Digital, Tapi Tetap Waspada**\n\n"
    "Deposito yang ditawarkan oleh bank digital rata-rata memiliki bunga yang tinggi dan bisa mencapai 8% per tahun. "
    "Namun, **LPS hanya menjamin maksimal bunga 6%**. Artinya, jika bank tersebut bermasalah dan bungamu di atas 6%, "
    "uangmu tidak akan diganti oleh negara. Risiko ditanggung sendiri!"
)

st.success(
    "**2. Trik Legal Menghindari Pajak 20%**\n\n"
    "Pajak atas bunga deposito akan dikenakan sebesar 20% **jika** nominal deposito yang ditempatkan melebihi Rp 7.500.000. "
    "Kamu bisa membuat beberapa akun deposito (memecah uangmu) di bank digital dengan nominal masing-masing **di bawah Rp 7.500.000** "
    "untuk menghindari potongan bunga ini secara sah. *(Coba buktikan sendiri dengan menggeser slider nominal di atas ke angka Rp 7.000.000!)*"
)

st.divider()

st.success("🎉 **Hebat!** Kamu sudah paham cara kerja instrumen paling dasar. Jika kamu siap mengambil sedikit risiko lebih demi keuntungan yang lebih tinggi dari ini, mari lanjut pelajari tentang instrumen finansial lainnya di halaman berikutnya!")