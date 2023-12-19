#Load libraries needed
import streamlit as st


# set page configuration
st.set_page_config(
    page_title="Selamat datang di Aplikasi Time Series",
    page_icon="☠️",
    layout="wide",
)

# Add content
st.markdown("# 👋Selamat datang di Aplikasi Prediksi penjualan Produk di seluruh toko")

# Add image
st.image("https://www.animatedimages.org/data/media/707/animated-welcome-image-0280.gif")

# Add CSS for animation
st.write("""
    <style>
        @keyframes slide-in {
         0% {
            transform: translate(-100%);
        }
         100% {
            transform: translate(0);
        }
    }
    .slide-in-animation {
         animation: slide-in 1.5s ease-in-out; 
    }
    </style>
""", unsafe_allow_html=True)        

# Text with animation
st.write('<div class="slide-in-animation"> isinya </div>', unsafe_allow_html=True)

# add a sidebar to select pages
st.sidebar.success("Pilih halaman di atas.")


# create a streamlite container for the subheader
subheader_container = st.container()

# define the subheader content
subheader_content = """
<div class="slide-in-animation">
<h3>hal yang dapat anda lakukan di aplikasi ini:</h3>
<ul>
  <li>Perkiraan Penjualan pada tanggal Tertentu untuk Toko Favorita.</li>
  <li>Lihat kumpulan data dan berinteraksi dengan visual yang menunjukkan penjualan harian di seluruh toko</li>
  <li>Kenali lebih banyak tentang tim</li>
</ul>
</div>
"""

# Apply CSS animation using HTML/CSS
subheader_container.markdown(subheader_content, unsafe_allow_html=True)

# Add CSS for animation
st.write("""
    <style>
        @keyframes slide-in {
         0% {
            transform: translate(-100%);
        }
         100% {
             transform: translate(0);
        }
    }
    .slide-in-animation {
         animation: slide-in 1.5s ease-in-out; 
    }
    </style>
""", unsafe_allow_html=True) 