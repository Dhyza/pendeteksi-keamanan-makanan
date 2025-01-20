import streamlit as st
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="Food Freshness App", page_icon="🍎", layout="wide")

# Palet Warna
PRIMARY_COLOR = "#4CAF50"
SECONDARY_COLOR = "#F44336"
BACKGROUND_COLOR = "#E3F2FD"  # Biru muda
TEXT_COLOR = "#333333"
ACCENT_COLOR = "#FFC107"

# CSS Kustom
st.markdown(f"""
    <style>
    .main {{
        background-color: {BACKGROUND_COLOR} !important;
        color: {TEXT_COLOR};
        font-family: 'Poppins', sans-serif;
    }}
    .stApp {{
        background-color: {BACKGROUND_COLOR} !important;
    }}
    .stButton>button {{
        background-color: {PRIMARY_COLOR};
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 16px;
        transition: 0.3s;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    }}
    .stButton>button:hover {{
        background-color: {SECONDARY_COLOR};
        transform: scale(1.05);
    }}
    .sidebar .sidebar-content {{
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    }}
    h1, h2, h3 {{
        color: {PRIMARY_COLOR};
    }}
    .title {{
        font-size: 36px;
        font-weight: bold;
        color: {PRIMARY_COLOR};
    }}
    .subtitle {{
        font-size: 24px;
        color: {TEXT_COLOR};
        margin-bottom: 20px;
    }}
    .image-container {{
        text-align: center;
        margin: 20px 0;
    }}
    </style>
""", unsafe_allow_html=True)


# --- Efek Animasi Balon dan Salju ---
def animation_effect():
    st.balloons()
    for _ in range(5):
        st.markdown('<div class="snowflake">❄️</div>', unsafe_allow_html=True)


# --- Navigasi Sidebar ---
menu = st.sidebar.selectbox("📂 Menu", [
    "🏠 Beranda", 
    "🧮 Penilaian Kelayakan Makanan", 
    "🔍 Deteksi Perubahan Fisik Makanan", 
    "📖 Panduan Penyimpanan", 
    "🍽️ Resep & Tips Memasak", 
    "📰 Artikel Edukasi", 
    "💬 Forum Diskusi",
    "ℹ️ Info"
])

from datetime import datetime
import streamlit as st
import numpy as np

# --- Beranda ---
if menu == "🏠 Beranda":
    st.title("🍎 FRESH CHECK - Pendeteksi Kelayakan Konsumsi Makanan")

    # Gambar lebih menarik mencakup semua kategori makanan
    st.image("https://www.ybkb.or.id/wp-content/uploads/2024/03/shopping-bag-full-fresh-fruits-vegetables-with-assorted-ingredients-min-825x551_yUwnK.jpg")

    # Deskripsi aplikasi dengan ikon dan bullet point yang lebih menarik
    st.markdown("""
    ### 🌟 Selamat Datang di **Pendeteksi Kelayakan Konsumsi Makanan**!  
    Aplikasi ini dirancang untuk membantu Anda mengonsumsi makanan yang **sehat** dan **aman** dengan fitur-fitur menarik berikut:

    - 📅 **Pengecekan Tanggal Kedaluwarsa**: Pantau masa simpan makanan agar tetap aman.  
    - 🔍 **Deteksi Perubahan Fisik Makanan**: Identifikasi tanda-tanda kerusakan pada makanan.  
    - ❄️ **Tips Penyimpanan Optimal**: Rekomendasi penyimpanan agar makanan tahan lama.  
    - 🍳 **Saran Pengolahan & Konsumsi**: Ide olahan lezat dari bahan yang tersedia.  
    - 📊 **Penilaian Kelayakan Makanan**: Hitung kelayakan konsumsi makanan Anda secara cepat.  
    - 📖 **Panduan Penyimpanan**: Pelajari cara menyimpan makanan dengan benar.  
    - 📰 **Artikel Edukasi**: Baca artikel informatif tentang keamanan dan nutrisi makanan.  
    - 💬 **Forum Diskusi**: Berbagi pengalaman dan tips dengan pengguna lainnya.
    """)

     # Tambahkan tombol untuk langsung menuju fitur utama
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 Penilaian Kelayakan Makanan"):
            st.success("Silakan buka menu 📊 Penilaian Kelayakan Makanan di sidebar!")
    
    with col2:
        if st.button("📖 Lihat Resep Sehat"):
            st.success("Silakan buka menu 📚 Resep & Tips Memasak di sidebar!")

    # Catatan di bagian bawah
    st.markdown("---")
    st.info("💡 **Tips:** Jaga kesehatan dengan memilih makanan bergizi dan mengolahnya dengan cara yang tepat!")

