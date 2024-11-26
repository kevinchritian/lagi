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


with open("style/latarbelakang.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

with open("images/RAPI.png", "rb") as image_file:
    RAPI = base64.b64encode(image_file.read()).decode()

with open("images/bannerRapi.jpg", "rb") as image_file:
    banner = base64.b64encode(image_file.read()).decode()

with open("images/tujuan.jpg", "rb") as image_file:
    goal = base64.b64encode(image_file.read()).decode()

with open("images/benefit.jpg", "rb") as image_file:
    manfaat = base64.b64encode(image_file.read()).decode()

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
                <div class="gambar-banner text-center mb-3">
                    <img src="data:image/jpeg;base64,{RAPI}">
                </div>
                <div class="text-center">
                    <h1 class="judul1">RAPI <span>Bank Sampah</h1>
                </div>
            </div>
        </div>
    </div>
""" , unsafe_allow_html=True)

# latar belakang
st.markdown(f"""
    <div class ="container-fluid py-5">
        <h2 class="text-center mb-5">Latar Belakang</h2>            
        <div class="container">
            <div class="latarbelakang">
                <p>
                    Sampah merupakan hasil sisa dari aktivitas manusia 
                    yang sering kali tidak dikelola dengan baik, sehingga 
                    menimbulkan masalah lingkungan. Peningkatan jumlah 
                    penduduk dan konsumsi masyarakat turut meningkatkan 
                    volume sampah, terutama dari rumah tangga yang 
                    berkontribusi hingga 50-60%. Sistem pengelolaan sampah 
                    tradisional seperti kumpul-angkut-buang hanya memindahkan 
                    masalah tanpa mengurangi volume sampah. Kebiasaan membuang 
                    sampah sembarangan, seperti ke sungai atau pinggir jalan, 
                    memperburuk situasi, meskipun sudah ada upaya seperti menyediakan 
                    tong sampah. Untuk itu, diperlukan kesadaran masyarakat dalam mengelola 
                    sampah langsung dari sumbernya sebagai langkah strategis.
                </p>
                <p>
                    Berawal dari keresahan terhadap pengelolaan sampah yang kurang 
                    optimal, "RAPI" BANK SAMPAH hadir di Kampung Gemblakan Bawah RW 09, 
                    Yogyakarta, sebagai solusi inovatif. Bank Sampah ini bertujuan 
                    meningkatkan kesadaran masyarakat akan pentingnya pengelolaan sampah 
                    yang tepat guna. Dengan pendekatan berbasis kemandirian dan 
                    kebersamaan, Bank Sampah tidak hanya membantu mengurangi sampah 
                    tetapi juga mendorong perilaku peduli lingkungan. Inisiatif ini 
                    diterima baik oleh masyarakat setempat, menjadi langkah nyata dalam 
                    mengatasi permasalahan sampah di tingkat lokal.
                </p>
            <div>
        </div>
    </div>
""", unsafe_allow_html=True)


# Tujuan
st.markdown(f"""
    <div class="container-fluid bg py-5">
        <div class="container">
            <h2 class="text-center mb-5">Tujuan</h2>
            <div class="row">
                <div class="tujuan col-lg-6">
                    <p>
                        "RAPI" BANK SAMPAH didirikan sebagai wujud apresiasi 
                        terhadap lingkungan dan niat untuk mengatasi permasalahan 
                        sosial, ekonomi, serta mendukung program pemerintah dalam 
                        penanggulangan sampah. Tujuannya adalah meningkatkan kesadaran 
                        masyarakat untuk peduli terhadap lingkungan, membiasakan pemilahan 
                        sampah organik dan anorganik, serta mendorong kemandirian dalam 
                        mengelola sampah tanpa bergantung pada pemerintah. Dengan sistem 
                        Bank Sampah, masyarakat dapat mengelola sampah di lingkungan mereka 
                        sendiri, terbebas dari iuran sampah, dan memperoleh penghasilan 
                        tambahan dari tabungan sampah, sekaligus membantu menciptakan lingkungan 
                        yang bersih dan sehat.
                    </p>
                </div>
                <div class="col-lg-6 image mt-5 mt-lg-0 text-center">
                    <img src="data:image/jpeg;base64,{goal}" class="gambar">
                </div>
            </div>
            <h2 class="text-center my-5">Manfaat</h2>
            <div class="row">
                <div class="col-lg-6 text-center mb-5">
                    <img src="data:image/jpeg;base64,{manfaat}" class="gambar">
                </div>
                <div class="col-lg-6">
                    <p class="manfaat mb-5">
                        Manfaat dari “RAPI” Bank Sampah adalah membuat 
                        lingkungan menjadi bersih, sehat, indah dan asri. 
                        Selain itu menjadikan sampah sebagai tabungan yang 
                        mempunyai nilai ekonomi, serta membuka peluang bagi 
                        masyarakat untuk berkarya secara kreatif.
                    </p>
                </div>
            </div>
            <div class="manfaat">
                <p>
                    Melihat dari tujuan dan manfaat dari "RAPI" BANK 
                    SAMPAH, sasaran utama yang ingin dicapai adalah 
                    adanya perubahan sikap, kesadaran, dan kebisaaan masyarakat 
                    dalam mengelola sampah. Sampah yang sebelumnya dianggap tidak 
                    berguna kini dapat menjadi sumber ekonomi. Untuk mencapai hal 
                    ini, "RAPI" BANK SAMPAH berupaya membangun kesadaran dan 
                    mendorong perubahan sikap serta kebiasaan masyarakat dengan 
                    memperkenalkan konsep RAPI" BANK SAMPAH. Mereka memberi contoh 
                    tentang cara menjadi nasabah dan cara membuang sampah di "RAPI" 
                    Bank Sampah, sehingga perubahan tersebut dapat muncul  dari kesadaran 
                    dan inisiatif masyarakat itu sendiri.
                </p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)



