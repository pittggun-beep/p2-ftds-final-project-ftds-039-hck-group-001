import streamlit as st

st.set_page_config(page_title="EduInvest by RencanaKita - Belajar Investasi dari Nol", layout="wide")

st.title("🌱 Selamat Datang di EduInvest by RencanaKita!")
st.write("Belajar investasi gak harus pusing dengan istilah ribet. Yuk, bangun fondasi keuanganmu di sini.")

st.divider()

# Pilar 1: Fondasi Keuangan
st.header("🧠 3 Langkah Sebelum Mulai Investasi")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1. Atur Budget (50/30/20)")
    st.write("Pisahkan gajimu: 50% untuk kebutuhan pokok (makan, kos, tagihan), 30% untuk keinginan (ngopi, nonton), dan **20% untuk masa depan (tabungan & investasi)**.")

with col2:
    st.subheader("2. Amankan Dana Darurat")
    st.write("Sebelum beli aset apa pun, pastikan kamu punya pegangan uang tunai setara **3 sampai 6 bulan pengeluaranmu**. Ini penting biar kamu gak perlu mencairkan investasi saat ada keadaan darurat.")

with col3:
    st.subheader("3. Lunasi Utang Konsumtif")
    st.write("Jika masih punya utang dengan bunga tinggi seperti Paylater atau Kartu Kredit, **lunasi itu dulu**. Bunga utang konsumtif biasanya jauh lebih besar daripada keuntungan investasi.")

st.divider()

# Pilar 2: Cek Profil Risiko Singkat
st.header("🎯 Kenali Karakter Investasimu")
st.write("Setiap orang punya toleransi yang berbeda terhadap risiko kehilangan uang. Pilih pernyataan yang paling menggambarkan dirimu:")

karakter = st.radio(
    "Bagaimana sikapmu jika uang investasimu turun 10% dalam sebulan?",
    (
        "A. Panik banget! Saya mau uang saya aman-aman saja dan pasti untung walaupun kecil.",
        "B. Sedikit khawatir, tapi saya paham itu wajar asal turunnya gak terlalu banyak.",
        "C. Biasa saja. Saya siap rugi besar demi bisa untung yang jauh lebih besar di masa depan."
    )
)

if st.button("Lihat Profil Risikoku"):
    if "A" in karakter:
        st.success("🤖 **Profilmu: Konservatif / Averse**. Kamu cocok dengan instrumen super aman seperti **Deposito atau Reksadana Pasar Uang**. Silakan buka menu di samping untuk mulai belajar!")
    elif "B" in karakter:
        st.info("🤖 **Profilmu: Moderat / Cautious**. Kamu siap mengambil risiko kecil yang terukur. Kamu cocok dengan **Obligasi Negara**. Yuk, pelajari di menu samping!")
    else:
        st.warning("🤖 **Profilmu: Agresif / Hungry**. Kamu adalah tipe pemburu keuntungan besar dan gak takut melihat saldo naik-turun ekstrem. Menu **Saham** sangat cocok untukmu!")