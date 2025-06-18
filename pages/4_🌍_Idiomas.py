import streamlit as st
from PIL import Image

# Page config
st.set_page_config(
    page_title="Languages",
    page_icon="🌍",
)

# Estilo personalizado para reduzir o tamanho do texto
st.markdown("""
<style>
    .small-text {
        font-size:16px !important;
        line-height:1.5;
    }
    .slider-container {
        text-align: center;
    }
    .slider-container img {
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Texto com fonte reduzida
st.markdown("""
<div class="small-text">
<p>Over the years, I've developed different levels of proficiency in English, Spanish, and Dutch — each one shaped by personal and meaningful experiences.</p>

<p>I started learning Spanish on my own, inspired by family members who lived in Buenos Aires and often shared the culture and language with me. That influence sparked my curiosity and helped me reach an advanced level.</p>

<p>As for Dutch and English, I’ve been constantly exposed to both thanks to my aunt, who has been living in Amsterdam for over 20 years. Every call with her is a real-life language lesson — she encourages us to speak and practice in both languages, which has helped me maintain a basic level of Dutch and develop my intermediate English skills through regular use.</p>
</div>
""", unsafe_allow_html=True)

# Colunas lado a lado com sliders abaixo das imagens
col1, col2, col3 = st.columns(3)

with col1:
    with st.container():
        st.markdown('<div class="slider-container">', unsafe_allow_html=True)
        image_en = Image.open("Bandeira_do_USA.png")
        st.image(image_en, width=150)
        st.slider("English", 0, 100, 40)
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="slider-container">', unsafe_allow_html=True)
        image_fr = Image.open("Bandeira_da_SPAN.png")  # substitua conforme nome salvo
        st.image(image_fr, width=150)
        st.slider("Espanhol", 0, 100, 70)
        st.markdown('</div>', unsafe_allow_html=True)

with col3:
    with st.container():
        st.markdown('<div class="slider-container">', unsafe_allow_html=True)
        image_fr = Image.open("Bandeira_da_HOLANDA.png")  # substitua conforme nome salvo
        st.image(image_fr, width=150)
        st.slider("Holandes", 0, 100, 20)
        st.markdown('</div>', unsafe_allow_html=True)