# --- Penilaian Kelayakan Makanan ---
if menu == "🧮 Penilaian Kelayakan Makanan":
    st.title("🔍 Penilaian Kelayakan Makanan")

    jenis_makanan = st.selectbox("🍽️ Pilih Jenis Makanan", [
        "Sayuran 🥦", "Buah-buahan 🍎", "Daging 🍖", 
        "Susu & Produk Olahan 🥛", "Roti & Kue 🍞", 
        "Makanan Kaleng 🥫", "Minuman 🥤"
    ])

    tanggal_input = st.date_input("📅 Tanggal Pembelian")

    kondisi_penyimpanan = st.selectbox("❄️ Kondisi Penyimpanan", [
        "Suhu Ruang 🌡️", "Kulkas (0–4°C) ❄️", "Freezer (-18°C) 🧊"
    ])
    perubahan_fisik = st.multiselect("⚠️ Perubahan Fisik", [
        "Perubahan warna 🎨", "Bau tidak sedap 🤢", 
        "Tekstur berlendir 🦠", "Jamur 🍄"
    ])

    
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Fungsi untuk mengirim email notifikasi
def kirim_notifikasi_email(email_pengguna, jenis_makanan, hari_tanggal):
    try:
        # Setup email
        pengirim_email = "your_email@example.com"  # Ganti dengan email pengirim
        password_email = "your_password"  # Ganti dengan password pengirim
        penerima_email = email_pengguna
        
        # Buat pesan email
        msg = MIMEMultipart()
        msg['From'] = pengirim_email
        msg['To'] = penerima_email
        msg['Subject'] = f"Peringatan Kedaluwarsa {jenis_makanan}"
        
        body = f"""
        Hallo,

        Kami ingin mengingatkan Anda bahwa {jenis_makanan} Anda hampir kedaluwarsa pada {hari_tanggal}.
        Harap pastikan untuk segera mengonsumsinya atau memeriksanya kembali.

        Terima kasih,
        Pendeteksi Kelayakan Makanan
        """
        msg.attach(MIMEText(body, 'plain'))
        
        # Kirim email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(pengirim_email, password_email)
            server.sendmail(pengirim_email, penerima_email, msg.as_string())
        
        st.success("Notifikasi email berhasil dikirim!")
    except Exception as e:
        st.error(f"Error mengirim email: {e}")

# Integrasi fitur notifikasi di dalam alur penilaian kelayakan makanan
if menu == "🧮 Penilaian Kelayakan Makanan":
    email_pengguna = st.text_input("📧 Masukkan Email Anda untuk Notifikasi", "")
    
    if st.button("🔎 Cek Kelayakan"):
        animation_effect()
        hari_ini = datetime.now().date()
        lama_simpan = (hari_ini - tanggal_input).days

        if tanggal_input > hari_ini:
            st.error("❗ Tanggal yang Anda masukkan tidak valid. Silakan masukkan tanggal yang logis.")
        else:
            if perubahan_fisik:
                st.error("❌ Makanan tidak layak dikonsumsi!")
                st.write("⚠️ *Perubahan fisik pada makanan menandakan kerusakan.*")
            else:
                batas_penyimpanan = {
                    "Daging 🍖": {"Freezer (-18°C) 🧊": 180, "Kulkas (0–4°C) ❄️": 3, "Suhu Ruang 🌡️": 1},
                    "Sayuran 🥦": {"Freezer (-18°C) 🧊": 12, "Kulkas (0–4°C) ❄️": 7, "Suhu Ruang 🌡️": 2},
                    "Buah-buahan 🍎": {"Freezer (-18°C) 🧊": 30, "Kulkas (0–4°C) ❄️": 7, "Suhu Ruang 🌡️": 3},
                    "Susu & Produk Olahan 🥛": {"Kulkas (0–4°C) ❄️": 7, "Suhu Ruang 🌡️": 1},
                    "Roti & Kue 🍞": {"Kulkas (0–4°C) ❄️": 5, "Suhu Ruang 🌡️": 2},
                    "Makanan Kaleng 🥫": {"Suhu Ruang 🌡️": 365},
                    "Minuman 🥤": {"Kulkas (0–4°C) ❄️": 7, "Suhu Ruang 🌡️": 3}
                }

                batas_hari = batas_penyimpanan.get(jenis_makanan, {}).get(kondisi_penyimpanan, 0)

                if lama_simpan > batas_hari:
                    st.error("❌ Makanan sudah tidak layak dikonsumsi.")
                elif (batas_hari - lama_simpan) <= 2:
                    st.warning(f"⚠️ Makanan hampir kedaluwarsa dalam {batas_hari - lama_simpan} hari!")
                    st.success("✅ Makanan masih layak dikonsumsi.")
                else:
                    st.success("✅ Makanan masih layak dikonsumsi.")
                    st.info(f"🗓️ Lama penyimpanan: {lama_simpan} hari dari batas {batas_hari} hari.")


