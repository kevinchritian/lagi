import streamlit as st
import requests
import streamlit as st
from PIL import Image
import base64
import io

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
st.set_page_config(layout='wide')

hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem; padding-left:0rem; padding-right:0rem; padding-bottom:0rem;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

# Membaca file CSS dari file terpisah
with open("style/pengolahan.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
with open("images/pengolahan.jpg", "rb") as image_file:
    olah = base64.b64encode(image_file.read()).decode()

with open("images/cth.png", "rb") as image_file:
    anorganik1 = base64.b64encode(image_file.read()).decode()
with open("images/cth2.png", "rb") as image_file:
    anorganik2 = base64.b64encode(image_file.read()).decode()

with open("images/cth3.png", "rb") as image_file:
    anorganik3 = base64.b64encode(image_file.read()).decode()

with open("images/cth4.png", "rb") as image_file:
    anorganik4 = base64.b64encode(image_file.read()).decode()

with open("images/cth5.png", "rb") as image_file:
    anorganik5 = base64.b64encode(image_file.read()).decode()

with open("images/cth6.png", "rb") as image_file:
    anorganik6 = base64.b64encode(image_file.read()).decode()

with open("images/cth7.png", "rb") as image_file:
    anorganik7 = base64.b64encode(image_file.read()).decode()

with open("images/cth8.png", "rb") as image_file:
    anorganik8 = base64.b64encode(image_file.read()).decode()

with open("images/cth9.png", "rb") as image_file:
    anorganik9 = base64.b64encode(image_file.read()).decode()

with open("images/organik1.png", "rb") as image_file:
    organik1 = base64.b64encode(image_file.read()).decode()

with open("images/organik2.png", "rb") as image_file:
    organik2 = base64.b64encode(image_file.read()).decode()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

st.markdown(f"""
    <style>
    .try-banner {{
            background-image: linear-gradient(to left, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.8)), url('data:image/jpg;base64,{olah}');
            background-reapat: no-reapet;
            background-size: cover;
            background-position:center;
        }}
    </style>
    <div class="container-fluid try-banner banner">
        <div class="container banner-content">
            <div class="waste">
                <div class="text-center text-light">
                    <h1 class="judul1">Penanganan Sampah</h1>
                </div>
            </div>
        </div>
    </div>
""" , unsafe_allow_html=True)

# Anorganik
st.markdown(f"""
<div class="container-fluid py-5">
    <div class="container col-md-8">
        <h2 class="text-center mb-5">Kegiatan Penanganan Sampah anorganik (sampah kering)</h2>
        <div class="anorganik">
            <p><strong>1. Pemilahan Sampah</strong></p>
                <p>
                Setiap rumah tangga di RW 09 Kampung Gemblakan Bawah telah diberikan kantong pilah oleh DLH Kota Yogyakarta untuk 
                memilah sampah. Tingginya kesadaran warga mempermudah kerja "RAPI" BANK SAMPAH.
            </p>
            <p><strong>2. Penimbangan Sampah</strong></p>
                <p>Penimbangan dilakukan setiap tanggal 15 bersamaan dengan kegiatan PKK RW 09. Sampah anorganik yang ditabung warga 
                disimpan sementara di gudang yang terorganisir, seperti rumah botol untuk botol plastik dan rak container untuk kertas, 
                kaca, atau logam.
            </p>
            <p><strong>3. Penjualan Sampah Anorganik</strong></p>
                <p>Setelah ditimbang, sampah anorganik dijual kepada pelapak oleh pengurus "RAPI" BANK SAMPAH.
            </p>
            <p><strong>4. Pengadministrasian Tabungan Donasi</strong></p>
                <p>Semua kegiatan dicatat, dan di akhir tahun dilakukan tutup buku. Dana di kas dikembalikan kepada anggota dalam bentuk 
                alat kebersihan seperti sapu atau kemoceng.
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="container-fluid bg py-5">
    <div class="container">
        <p class="mb-5 gbr">Gambar penanganan sampah anorganik</p>
        <div class="row">
            <div class="col-lg-4 col-sm-6 mb-5">
                <div class="thumbnail">
                    <div class="img-container">
                        <img src="data:image/jpeg;base64,{anorganik1}" class="image">
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 mb-5">
                <div class="thumbnail">
                    <div class="img-container">
                        <img src="data:image/jpeg;base64,{anorganik2}" class="image">
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 mb-5">
                <div class="thumbnail">
                    <div class="img-container">
                        <img src="data:image/jpeg;base64,{anorganik3}" class="image">
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 mb-5">
                <div class="thumbnail">
                    <div class="img-container">
                        <img src="data:image/jpeg;base64,{anorganik4}" class="image">
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 mb-5">
                <div class="thumbnail">
                    <div class="img-container">
                        <img src="data:image/jpeg;base64,{anorganik5}" class="image">
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 mb-5">
                <div class="thumbnail">
                    <div class="img-container">
                        <img src="data:image/jpeg;base64,{anorganik6}" class="image">
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 mb-5">
                <div class="thumbnail">
                    <div class="img-container">
                        <img src="data:image/jpeg;base64,{anorganik7}" class="image">
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 mb-5">
                <div class="thumbnail">
                    <div class="img-container">
                        <img src="data:image/jpeg;base64,{anorganik8}" class="image">
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 mb-5">
                <div class="thumbnail">
                    <div class="img-container">
                        <img src="data:image/jpeg;base64,{anorganik9}" class="image">
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)



# Organik
st.markdown(f"""
<div class="container-fluid py-5">
    <div class="container col-md-8">
        <h2 class="text-center mb-5">Kegiatan Penanganan Sampah organik (sampah basah) </h2>
        <div class="anorganik">
            <p><strong>1. Losida (Lodong Sisa Dapur)</strong></p>
                <p>
                Losida adalah metode sederhana untuk mengurangi sampah organik di sumbernya. Setiap rumah menggunakan pipa khusus untuk 
                menampung sampah dapur, yang nantinya diolah menjadi pupuk atau produk lain yang bermanfaat.
            </p>
            <p><strong>2. Pembuatan Eco Enzyme</strong></p>
                <p>Eco enzyme adalah larutan fermentasi dari limbah organik seperti buah dan sayuran, dicampur dengan gula merah atau molase 
                    dan air. Larutan ini digunakan sebagai cairan serbaguna untuk kebutuhan rumah tangga, pertanian, hingga peternakan, karena 
                    mampu mempercepat proses bio-kimia di alam.
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="container-fluid bg py-5">
    <div class="container">
        <p class="mb-5 gbr">Gambar penanganan sampah organik</p>
        <div class="row">
            <div class="col-lg-4 col-sm-6 mb-5">
                <div class="thumbnail">
                    <div class="img-container">
                        <img src="data:image/jpeg;base64,{organik1}" class="image">
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 mb-5">
                <div class="thumbnail">
                    <div class="img-container">
                        <img src="data:image/jpeg;base64,{organik2}" class="image">
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)