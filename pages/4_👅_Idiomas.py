import streamlit as st
from PIL import Image

# Page config
st.set_page_config(
    page_title="Languages",
    page_icon="🌍",
)

# Introductory text
col1 = st.columns(1)

with col1:
    st.markdown('<div style="font-size: 14px">Olá! Eu sou Aline Gomes!!</div>', unsafe_allow_html=True)


  st.text("")

# Two columns: English and French
col2, col3 = st.columns(2)

with col1:
    image_en = Image.open("Bandeira_do_USA.png")
    st.image(image_en, width=200)
    st.slider("English", 0, 100, 30)

with col2:
    image_fr = Image.open("Bandeira_do_SPAN.png")  # use the name you saved for the second image
    st.image(image_fr, width=200)
    st.slider("French", 0, 100, 70)