# --- Deteksi Perubahan Fisik Makanan ---
if menu == "🔍 Deteksi Perubahan Fisik Makanan":
    st.title("🔍 Deteksi Perubahan Fisik Makanan")

    st.markdown("""
    Identifikasi tanda-tanda kerusakan pada makanan berdasarkan kategori berikut:
    """)

    # Pilihan kategori makanan
    kategori = st.selectbox(
        "Pilih Kategori Makanan",
        ["Buah", "Sayur", "Susu & Produk Olahan", "Roti & Kue", "Makanan Olahan"]
    )

    # Informasi tanda kerusakan berdasarkan kategori
    if kategori == "Buah":
        st.subheader("🍎 Tanda Kerusakan pada Buah")
        st.markdown("""
        - Warna kulit berubah menjadi cokelat atau hitam.  
        - Tekstur menjadi lembek atau berlendir.  
        - Muncul bercak hitam atau jamur.  
        - Aroma asam atau bau tidak sedap.  
        """)
        st.image("https://unair.ac.id/wp-content/uploads/2021/12/Foto-oleh-Pinterests.jpg")

    elif kategori == "Sayur":
        st.subheader("🥦 Tanda Kerusakan pada Sayur")
        st.markdown("""
        - Warna daun menguning atau menghitam.  
        - Tekstur layu dan berlendir.  
        - Muncul bercak busuk atau jamur.  
        - Aroma busuk atau asam.  
        """)
        st.image("https://st.depositphotos.com/1009322/3656/i/450/depositphotos_36569393-stock-photo-rotten-vegetables.jpg")

    elif kategori == "Susu & Produk Olahan":
        st.subheader("🥛 Tanda Kerusakan pada Susu & Produk Olahan")
        st.markdown("""
        - Aroma asam yang menyengat.  
        - Tekstur menggumpal atau mengental.  
        - Rasa asam atau tidak segar.  
        - Warna berubah keruh atau kekuningan.  
        """)
        st.image("https://asset.kompas.com/crops/Dp0ZM45tY7UdSOlPJ1uZxA2IyzM=/0x92:840x652/1200x800/data/photo/2023/11/06/654878358cf8a.png")

    elif kategori == "Roti & Kue":
        st.subheader("🍞 Tanda Kerusakan pada Roti & Kue")
        st.markdown("""
        - Muncul bercak hijau atau hitam (jamur).  
        - Tekstur menjadi keras atau lembek.  
        - Aroma apek atau asam.  
        """)
        st.image("https://asset.kompas.com/crops/yswLRikqooU6_6Z31ZKjPJD0gbM=/73x31:935x605/750x500/data/photo/2022/09/24/632ed22643668.jpg")

    elif kategori == "Makanan Olahan":
        st.subheader("🥫 Tanda Kerusakan pada Makanan Olahan")
        st.markdown("""
        - Kemasan menggelembung atau penyok.  
        - Bau menyengat atau tidak biasa saat dibuka.  
        - Warna dan tekstur berubah.  
        - Adanya lapisan minyak atau berlendir.  
        """)
        st.image("https://radarlombok.co.id/wp-content/uploads/2017/06/F-TAK-LAYAK-696x549.jpg")

    st.markdown("---")
    st.info("💡 **Tips:** Simpan makanan sesuai anjuran agar lebih tahan lama dan terhindar dari kerusakan.")

