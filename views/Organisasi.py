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


with open("style/organisasi.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


with open("images/a.jpg", "rb") as image_file:
    banner = base64.b64encode(image_file.read()).decode()

with open("images/ketua.png", "rb") as image_file:
    ketua = base64.b64encode(image_file.read()).decode()

with open("images/pengurus1.png", "rb") as image_file:
    pengurus1 = base64.b64encode(image_file.read()).decode()

with open("images/pengurus2.png", "rb") as image_file:
    pengurus2 = base64.b64encode(image_file.read()).decode()

with open("images/pengurus3.png", "rb") as image_file:
    pengurus3 = base64.b64encode(image_file.read()).decode()

with open("images/pengurus4.png", "rb") as image_file:
    pengurus4 = base64.b64encode(image_file.read()).decode()
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown(f"""
    <style>
    .try-banner {{
            background-image: linear-gradient(to left, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.8)), url('data:image/jpg;base64,{banner}');
            background-reapat: no-reapet;
            background-size: cover;
            background-position:center;
        }}
    </style>
    <div class="container-fluid try-banner banner">
        <div class="container banner-content">
            <div class="waste">
                <div class="text-center warna">
                    <h1>Organisasi RAPI BANK SAMPAH</h1>
                </div>
            </div>
        </div>
    </div>
""" , unsafe_allow_html=True)


# organisasi

# Ketua
st.markdown(f"""
<div class="container-fluid py-5">
    <div class="profile-area">
        <div class="container">    
        <h2 class="text-center"> Ketua RAPI BANK SAMPAH</h2>
        <hr class="mb-5 custom-hr">
        <div class="row">
            <div class="col-md-4 mb-5">
            </div>
            <div class="col-md-4 mb-5">
                <div class="card">
                    <div class="img1"><img src="data:image/jpeg;base64,{banner}" alt="Image 1"></div>
                    <div class="img2"><img src="data:image/jpeg;base64,{ketua}" alt="Image 2"></div>
                    <div class="main-text">
                        <h2>Fenny Kurniawaty</h2>
                        <p>
                            <strong>Ketua RAPI BANK SAMPAH </strong><br>
                            <strong>Tgl Lahir:</strong> Yogyakarta, 10 Desember 1981<br>
                            <strong>Pendidikan:</strong> SMU<br>
                            <strong>Alamat:</strong> RT 26
                        </p>
                    </div>
                </div>
            </div>
                <div class="col-md-4 mb-5">
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)



# Pengurus
st.markdown(f"""
<div class="container-fluid py-5 color">
    <div class="profile-area">
        <div class="container">    
        <h2 class="text-center">Pengurus RAPI Bank Sampah</h2>
        <hr class="mb-5 custom-hr">
        <div class="row">
            <div class="col-lg-4 col-md-6 mb-5">
                <div class="card">
                    <div class="img1"><img src="data:image/jpeg;base64,{banner}" alt="Image 1"></div>
                    <div class="img2"><img src="data:image/jpeg;base64,{pengurus1}" alt="Image 2"></div>
                    <div class="main-text">
                        <h2>Sujarwati</h2>
                        <p>
                            <strong>Sekretaris RAPI BANK SAMPAH</strong><br>
                            <strong>Tgl Lahir:</strong> Gunung Kidul 5 Juni 1983<br>
                            <strong>Pendidikan:</strong> SMK<br>
                            <strong>Alamat:</strong> RT 27
                        </p>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-5">
                <div class="card">
                    <div class="img1"><img src="data:image/jpeg;base64,{banner}" alt="Image 1"></div>
                    <div class="img2"><img src="data:image/jpeg;base64,{pengurus2}" alt="Image 2"></div>
                    <div class="main-text">
                        <h2>lestari</h2>
                        <p>
                            <strong>Bendahara BANK SAMPAH </strong><br>
                            <strong>Tgl Lahir:</strong> Yogyakarta, 11 Februari 1974<br>
                            <strong>Pendidikan:</strong> SMP<br>
                            <strong>Alamat:</strong> RT 26
                        </p>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-5">
                <div class="card">
                    <div class="img1"><img src="data:image/jpeg;base64,{banner}" alt="Image 1"></div>
                    <div class="img2"><img src="data:image/jpeg;base64,{pengurus3}" alt="Image 2"></div>
                    <div class="main-text">
                        <h2>Desma Tricahyaningrum</h2>
                        <p>
                            <strong>Sie Penimbangan / Penjualan</strong><br>
                            <strong>Tgl Lahir:</strong> Yogyakarta, 30 Desember 1988<br>
                            <strong>Pendidikan:</strong> SMK<br>
                            <strong>Alamat:</strong> RT 27
                        </p>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-5">
                <div class="card">
                    <div class="img1"><img src="data:image/jpeg;base64,{banner}" alt="Image 1"></div>
                    <div class="img2"><img src="data:image/jpeg;base64,{pengurus4}" alt="Image 2"></div>
                    <div class="main-text">
                        <h2>Yuliningsih</h2>
                        <p>
                            <strong>Sie Penimbangan / Penjualan</strong><br>
                            <strong>Tgl Lahir:</strong> Bantul, 25 Juli 1986<br>
                            <strong>Pendidikan:</strong> SMK<br>
                            <strong>Alamat:</strong> RT 27
                        </p>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-5">
                <div class="card">
                    <div class="img1"><img src="data:image/jpeg;base64,{banner}" alt="Image 1"></div>
                    <div class="img2"><img src="data:image/jpeg;base64,{banner}" alt="Image 2"></div>
                    <div class="main-text">
                        <h2>eni kristiani</h2>
                        <p>
                            <strong>unknown</strong><br>
                            <strong>Tgl Lahir:</strong> unknown<br>
                            <strong>Pendidikan:</strong> unknown<br>
                            <strong>Alamat:</strong> unknown
                        </p>
                    </div>
                </div>
            </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)