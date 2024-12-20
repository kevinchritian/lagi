import streamlit as st

# st.title("Hello world")

home = st.Page(
    page = "views/home.py",
    title='Home',
    icon=":material/home:",
    default= True
)

about = st.Page(
    page = "views/about.py",
    icon=":material/groups_2:",
    title='Tentang Kami',
)

sampah = st.Page(
    page = "views/sampah.py",
    icon=":material/delete_forever:",
    title='Sampah',
)

sampah_organik = st.Page(
    page = "views/organik.py",
    icon=":material/compost:",
    title='Sampah Organik',
)

sampah_anorganik = st.Page(
    page = "views/anorganik.py",
    icon=":material/water_bottle_large:",
    title='Sampah Anorganik',
)

AI = st.Page(
    page = "views/AI.py",
    icon=":material/smart_toy:",
    title = "AI",
)

Suryatmajan = st.Page(
    page = "views/Suryatmajan.py",
    # icon= ":material"
    title= "Tentang RAPI Bank Sampah"
)

Peta= st.Page(
    page = "views/Peta.py",
    # icon= ":material"
    title= "Jalur Peta Tempat Pembuangan Sampah"
)

# Gambaran Umum
Umum = st.Page(
    page="views/Umum.py",
    title="Gambaran Umum RAPI Bank Sampah"
)

# Organisasi
Organisasi= st.Page(
    page="views/Organisasi.py",
    title="Organisasi RAPI Bank Sampah"
)

# Kegiatan Kerja
Kegiatan= st.Page(
    page="views/Kegiatan.py",
    title= "Kegiatan Kerja RAPI Bank Sampah"
)

Pengolahan = st.Page(
    page="views/Pengolahan.py",
    title= "Penanganan Sampah Organik dan Anorganik"
)


pg = st.navigation(
    {
    "Info" : [home,about],
    "Projects" :[sampah, sampah_organik, sampah_anorganik, AI],
    'RAPI BANK SAMPAH' :[Suryatmajan, Organisasi, Umum, Kegiatan, Pengolahan],
    "Peta Suryatmajan" :[Peta]
    }
)



pg.run()


hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden; }
    </style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)

