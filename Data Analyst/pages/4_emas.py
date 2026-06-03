import streamlit as st
import pandas as pd

st.set_page_config(page_title="EduInvest - Emas", layout="wide")

st.title("🥇 Level 3: Emas (Logam Mulia)")
st.subheader("Bukan untuk cepat kaya, tapi untuk menjaga agar kamu tidak jatuh miskin saat terjadi krisis.")

st.divider()

# ==========================================
# BAGIAN 1: EDUKASI FUNDAMENTAL
# ==========================================
st.header("🧠 Mari Pahami Konsep Dasarnya")

st.info(
    "💡 **Analogi Sederhana:** Emas adalah 'Safe Haven' (Tempat Berlindung). Bayangkan uang kertasmu adalah "
    "sebuah kapal kayu di tengah lautan. Saat cuaca cerah, kapal kayu melaju cepat. Tapi saat terjadi badai "
    "(krisis ekonomi, perang, inflasi gila-gilaan), kapal kayu bisa hancur. Emas adalah sekoci baja anti-badai "
    "yang akan menyelamatkan nilai kekayaanmu."
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🛡️ Pelindung Nilai (Hedging)")
    st.write(
        "Di tahun 1990, dengan uang Rp 10.000 kamu bisa beli banyak barang. Sekarang, Rp 10.000 cuma dapat nasi kucing. "
        "Tapi, 1 gram emas di zaman nabi sampai sekarang nilainya kurang lebih sama: bisa buat beli 1 ekor kambing. "
        "Emas tidak menciptakan kekayaan baru (tidak ada bunga/dividen), ia hanya mempertahankan daya belimu dari gerusan inflasi."
    )
    
with col2:
    st.markdown("### 🎯 Untuk Siapa Aset Ini?")
    st.write(
        "Cocok untuk semua profil risiko, tapi idealnya dialokasikan **5% - 10% saja dari total uangmu** sebagai jangkar pelindung. "
        "Ini adalah investasi wajib bagi tipe yang memikirkan jangka sangat panjang (> 5 tahun) atau untuk warisan anak cucu."
    )

st.markdown("### ⚖️ Plus & Minus")
col_plus, col_minus = st.columns(2)
with col_plus:
    st.success("**Kelebihan:**\n- **Tahan Krisis:** Harganya justru sering naik gila-gilaan saat dunia sedang kacau/krisis.\n- **Universal:** Laku dijual di negara mana pun di seluruh dunia.\n- **Fisik Nyata:** Bisa kamu pegang dan simpan sendiri (jika beli fisik).")
with col_minus:
    st.warning("**Kekurangan:**\n- **Tidak Ada Passive Income:** Emas tidak memberikan bunga atau dividen bulanan.\n- **Ada Risiko Kehilangan:** Kalau fisik, bisa dicuri. Kalau sewa *Safe Deposit Box* di bank, ada biaya tambahan.\n- **Spread:** Selisih harga beli dan jual cukup jauh.")

st.divider()

# ==========================================
# BAGIAN 2: RUMUS MATEMATIKA (SPREAD & BUYBACK)
# ==========================================
st.header("🧮 Hati-hati dengan SPREAD (Harga Buyback)")
st.write("Kesalahan terbesar pemula: Beli emas Rp 1.300.000, lalu besoknya butuh uang dan dijual ke toko emas. Mereka kaget karena toko hanya mau beli di harga Rp 1.150.000. Selisih inilah yang disebut **Spread**.")

st.latex(r"Spread = Harga\ Beli\ Saat\ Ini - Harga\ Jual\ Kembali\ (Buyback)")
st.latex(r"Gram\ Didapat = \frac{Nominal\ Uang}{Harga\ Beli\ per\ Gram}")
st.latex(r"Uang\ Saat\ Dicairkan = Gram\ Dimiliki \times Harga\ Buyback\ Saat\ Itu")

st.markdown("""
**Aturan Emas:** Karena adanya *Spread* (biasanya sekitar 3% - 10% tergantung tempat beli), investasi emas **wajib jangka panjang minimal 3-5 tahun** hanya untuk sekadar "balik modal" dari potongan spread tersebut.
""")

st.divider()

# ==========================================
# BAGIAN 3: SIMULATOR INTERAKTIF (THE SPREAD TRAP)
# ==========================================
st.header("🎛️ Simulator Jebakan Spread Emas")
st.write("Gunakan *slider* di bawah. Perhatikan bahwa di tahun-tahun pertama, kamu sebenarnya **rugi** jika langsung menjual emasmu.")

st.markdown("#### 1. Masukkan Skenario Pembelianmu")
input_col1, input_col2, input_col3, input_col4 = st.columns(4)

with input_col1:
    modal_awal = st.slider("Uang untuk Beli Emas (Rp)", 1_000_000, 100_000_000, 10_000_000, step=1_000_000)
with input_col2:
    harga_beli_skrg = st.number_input("Harga Beli Saat Ini (Rp/Gram)", value=1_300_000, step=10_000)
with input_col3:
    spread_persen = st.slider("Asumsi Spread / Potongan Buyback (%)", 1, 15, 5, step=1)
with input_col4:
    kenaikan_tahunan = st.slider("Asumsi Kenaikan Harga/Tahun (%)", 1.0, 15.0, 6.0, step=0.5)

# Kalkulasi Emas
gram_didapat = modal_awal / harga_beli_skrg
harga_buyback_skrg = harga_beli_skrg * (1 - (spread_persen / 100))
nilai_jual_hari_ini = gram_didapat * harga_buyback_skrg
rugi_hari_pertama = modal_awal - nilai_jual_hari_ini

st.markdown("#### 2. Kondisi Hari Pertama Kamu Beli")
res_col1, res_col2, res_col3 = st.columns(3)

res_col1.metric(label="Total Emas yang Didapat", value=f"{gram_didapat:.2f} Gram")
res_col2.metric(label="Jika Langsung Dijual Hari Ini", value=f"Rp {nilai_jual_hari_ini:,.0f}", delta=f"- Rp {rugi_hari_pertama:,.0f}", delta_color="inverse")
res_col3.info(f"💡 Ini karena harga *Buyback* toko hari ini hanya Rp {harga_buyback_skrg:,.0f}/gram.")

st.write("---")

st.markdown("#### 3. Butuh Berapa Tahun Untuk Untung?")
st.write("Grafik di bawah mensimulasikan kapan harga *buyback* akhirnya berhasil menyalip modal awalmu (garis biru).")

# Loop simulasi 10 tahun ke depan
data_emas = []
for tahun in range(0, 11):
    # Harga emas naik tiap tahun
    harga_beli_tahun_ini = harga_beli_skrg * ((1 + (kenaikan_tahunan / 100)) ** tahun)
    # Harga buyback tahun tersebut
    harga_buyback_tahun_ini = harga_beli_tahun_ini * (1 - (spread_persen / 100))
    # Nilai uang jika dijual di tahun tersebut
    nilai_pencairan = gram_didapat * harga_buyback_tahun_ini
    
    data_emas.append({
        "Tahun ke-": tahun,
        "Modal Awalku (Rp)": modal_awal,
        "Nilai Pencairan Emas (Rp)": nilai_pencairan
    })

df_emas = pd.DataFrame(data_emas).set_index("Tahun ke-")

# Garis biru untuk modal, Garis kuning/oranye untuk nilai pencairan
st.line_chart(df_emas, color=["#1f77b4", "#ffb300"]) 

st.divider()

# ==========================================
# BAGIAN 4: TIPS PRO (HACKS)
# ==========================================
st.header("💡 Tips Pro: Memaksimalkan Investasi Emas")

st.warning(
    "**1. JANGAN Investasi di Emas Perhiasan!**\n\n"
    "Kalung atau gelang emas bukan alat investasi yang baik. Saat kamu beli, kamu membayar 'Ongkos Bikin' yang mahal. "
    "Namun saat dijual kembali, toko HANYA menghitung berat emasnya saja (ongkos bikin hangus). "
    "Belilah **Emas Batangan / Logam Mulia (seperti Antam/UBS)** yang *spread*-nya jauh lebih kecil dan jelas."
)

st.success(
    "**2. Emas Digital vs Emas Fisik**\n\n"
    "Kalau modalmu di bawah 1 gram, mulailah dari **Emas Digital** (bisa dibeli di aplikasi terpercaya mulai dari Rp 10.000). "
    "Emas digital tidak ada risiko hilang dicuri dan *spread*-nya biasanya lebih kecil dari emas fisik. "
    "Setelah terkumpul 5 atau 10 gram, barulah kamu cetak menjadi emas fisik untuk disimpan."
)