import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="EduInvest by RencanaKita- Saham", layout="wide")

# ==========================================
# FUNGSI UNTUK MEMBACA FILE CSV 
# ==========================================
@st.cache_data
def load_stock_data(ticker):
    """
    Fungsi ini dibuat untuk membaca data emiten yang sudah bersih dan siap pakai dari file CSV.
    """
    nama_file = f"{ticker}.csv" 
    
    try:
        df = pd.read_csv(nama_file)
        
        # Mengubah kolom Date menjadi format datetime agar sumbu X di grafik rapi
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])
            
        return df
    
    except FileNotFoundError:
        st.error(f"🚨 File {nama_file} tidak ditemukan! Pastikan nama file sama persis dengan nama ticker.")
        # Mengembalikan dataframe kosong agar aplikasi tidak mati total
        return pd.DataFrame()

# Sesuaikan daftar ini dengan 15 file CSV yang lo punya
daftar_emiten = [
    'BBCA', 'BBRI', 'BMRI', 'BBNI', 'TLKM', 
    'ASII', 'ICBP', 'UNVR', 'GOTO', 'AMMN', 
    'ADRO', 'PTBA', 'UNTR', 'KLBF', 'MYOR'
]

# ==========================================
# LAYOUT HALAMAN STREAMLIT
# ==========================================
st.title("🏢 Level 5: Saham (Equities)")
st.subheader("Beli bisnisnya, bukan sekadar menebak grafik. Jadilah pemilik dari perusahaan-perusahaan raksasa.")

st.divider()

# ==========================================
# BAGIAN 1: EDUKASI FUNDAMENTAL & ANALOGI
# ==========================================
st.header("🧠 Pahami Mindset yang Benar")

st.info(
    "💡 **Apa itu Saham?**\n\n"
    "Saham adalah **bukti kepemilikan suatu perusahaan**. Ketika kamu membeli saham, kamu sebenarnya membeli sebagian kecil dari bisnis tersebut. ")

st.info(
    "💡 **Analogi Buka Usaha:** Beli saham itu ibarat temanmu membuka kedai kopi dengan modal Rp 100 Juta, lalu dia membagi kepemilikannya "
    "menjadi 100 lembar (per lembar Rp 1 Juta). Jika kamu membeli 10 lembar, kamu resmi menjadi pemilik 10% kedai kopi tersebut. "
    "Kamu berhak atas keuntungannya, tapi juga ikut menanggung risiko jika kedai itu sepi."
)

st.write("---")

# Template 3 Pillars untuk Faktor Penggerak Harga
st.markdown("### 🎢 Apa yang Mempengaruhi Naik-Turun Harga Saham?")
st.write("Sangat banyak faktor yang menggerakkan harga saham setiap detiknya, di antaranya:")

col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    st.success(
        "**🏢 Kinerja Perusahaan**\n\n"
        "Mesin utama penggerak harga:\n"
        "- 📈 **Pendapatan Meningkat:** Harga saham cenderung naik.\n"
        "- 📉 **Laba Menurun:** Harga saham cenderung turun (dijual investor)."
    )

with col_f2:
    st.warning(
        "**🌍 Kondisi Ekonomi**\n\n"
        "Faktor makro dari luar perusahaan:\n"
        "- 📈 **Ekonomi Tumbuh:** Daya beli kuat, pasar saham menghijau.\n"
        "- 📉 **Resesi / Krisis:** Masyarakat menahan uang, menekan harga saham anjlok."
    )

with col_f3:
    st.info(
        "**📰 Sentimen Pasar**\n\n"
        "Psikologis ketakutan & keserakahan manusia:\n"
        "- 📈 **Berita Positif:** (Misal: perusahaan menang tender besar) mendorong harga naik.\n"
        "- 📉 **Berita Negatif:** (Misal: skandal korupsi direktur) memicu panik jual."
    )

st.write("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📈 Cara Cuan dari Saham")
    st.success(
        "Pemula sering lupa kalau untung di saham itu ada dua sumber:\n"
        "1. **Capital Gain:** Untung dari selisih harga jual dan beli.\n"
        "2. **Dividen:** Pembagian laba bersih perusahaan secara tunai kepada pemegang saham. "
    )
    
with col2:
    st.markdown("### 🎯 Untuk Siapa Aset Ini?")
    st.warning(
        "Ini adalah arena bagi tipe investor **Open** dan **Hungry** (Agresif). Harga saham sangat bergejolak setiap hari. "
        "Hanya gunakan **uang dingin** (uang yang tidak akan kamu pakai dalam waktu minimal 5 tahun ke depan)."
    )

