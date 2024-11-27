import streamlit as st
import streamlit as st
from PIL import Image
import base64
import io

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
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


with open("style/umum.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

with open("images/umum.jpg", "rb") as image_file:
    umum = base64.b64encode(image_file.read()).decode()

with open("images/map.jpg", "rb") as image_file:
    peta = base64.b64encode(image_file.read()).decode()


with open("images/history.jpg", "rb") as image_file:
    history = base64.b64encode(image_file.read()).decode()

with open("images/visi.jpg", "rb") as image_file:
    visi = base64.b64encode(image_file.read()).decode()

with open("images/mission.jpg", "rb") as image_file:
    misi = base64.b64encode(image_file.read()).decode()

with open("images/visi.jpg", "rb") as image_file:
    vision = base64.b64encode(image_file.read()).decode()
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------


st.markdown(f"""
    <style>
    .try-banner {{
            background-image: linear-gradient(to left, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.8)), url('data:image/jpg;base64,{umum}');
            background-reapat: no-reapet;
            background-size: cover;
            background-position:center;
        }}
    </style>
    <div class="container-fluid try-banner banner">
        <div class="container banner-content">
            <div class="waste">
                <div class="text-center text-light">
                    <h1 class="judul1">Gambaran Umum RAPI Bank Sampah</h1>
                </div>
            </div>
        </div>
    </div>
""" , unsafe_allow_html=True)


# Geografis
st.markdown(f"""
    <div class="py-5 container-fluid">
        <div class="container">
            <h2 class="text-center">Geografis</h2>
            <div class="text-center mb-5">
                <img src="data:image/jpeg;base64,{peta}">
            </div>
            <p class="geografis">
                “RAPI” BANK SAMPAH berada di wilayah Kampung Gemblakan Bawah RW 09 Kelurahan Suryatmajan Kemantren Danurejan Yogyakarta. 
                Secara Geografis berada di ketinggian 112 meter diatas permukaan laut dengan curah hujan rata-rata 1000mm/thn. Suhu rata 
                rata mencapai 28 derajat Celcius dengan kelembapan udara rata rata 70% per tahun. 
                Wilayah Kampung Gemblakan Bawah RW 09 Kelurahan Suryatmajan di sebelah Utara berbatasan dengan Kampung Gemblakan Bawah RW 
                08, sebelah Selatan berbatasan dengan Kampung Cokrodirjan, disisi Barat berbatasan dengan Kampung Gemblakan Bawah RW 08, 
                dan di sisi Timur berbatasan dengan kampung ledok Tukungan Kelurahan Tegal Panggung. Selain itu Wilayah Kampung Gemblakan 
                Bawah RW 09 Kelurahan Suryatmajan Kemantren Danujeran Yogyakarta terdiri dari 3 RT dan 1 RW.
            <p>
        </div>
    </div>   
""", unsafe_allow_html=True)

# Sejarah
st.markdown(f"""
<style>
    .banner-sejarah {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.8)), url('data:image/jpg;base64,{history}');
            background-reapat: no-reapet;
            background-size: cover;
            background-position:center;
        }}
</style>
<div class="container-fluid bg py-5 banner-sejarah text-light">
    <h2 class="text-center mb-5">Sejarah</h2>
    <div class="container sejarah">
        <div class="mb-5 gambar">
        </div>
        <p class="mb-5">
            Bank Sampah "RAPI" didirikan pada 9 September 2012 di Kampung Gemblakan Bawah, RW 09, Kelurahan Suryatmajan, Kemantren 
            Danurejan, Yogyakarta. Bank ini mengelola berbagai jenis sampah plastik seperti bungkus deterjen, pembersih lantai, 
            kemasan minuman instan, hingga gelas plastik. Sampah-sampah yang dikumpulkan dari warga sekitar dipilah berdasarkan motif 
            dan ukuran, lalu dicuci, dikeringkan, dan dipotong sesuai kebutuhan. Dengan sistem bagi hasil, warga yang menyetor sampah 
            plastik mendapatkan imbalan tahunan. Proses kreatif mulai terlihat saat sampah plastik dirangkai menjadi produk seperti 
            tas cantik, yang memerlukan ketelitian agar motifnya seragam serta kekuatan tambahan dari ikatan benang.
        </p>
        <p>
            Setelah sempat tidak aktif pada 2017 karena kesibukan para pengurusnya, Bank Sampah "RAPI" kembali bangkit pada 2020 
            dengan menerapkan sistem donasi sampah. Sampah yang didonasikan diolah dan hasil penjualannya digunakan untuk menyediakan 
            barang-barang berguna bagi anggota. Model ini memberikan manfaat langsung kepada masyarakat sambil terus mempromosikan 
            pengelolaan sampah yang berkelanjutan.
        </p>
    </div>   
</div>
""", unsafe_allow_html=True)

# VISI dan MISI
st.markdown(f"""
<div class="container-fluid py-5">
    <h2 class="text-center mb-5">Visi dan Misi</h2>
    <div class="container">
        <div class="row">
            <div class="col-md-6 mision">
                <img src="data:image/jpeg;base64,{vision}">
            </div>
            <div class="col-md-6">
                <h3 class="text-center mt-5">Visi</h3>
                <p class="mb-5 visi text-center">Bank sampah sebagai wadah untuk mewujudkan masyarakat yang peduli terhadap lingkungan.</p>
                <h3 class="text-center">Misi</h3>
                <ol class="visi mb-5">
                    <li>Mengajak masyarakat untuk peduli terhadap lingkungan.</li>
                    <li>Memberikan pendidikan terhadap masyarakat agar sadar tentang pentingnya menjaga lingkungan dan kesehatan.</li>  
                    <li>Memberdayakan masyarakat dengan memanfaatkan sampah.</li>
                </ol>
            </div>
        </div>   
    </div>
</div>
""", unsafe_allow_html=True)