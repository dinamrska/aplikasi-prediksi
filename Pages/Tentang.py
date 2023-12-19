import streamlit as st
from PIL import Image

st.title("Logo")

image = Image.open("Team logo/blacpink-logo.jpeg")

new_size = (350, 400)

resized_image = image.resize(new_size)

st.image(resized_image)

## info about the team
st.write("Blackpink (bahasa Korea: 블랙핑크, digayakan dalam huruf kapital semua atau sebagai BLɅƆKPIИK) adalah grup vokal wanita asal Korea Selatan. Blackpink dibentuk oleh YG Entertainment dengan beranggotakan empat orang, diantaranya Jennie, Jisoo, Lisa, dan Rosé.")
st.write("Blackpink merupakan grup vokal wanita Korea yang memiliki lagu dengan posisi tertinggi di Billboard Hot 100, berada di nomor 55 dengan Ddu-Du Ddu-Du, dan di Billboard 200, berada di nomor 40 dengan EP berjudul Square Up. Blackpink merupakan grup pop Korea perempuan pertama dan satu-satunya yang memasuki dan memuncaki Emerging Artists Billboard.")

st.subheader("Di bawah adalah para member")

## for Player
st.header("Member BlackPink")
st.info('Jennie, Jisoo, Lisa, dan Rosé')
lead=Image.open('Team logo/Team.jpeg')
size=(400, 400)
lead_image=lead.resize(size)
st.image(lead_image)

st.subheader("Connect dengan BlackPink: ")

# Button to send an Instagram 
if st.button("Contact Me Via Instagram"):
    st.markdown('<a href="https://www.instagram.com/blackpinkofficial/">Send Instagram</a>', unsafe_allow_html=True)

# Button to visit Twitter
if st.button("visit My Twitter"):
    st.markdown('<a href="https://twitter.com/BLACKPINK">Twitter</a>', unsafe_allow_html=True)