st.divider()

# ==========================================
# BAGIAN 2: INTERAKTIF GRAFIK LILIN & VOLUME
# ==========================================
st.header("📊 Membaca Pergerakan Pasar")
st.write("Grafik di bawah menggunakan standar profesional: **Candlestick** untuk melihat rentang harga harian, dan **Volume** (diagram batang di bawah) untuk melihat seberapa ramai saham tersebut ditransaksikan.")

with st.expander("Klik di sini untuk belajar cara membaca Grafik Lilin 🕯️"):
    st.markdown("""
    - **Lilin Hijau:** Harga Naik. Artinya harga Tutup (*Close*) lebih tinggi dari harga Buka (*Open*).
    - **Lilin Merah:** Harga Turun. Artinya harga Tutup (*Close*) lebih rendah dari harga Buka (*Open*).
    - **Sumbu Atas & Bawah (Wick):** Menunjukkan jejak harga Tertinggi (*High*) dan Terendah (*Low*) yang sempat disentuh.
    """)

# Interaktif Selectbox
pilihan_saham = st.selectbox("Pilih Emiten yang Ingin Kamu Analisa:", daftar_emiten)

# Membaca data dari file CSV yang dipilih
df_pilihan = load_stock_data(pilihan_saham)

# Mencegah error jika file CSV tidak ditemukan
if not df_pilihan.empty:
    
    # --- MEMBUAT LAYOUT PROFESIONAL (SUBPLOTS) ---
    fig = make_subplots(
        rows=2, cols=1, 
        shared_xaxes=True, 
        vertical_spacing=0.03, 
        row_heights=[0.75, 0.25]
    )

    # 1. Menambahkan Trace Candlestick ke Baris 1
    fig.add_trace(go.Candlestick(
        x=df_pilihan['Date'],
        open=df_pilihan['Open'],
        high=df_pilihan['High'],
        low=df_pilihan['Low'],
        close=df_pilihan['Close'],
        name='Harga'
    ), row=1, col=1)

    # 2. Menentukan warna Volume (Hijau jika harga naik, Merah jika harga turun)
    colors = ['#2ca02c' if row['Close'] >= row['Open'] else '#d62728' for index, row in df_pilihan.iterrows()]

    # 3. Menambahkan Trace Bar (Volume) ke Baris 2
    fig.add_trace(go.Bar(
        x=df_pilihan['Date'], 
        y=df_pilihan['Volume'],
        marker_color=colors,
        name='Volume'
    ), row=2, col=1)

    # 4. Merapikan Layout keseluruhan
    fig.update_layout(
        title=f'Pergerakan Harga & Volume Saham {pilihan_saham}',
        template='plotly_dark',
        height=650, 
        showlegend=True,
        xaxis_rangeslider_visible=False, 
        margin=dict(l=20, r=20, t=50, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Grafik tidak dapat ditampilkan karena data tidak tersedia.")

st.divider()

# ==========================================
# BAGIAN 3: ANALISA DAPUR PERUSAHAAN (FUNDAMENTAL)
# ==========================================
st.header("🔍 Membaca Fundamental Perusahaan ")
st.write("Sebelum membeli grafik di atas, pastikan bisnis di baliknya sehat. Mari kita ambil contoh metrik dari emiten **Big Banks**:")

col_f1, col_f2 = st.columns(2)
with col_f1:
    st.success("**1. ROE (Return on Equity)**\n\nMengukur seberapa pintar manajemen mencetak laba bersih dari modal yang kamu setor. Jika ROE Bank di atas 15%, artinya mesin bisnis mereka sangat efisien.")
with col_f2:
    st.warning("**2. PBV (Price to Book Value)**\n\nMengukur apakah saham sedang murah atau kemahalan. PBV = 1 artinya harga wajar. Jika bank krisis dan PBV-nya di bawah 1, itu mungkin saat yang tepat memborong sahamnya!")

st.divider()

# ==========================================
# BAGIAN 4: TIPS PRO (HACKS)
# ==========================================
st.header("💡 Tips Pro: Bertahan Hidup di Pasar Saham")

st.error(
    "**Hindari Saham Gorengan!**\n\n"
    "Pemula sangat dilarang menyentuh saham perusahaan kecil yang tidak jelas bisnisnya, "
    "meskipun harganya sering naik ratusan persen dalam sehari. Uangmu bisa nyangkut selamanya. "
    "Mulailah dari perusahaan *Blue-Chip* yang produknya kamu gunakan setiap hari."
)