# Konten
st.markdown(f"""
    <div class="container-fluid py-5">
        <div class="container">
            <h2 class="text-center mb-5">RAPI Bank Sampah</h2>
            <div class="row">
                <div class="col-lg-3">
                    <div class="card shadow mb-4 h-100">
                        <img src="data:image/jpeg;base64,{manfaat}" class="card-img-top">
                        <div class="card-body d-flex flex-column">
                            <h5 class="card-title fw-bold">Gambaran Umum, Visi, dan Misi</h5>
                            <p class="card-text">Gambaran umum, visi, dan misi RAPI Bank Sampah</p>
                            <a href="" target="_self" class="mt-auto">
                                <button class="btn btn-outline-info float-end">Lihat >></button>
                            </a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3">
                    <div class="card shadow mb-4 h-100">
                        <img src="data:image/jpeg;base64,{manfaat}" class="card-img-top">
                        <div class="card-body d-flex flex-column">
                            <h5 class="card-title fw-bold">Organisasi</h5>
                            <p class="card-text">Organisasi Bank Sampah</p>
                            <a href="" target="_self" class="mt-auto">
                                <button class="btn btn-outline-info float-end">Lihat >></button>
                            </a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3">
                    <div class="card shadow mb-4 h-100">
                        <img src="data:image/jpeg;base64,{manfaat}" class="card-img-top">
                        <div class="card-body d-flex flex-column">
                            <h5 class="card-title fw-bold">Kegiatan Kerja RAPI Bank Sampah</h5>
                            <p class="card-text">Pengertian, jenis jenis, dan dampak sampah</p>
                            <a href="" target="_self" class="mt-auto">
                                <button class="btn btn-outline-info float-end">Lihat >></button>
                            </a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-3">
                    <div class="card shadow mb-4 h-100">
                        <img src="data:image/jpeg;base64,{manfaat}" class="card-img-top">
                        <div class="card-body d-flex flex-column">
                            <h5 class="card-title fw-bold">Pengolahan Anorganik dan Organik</h5>
                            <p class="card-text">Pengolahan sampah organik dan anorganik pada RAPI Bank Sampah</p>
                            <a href="" target="_self" class="mt-auto">
                                <button class="btn btn-outline-info float-end">Lihat >></button>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>           
""", unsafe_allow_html=True)



# Konten