# --- Resep & Tips Memasak ---
elif menu == "🍽️ Resep & Tips Memasak":
    st.title("🍳 Resep & Tips Memasak Makanan Sehat")
    kategori_makanan = st.selectbox("🥘 Pilih Jenis Makanan", [
        "Sayuran", "Buah-buahan", "Daging", "Roti & Kue"
    ])

    if kategori_makanan == "Sayuran":
        st.subheader("Resep Sayuran Segar")
        st.write("Berikut adalah resep tumis sayuran segar:")
        st.code("Tumis bayam dengan bawang putih dan saus tiram.")
    elif kategori_makanan == "Buah-buahan":
        st.subheader("Resep Salad Buah")
        st.write("Berikut adalah resep salad buah yang sehat:")
        st.code("Campurkan potongan buah dengan yogurt dan madu.")
    elif kategori_makanan == "Daging":
        st.subheader("Resep Daging Panggang")
        st.write("Berikut adalah resep daging panggang:")
        st.code("Marinasi daging dengan bumbu, lalu panggang hingga matang.")
    elif kategori_makanan == "Roti & Kue":
        st.subheader("Resep Roti Panggang")
        st.write("Berikut adalah resep roti panggang yang enak:")
        st.code("Panggang roti dengan mentega dan taburan gula kayu manis.")

# --- Forum Diskusi ---
elif menu == "💬 Forum Diskusi":
    st.title("💬 Forum Diskusi Makanan dan Kesehatan")
    st.markdown("""
    Selamat datang di forum diskusi!  
    Di sini Anda bisa bertanya atau berbagi pengalaman terkait makanan dan kesehatan.  
    - Bagaimana cara memilih makanan sehat?  
    - Apa tips agar makanan tetap segar lebih lama?  
    - Diskusikan resep dan tips memasak yang sehat.
    """)
    st.text_area("💬 Tuliskan pertanyaan atau komentar Anda di sini:", height=200)

# --- Panduan Penyimpanan ---
elif menu == "📖 Panduan Penyimpanan":
    st.title("📖 Panduan Penyimpanan & Saran Pengolahan")
    kategori = st.selectbox("🍲 Pilih Kategori Makanan", ["Sayuran", "Buah-buahan", "Daging", "Roti & Kue"])
    if kategori == "Roti & Kue":
        st.subheader("🍞 Roti & Kue")
        st.write("- Simpan dalam wadah kedap udara untuk mencegah jamur.\n- Simpan di kulkas untuk memperpanjang umur simpan.")
        st.info("💡 Olahan: Roti panggang, puding roti.")
    elif kategori == "Sayuran":
        st.subheader("🥦 Sayuran")
        st.write("- Cuci dan keringkan sebelum disimpan.\n- Bungkus dengan tisu atau plastik berlubang.\n- Simpan di kulkas dalam crisper drawer.")
        st.info("💡 Olahan: Tumis sayur, sup sayur.")
    elif kategori == "Buah-buahan":
        st.subheader("🍎 Buah-buahan")
        st.write("- Simpan buah matang di kulkas.\n- Pisahkan buah yang cepat matang seperti pisang.\n- Jangan mencuci sebelum disimpan untuk menghindari kelembapan.")
        st.info("💡 Olahan: Smoothie, salad buah.")
    elif kategori == "Daging":
        st.subheader("🍖 Daging")
        st.write("- Simpan di freezer dalam wadah tertutup.\n- Hindari mencairkan dan membekukan ulang.")
        st.info("💡 Olahan: Daging panggang, sup daging.")

