import streamlit as st
import pandas as pd

st.set_page_config(page_title="EduInvest by RencanaKita - Reksadana", layout="wide")

st.title("🧺 Level 2: Reksadana (Mutual Funds)")
st.subheader("Serahkan pada ahlinya. Beli 'keranjang' berisi berbagai aset hanya dengan satu kali klik.")

st.divider()

# ==========================================
# BAGIAN 1: EDUKASI FUNDAMENTAL
# ==========================================
st.header("🧠 Mari Pahami Konsep Dasarnya")

st.info(
        "📊 **Apa Itu Reksadana?**\nReksadana adalah wadah investasi yang mengumpulkan dana dari banyak investor untuk kemudian diinvestasikan ke berbagai instrumen seperti saham, obligasi, atau deposito. "
        "Dana yang terkumpul ini dikelola oleh Manajer Investasi (MI) profesional yang bertugas memilih aset terbaik untuk mencapai tujuan investasi. Kamu cukup membeli unit penyertaan reksadana, dan MI yang akan bekerja untukmu."
)

st.info(
    "💡 **Analogi Sederhana:** Bayangkan kamu ingin makan salad buah yang isinya macam-macam (apel, anggur, mangga, kiwi). "
    "Membeli setiap buah secara utuh pasti mahal dan repot mengupasnya. Reksadana adalah 'salad buah' yang sudah diracik oleh "
    "ahli gizi (**Manajer Investasi**). Kamu cukup beli satu porsi kecil, tapi sudah dapat semua jenis buah di dalamnya!"
)

st.info(
    "📈 **Jenis-Jenis Reksadana:**\n-"
    " **Reksadana Pasar Uang:** Investasi di instrumen pasar uang seperti deposito, obligasi jangka pendek. Risiko rendah, return stabil.\n-" 
    " **Reksadana Pendapatan Tetap:** Investasi di obligasi pemerintah atau korporasi. Risiko sedang, return lebih tinggi dari pasar uang.\n-"
    " **Reksadana Saham:** Investasi di saham-saham perusahaan. Risiko tinggi, potensi return besar dalam jangka panjang.\n-"
    " **Reksadana Campuran:** Kombinasi saham, obligasi, dan pasar uang. Risiko dan return menengah."
)


st.markdown("### 👨‍💼 Siapa itu Manajer Investasi (MI)?")
st.write(
    "Mereka adalah profesional bersertifikat yang kerjanya setiap hari memantau pasar. "
    "Uangmu dan uang ribuan investor lainnya dikumpulkan jadi satu, lalu MI yang akan membelanjakan "
    "uang tersebut ke saham, obligasi, atau deposito terbaik. Kamu tinggal duduk manis."
)

st.divider()
col1, col2 = st.columns(2)

st.markdown("### 🎯 Untuk Siapa Aset Ini?")
st.write(
    "Tergantung jenis reksadananya! \n-")
with col1:
    st.write(
        " Reksadana pasar uang cocok untuk tipe **Averse** dan **Minimalist** yang ingin melawan inflasi dengan risiko sangat rendah. " \
        " Cocok juga digunakan untuk target jangka pendek (1 tahun) atau sebagai tempat parkir sementara sebelum masuk ke investasi yang lebih agresif. \n-"
        " Reksadana Pendapatan Tetap cocok untuk tipe **Cautious** (Moderat) yang ingin sedikit lebih agresif dari pasar uang tapi masih tetap aman. Cocok untuk target jangka menengah (3-5 tahun)."     
    )
with col2:
    st.write(
        " Reksadana Saham cocok untuk tipe **Open** dan **Hungry** (Agresif). Ini sangat cocok "
        " untuk orang sibuk yang tidak punya waktu menganalisa grafik setiap hari. \n-"
        " Reksadana Campuran cocok untuk tipe **Cautious** yang ingin disversifikasi dengan risiko sedang, atau untuk investor pemula yang ingin mencoba-coba berbagai jenis aset dalam satu produk."
    )

st.markdown("### ⚖️ Plus & Minus")
col_plus, col_minus = st.columns(2)
with col_plus:
    st.success("**Kelebihan:**\n- **Praktis & Otomatis:** Dikelola oleh profesional.\n- **Diversifikasi:** Risiko tersebar, tidak menaruh semua telur di 1 keranjang.\n- **Modal Kecil:** Bisa mulai dari Rp 10.000 saja!")
with col_minus:
    st.warning("**Kekurangan:**\n- **Ada Biaya (Expense Ratio):** Manajer Investasi memotong sedikit keuntunganmu sebagai biaya jasa mereka.\n- **Risiko Pasar:** Jika pasar saham sedang anjlok, reksadana sahammu juga ikut turun.")

st.divider()

# ==========================================
# BAGIAN 2: RUMUS MATEMATIKA (NAB/UP)
# ==========================================
st.header("🧮 Cara Kerja Harga Reksadana (NAB)")
st.write("Di deposito kita bicara 'Suku Bunga', tapi di reksadana kita bicara **NAB/UP (Nilai Aktiva Bersih per Unit Penyertaan)**. Harga NAB ini naik-turun setiap hari.")

st.latex(r"Unit\ Penyertaan\ (UP) = \frac{Nominal\ Investasi}{Harga\ NAB\ saat\ beli}")
st.latex(r"Total\ Saldo = Unit\ Penyertaan\ (UP) \times Harga\ NAB\ hari\ ini")

