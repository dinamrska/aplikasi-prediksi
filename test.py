import streamlit as st
from pydataset import data
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title = "Titanic",
    page_icon = "?",#emoji ikon untuk ikon tab,bisa dengan "random"
    layout = "wide", #centered atau #wide
    menu_items = {
        'Get Help' : None,  #atau string
        'Report a bug' : "https://google.com/",
        'About' : "Ini adalah about"
    },
    initial_sidebar_state = "auto",
)

st.title("Visualisai Dataset Titanic di Python dengan Streamlit")
st.caption("Ini adalah simulasi pembuatan web dashboard dengan streamlit menggunakan dataset Titanic")
st.image("https://img.okezone.com/content/2023/06/28/18/2838625/alasan-di-balik-bangkai-kapal-titanic-dibiarkan-di-dasar-samudra-antlantik-hlb15e0FPP.jpg", width=600)

g1, g2, g3 = st.columns([1,2,1])
with g1:
    st.write("")
with g3:
    st.write("")
with g2:
    st.image("https://img.okezone.com/content/2023/06/28/18/2838625/alasan-di-balik-bangkai-kapal-titanic-dibiarkan-di-dasar-samudra-antlantik-hlb15e0FPP.jpg", width=600)
    st.caption("Ini iliustrasi Titanic")

st.markdown('<div style="text-align:center">RMS Titanic adalah sebuah kapal penumpang super Britania Raya yang tenggelam di Samudra Atlantik Utara pada tanggal 15 April 1912 setelah menabrak sebuah gunung es pada pelayaran perdananya dari Southampton, Inggris ke New York City. Tenggelamnya Titanic mengakibatkan kematian sebanyak 1514 orang dalam salah satu bencana maritim masa dama paling mematikan sepanjang sejarah. Titanic merupakan kapal terbesar di dunia pada pelayaran perdananya. Satu dari tiga kapal samudra kelas Olympic dioperasikan oleh White Star Line. Kapal ini dibangun pada 1909 sampai 1911 oleh galangan kapal Harland and Wolff di Belfast. Kapal ini sanggup mengangkut 2,224 penumpang.</div>', unsafe_allow_html=True)

st.markdown('<div style="text-align:center">RMS Titanic adalah sebuah kapal penumpang super Britania Raya yang tenggelam di Samudra Atlantik Utara pada tanggal 15 April 1912 setelah menabrak sebuah gunung es pada pelayaran perdananya dari Southampton, Inggris ke New York City. Tenggelamnya Titanic mengakibatkan kematian sebanyak 1514 orang dalam salah satu bencana maritim masa dama paling mematikan sepanjang sejarah. Titanic merupakan kapal terbesar di dunia pada pelayaran perdananya. Satu dari tiga kapal samudra kelas Olympic dioperasikan oleh White Star Line. Kapal ini dibangun pada 1909 sampai 1911 oleh galangan kapal Harland and Wolff di Belfast. Kapal ini sanggup mengangkut 2,224 penumpang.</div>', unsafe_allow_html=True)

titanic = data('titanic')
st.markdown('<h4 style="text-align=center">Visualiasasi Dataset Titanic</h4>',
            unsafe_allow_html=True)
st.markdown('<h5 style="text-align=justify">Menampilkan Dataset</h5>',
            unsafe_allow_html=True)
with st.expander('Dataset Titanic', expanded=False):
    st.dataframe(titanic)

expender = '''with st.expander('Dataset Titanic', expanded=False):
    st,dataframe(titanic)'''
st.code(expender, 'python')

pla, plb = st.columns([1,3])

with pla:
    st.markdown('<h6 style="text-align:center">widget input yang digunakan: Select Box</h6>', unsafe_allow_html=True)
    sb = st.selectbox('pilih variabel:',['class','age','sex','survived'])

with plb:
    pie = px.pie(titanic, names=sb)
    st.plotly_chart(pie)

pla, plb = st.columns([1,3])

with pla:
    st.markdown('<h6 style="text-align:center">widget input yang digunakan: Radio Box</h6>', unsafe_allow_html=True)
    rd = st.radio('pilih variabel:',['class','age','sex','survived'])

with plb:
    pie1 = px.pie(titanic, names=rd)
    st.plotly_chart(pie1)