# --- Resep & Tips Memasak ---
if menu == "📚 Resep & Tips Memasak":
    st.title("📚 Resep Lezat & Tips Memasak Aman")
    kategori_resep = st.selectbox("🍳 Pilih Kategori", ["Sayuran", "Buah", "Daging"])
    
    if kategori_resep == "Sayuran":
        st.subheader("🥬 Tumis Kangkung Bawang Putih")
        st.markdown("**Bahan-bahan:**")
        st.markdown("""
        - 1 ikat kangkung  
        - 3 siung bawang putih, cincang  
        - Garam dan kaldu bubuk secukupnya  
        """)
        
        st.markdown("**Cara Membuat:**")
        st.markdown("""
        1. Tumis bawang putih hingga harum.  
        2. Masukkan kangkung, aduk hingga layu.  
        3. Tambahkan garam dan kaldu bubuk, aduk rata.  
        4. Angkat dan sajikan.  
        """)
        st.image("https://cdn.pixabay.com/photo/2020/05/17/16/05/water-spinach-5182212_960_720.jpg", caption="Tumis Kangkung Bawang Putih")

    # Resep Buah
    elif kategori_resep == "Buah":
        st.subheader("🍓 Salad Buah Segar")
        st.markdown("**Bahan-bahan:**")
        st.markdown("""
        - Potongan melon, semangka, apel  
        - Yogurt plain  
        - Madu secukupnya  
        """)
        
        st.markdown("**Cara Membuat:**")
        st.markdown("""
        1. Campurkan semua potongan buah ke dalam mangkuk.  
        2. Tambahkan yogurt dan madu.  
        3. Aduk hingga merata dan sajikan dingin.  
        """)
        st.image("https://cdn.pixabay.com/photo/2017/06/02/18/24/salad-2367014_960_720.jpg", caption="Salad Buah Segar")

    # Resep Daging
    elif kategori_resep == "Daging":
        st.subheader("🥩 Steak Daging Sapi Simple")
        st.markdown("**Bahan-bahan:**")
        st.markdown("""
        - 200g daging sapi  
        - Garam dan lada secukupnya  
        - Mentega untuk memanggang  
        """)

        st.markdown("**Cara Membuat:**")
        st.markdown("""
        1. Lumuri daging dengan garam dan lada.  
        2. Panaskan teflon dan lelehkan mentega.  
        3. Panggang daging sesuai tingkat kematangan yang diinginkan.  
        4. Sajikan dengan sayuran rebus atau kentang.  
        """)
        st.image("https://cdn.pixabay.com/photo/2016/11/18/16/47/beef-1834641_960_720.jpg", caption="Steak Daging Sapi")

# --- Artikel Edukasi ---
elif menu == "📰 Artikel Edukasi":
    st.title("📚 Artikel Edukasi Seputar Kesehatan dan Gizi")
    st.markdown("""
    - [**Keamanan Pangan: Cara Memastikan Makanan Aman Dikonsumsi**](https://www.who.int/news-room/fact-sheets/detail/food-safety)
    - [**Tips Memilih Bahan Makanan Berkualitas**](https://health.detik.com/diet/d-5309576/8-tips-memilih-bahan-makanan-segar-dan-berkualitas)
    - [**Dampak Kesehatan Akibat Konsumsi Makanan Tidak Aman**](https://hellosehat.com/nutrisi/fakta-gizi/bahaya-makanan-tidak-sehat/)
    """)

# --- Forum Diskusi ---
elif menu == "💬 Forum Diskusi":
    st.title("💬 Forum Diskusi")
    komentar = st.text_area("Bagikan Pengalaman Anda:")
    if st.button("Kirim"):
        st.success("Terima kasih telah berbagi!")
        

# --- Info ---
elif menu == "ℹ️ Info":
    st.title("ℹ️ Informasi Pembuat Aplikasi")
    st.markdown("""
    **Aplikasi ini dikembangkan oleh:**

    - 👩‍💻 **Azzahra Sadrina Nadzifa (2350080)**
    - 👩‍💻 **Dhyza Aulia Shabirah (2350084)**
    - 👩‍💻 **Diyan Theda Mufarrihah (2350085)** 
    - 👩‍💻 **Haija Nafiah (2350094)**
    - 👨‍💻 **Irsan Abdurrahman (2350100)**

    Dibuat dengan ❤️ oleh Kelompok 10

    D-IV Nanoteknologi Pangan
    
    Politeknik AKA Bogor
    """)


# --- Footer ---
st.markdown("---")
st.caption("🥗 *Dirancang untuk mendukung gaya hidup sehat dan aman setiap hari.*")



