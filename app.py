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
    title= "Tentang RAPI BANK SAMPAH"
)

# Sejarah

# Organisasi

# Kegiatan Kerja



pg = st.navigation(
    {
    "Info" : [home,about],
    "Projects" :[sampah, sampah_organik, sampah_anorganik, AI],
    'RAPI BANK SAMPAH' :[Suryatmajan]
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

