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
with open("style/peta.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

with open("images/location.jpg", "rb") as image_file:
    lokasi = base64.b64encode(image_file.read()).decode()

with open("images/peta.jpg", "rb") as image_file:
    map = base64.b64encode(image_file.read()).decode()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

st.markdown(f"""
    <style>
    .try-banner {{
            background-image: linear-gradient(to left, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.8)), url('data:image/jpg;base64,{lokasi}');
            background-reapat: no-reapet;
            background-size: cover;
            background-position:center;
        }}
    </style>
    <div class="container-fluid try-banner banner">
        <div class="container banner-content">
            <div class="waste">
                <div class="text-center text-light">
                    <h1 class="judul1">Pemetaan Sistem Pengelolaan dan Transportasi Pengangkutan Sampah RW 09 Suryatmajan</h1>
                </div>
            </div>
        </div>
    </div>
""" , unsafe_allow_html=True)

st.markdown(f"""
<div class="container-fluid py-5">
    <div class="container">
        <h2 class="text-center">Pemetaan dan Jalur Transportasi Pengangkutan Sampah RW 09</h2>
        <hr class="mb-5 custom-hr">
    </div>
    <div class= "col-lg-8 offset-lg-2">
        <p class="tulisan">
            Di wilayah RW 09 Kelurahan Suryatmajan, terdapat enam tempat sampah yang strategis untuk 
            mendukung pengelolaan sampah berbasis lingkungan. Tiga di antaranya adalah tempat sampah 
            kompos yang ditempatkan di titik-titik yang mudah dijangkau oleh warga, khususnya di dekat 
            area perumahan yang menghasilkan banyak limbah organik. Selain itu, terdapat tiga tempat 
            sampah pilah, masing-masing untuk sampah organik, anorganik, dan kompos, yang diletakkan di 
            lokasi pusat aktivitas warga seperti balai pertemuan RW dan dekat dengan akses jalan utama. 
            Penempatan ini dirancang agar memudahkan warga dalam membuang sampah sesuai jenisnya 
            sekaligus mendukung proses pengolahan sampah yang lebih terorganisir.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    f"""
<div class="container-fluid bg py-5">
    <h2 class= "text-center">Peta Jalur Pemetaan dan Transportasi</h2>
    <hr class="mb-5 custom-hr">
    <div class="container">
        <div class="text-center">
            <img src="data:image/jpeg;base64,{map}" class="image">
        </div>
    </div>
</div>
""", unsafe_allow_html=True)