st.markdown("""
**Contoh Gampang:**
* Hari ini harga 1 Unit Reksadana (NAB) = Rp 1.000. Kamu investasi Rp 100.000. Maka kamu dapat **100 Unit**.
* Tahun depan, Manajer Investasimu pintar, harga NAB naik jadi Rp 1.200.
* Maka saldo uangmu sekarang: 100 Unit x Rp 1.200 = **Rp 120.000**.
""")

st.divider()

# ==========================================
# BAGIAN 3: SIMULATOR INTERAKTIF (DCA)
# ==========================================
st.header("🎛️ Simulator Kekuatan Rutin Menabung (DCA)")
st.write("Kunci sukses di Reksadana bukanlah menebak kapan harga murah, tapi berinvestasi secara rutin setiap bulan (*Dollar Cost Averaging / DCA*). Mari kita simulasikan!")

st.markdown("#### 1. Masukkan Rencanamu")
input_col1, input_col2, input_col3, input_col4 = st.columns(4)

with input_col1:
    modal_awal = st.slider("Modal Awal (Rp)", 0, 50_000_000, 5_000_000, step=1_000_000)
with input_col2:
    nabung_rutin = st.slider("Nabung Bulanan (Rp)", 100_000, 10_000_000, 1_000_000, step=100_000)
with input_col3:
    tenor_tahun = st.slider("Lama Investasi (Tahun)", 1, 30, 10, step=1)
with input_col4:
    asumsi_return = st.slider("Asumsi Return/Tahun (%)", 1.0, 20.0, 8.0, step=0.5)

# Kalkulasi Pertumbuhan (Compounding & DCA)
bulan_total = tenor_tahun * 12
asumsi_return_bulanan = (asumsi_return / 100) / 12

data_perjalanan = []
saldo_berjalan = modal_awal
modal_terkumpul = modal_awal

for bulan in range(1, bulan_total + 1):
    # Setor tiap bulan
    saldo_berjalan += nabung_rutin
    modal_terkumpul += nabung_rutin
    
    # Bunga majemuk (compounding) bekerja setiap bulan
    keuntungan_bulan_ini = saldo_berjalan * asumsi_return_bulanan
    saldo_berjalan += keuntungan_bulan_ini
    
    # Simpan titik data untuk grafik setiap akhir tahun (bulan kelipatan 12)
    if bulan % 12 == 0:
        data_perjalanan.append({
            "Tahun ke-": int(bulan / 12),
            "Uang Modalmu (Rp)": modal_terkumpul,
            "Total Uang + Keuntungan (Rp)": saldo_berjalan
        })

total_keuntungan = saldo_berjalan - modal_terkumpul

st.markdown("#### 2. Estimasi Hasil di Masa Depan")
res_col1, res_col2, res_col3 = st.columns(3)

res_col1.metric(label="Uang Modal (Yang Kamu Setor)", value=f"Rp {modal_terkumpul:,.0f}")
res_col2.metric(label="Keuntungan (Hasil Kerja MI)", value=f"Rp {total_keuntungan:,.0f}")
res_col3.metric(label="Total Saldo Akhir", value=f"Rp {saldo_berjalan:,.0f}")

st.write("---")

st.markdown("#### 3. Grafik Bola Salju (Snowball Effect)")
st.write("Perhatikan garis hijau (Total Uang) yang semakin lama semakin menjauh dari garis biru (Uang Modal). Itulah keajaiban bunga berbunga!")

# Render Line Chart dengan 2 garis
df_grafik = pd.DataFrame(data_perjalanan).set_index("Tahun ke-")
st.line_chart(df_grafik, color=["#1f77b4", "#2ca02c"]) # Biru untuk Modal, Hijau untuk Total

st.divider()

# ==========================================
# BAGIAN 4: TIPS PRO (HACKS)
# ==========================================
st.header("💡 Tips Pro: Memilih Reksadana Terbaik")

st.warning(
    "**1. Perhatikan *Expense Ratio* (Biaya Manajemen)**\n\n"
    "Cek *Fund Fact Sheet* sebelum membeli. *Expense Ratio* adalah persentase uang yang diambil MI untuk biaya operasional mereka. "
    "Semakin kecil angkanya (misal di bawah 1.5%), semakin bagus untukmu! Karena biaya ini dipotong langsung dari keuntunganmu."
)

st.warning(
    "**2. Jangan hanya memilih return tertinggi, namun cari yang punya kinerja konsisten**\n\n"
    "Cek *return 3 bulan, return 6 bulan, dan return 1 tahun* sebelum membeli."
    "Reksadana dengan return tinggi tapi fluktuatif bisa jadi sangat berisiko. Lebih baik pilih yang punya return stabil dan konsisten."
)

st.warning(
    "**3. Perhatikan total dana yang dikelola (AUM / Asset Under Management)**\n\n"
    "Untuk investor ritel, AUM yang cukup besar sering menjadi sinyal positif karena menunjukkan kepercayaan pasar."
)

st.success(
    "**4. DCA: Jurus Anti Stres Hadapi Pasar Merah**\n\n"
    "Saat harga reksadana turun, jangan panik! Dengan strategi rutin menabung tiap bulan (DCA), saat harga sedang anjlok, "
    "uang bulananmu otomatis akan mendapatkan **lebih banyak Unit Penyertaan (UP)**. Ketika pasar pulih, keuntunganmu akan berlipat ganda."
)