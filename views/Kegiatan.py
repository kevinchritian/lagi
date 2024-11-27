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
with open("style/kegiatan.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
with open("images/kerja.jpg", "rb") as image_file:
    kerja = base64.b64encode(image_file.read()).decode()

with open("images/mekanisme.jpg", "rb") as image_file:
    kerja1 = base64.b64encode(image_file.read()).decode()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------



st.markdown(f"""
    <style>
    .try-banner {{
            background-image: linear-gradient(to left, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.8)), url('data:image/jpg;base64,{kerja}');
            background-reapat: no-reapet;
            background-size: cover;
            background-position:center;
        }}
    </style>
    <div class="container-fluid try-banner banner">
        <div class="container banner-content">
            <div class="waste">
                <div class="text-center text-light">
                    <h1 class="judul1">Kegiatan Kerja RAPI BANK SAMPAH</h1>
                </div>
            </div>
        </div>
    </div>
""" , unsafe_allow_html=True)


# info
st.markdown("""
    <div class="conatiner-fluid py-5 bg">
        <h2 class="mb-5 text-center">Kegiatan Kerja</h2>
        <div class="container">
            <div class="col-md-10 offset-lg-1">
                <p class="mb-5 info">
                    Jam operasional “RAPI” BANK SAMPAH adalah setiap bulan sekali yaitu 
                    pada tanggal 15 pukul 16.00 WIB, bersama dengan kegiatan PKK RW 09 
                    Gemblakan Bawah. Kegiatan meliputi :
                </p>
            </div>
                <ol>
                    <li class="mb-3"><strong>Mengadakan koordinasi serta menjalin kerjasama dengan dinas terkait.</strong> Hal ini bertujuan agar berjalannya “RAPI” BANK SAMPAH sesuai peraturan serta regulasi yang terkait dengan pengolaan sampah dan bank sampah yang ada di daerah. Contoh kerjasama yaitu bank sampah telah mendapatkan bantuan dari dinas lingkungan hidup beruapa mesin jahit dan tong pengomposan. Disisi lain produk produk hasil bank sampah yang telah jadi dapat dipinjam atau dibeli denagn harga murah oleh lingkungan hidup sebagai bukti bahwa pengeloaan sampah dan bank sampah Di Yogyakarta sudah berjalan dengan baik.</li>
                    <li class="mb-3">
                        <strong>Mengadakan sosialisasi dan penyuluhan.</strong> “RAPI” BANK SAMPAH mencoba mengajak semua masyarakat untuk peduli terhadap 
                        lingkungan dengan mengelola sampah secara bijak. Masyarakat akan diberikan pengetahuan tentang sampah yang dianggap 
                        remeh, menjadi barang yang berguna dan ekonomis. Sosialisasi dan penyuluhan yang dilakukan oleh “RAPI” BANK SAMPAH 
                        diharapkan mempu membuat masyarakat sadar dan mau mengelola sampah secara bijak.
                        Sosialisasi dan penyuluhan oleh “RAPI” BANK SAMPAH melalui :
                        <ul>
                            <li>Pendekatan secara pribadi masyarakat</li>
                            <li>Kunjungan kerumah-rumah</li>
                            <li>Tatap muka dengan masyarakat</li>
                            <li>Kegiatan-kegiatan yang ada di kampung</li>
                            <li>Internet jejaring sosial</li>
                        </ul>
                    </li>
                    <li class="mb-3">
                        <strong>Mengadakan pengelolaan dan pengolahan sampah.</strong> “RAPI” BANK SAMPAH melakukan pengelolaan serta pengolahan bank sampah 
                        sendiri. Hal ini dilakukan untuk memperbadayakan masyarakat sekitar dalam pengolahan sampah. Selain itu dapat meningkatkan 
                        pendapatan masyarakat sekitar dan masyarakat juga dapat menabung di “RAPI” BANK SAMPAH karena mendapatkan manfaat secara 
                        langsung.
                    </li>
                    <li class="mb-3">
                        <strong>Bekerjasama dengan bank sampah lain.</strong> Sampah yang ada tidak bisa 100% dikelola oleh “RAPI” BANK SAMPAH, dikarenakan 
                        kurangnya inovasi “RAPI” BANK SAMPAH. Sampah sampah yang tidak bisa dikelola oleh “RAPI” BANK SAMPAH akan dijual ke bank 
                        sampah lain.
                    </li>
                    <li class="mb-3">
                        <strong>Mengadakan rapat dan evaluasi setiap 3 buan sekali.</strong> Rapat dan evaluasi dilakukan untuk memnetukan tujuan keddepan “RAPI” 
                        BANK SAMPAH dan mengontrol apakah kegiatan di bank samaph sudah mencapai tujuan atau belum.
                    </li>
                </ol>
        </div>
    </div>
""", unsafe_allow_html=True)


# Mekanisme
st.markdown(f"""
<style>
    .try-banner1 {{
            background-image: linear-gradient(to left, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.8)), url('data:image/jpg;base64,{kerja1}');
            background-reapat: no-reapet;
            background-size: cover;
            background-position:center;
        }}
    </style>
<div class="container-fluid py-5 try-banner1 text-light">
    <div class="container">
        <h2 class="text-center mb-5">Mekanisme Kerja</h2>
        <ol>
            <li class="mb-2">
                Pemilahan sampah di rumah tangga. 
            </li>
            <li class="mb-2">Sampah yang sudah dipilah di bawa ke "RAPI" BANK SAMPAH </li>
            <li class="mb-2">Di "RAPI" BANK SAMPAH pengelola akan menimbang sampah, mencatat di buku bantu tentang nama, jenis dan berat sampah yang di tabung.</li>
            <li class="mb-2">Pengelola menghubungi pembeli sampah. </li>
            <li class="mb-2">Setelah terjual pengelola akan memasukkan hasil penjualan sampah kedalam buku administrasi.</li> 
            <li class="mb-2">Pengelola membersihkan kembali tempat yang di pakai untuk Bank Sampah.</li>
        </ol>
    </div>
</div>
""", unsafe_allow_html=True)