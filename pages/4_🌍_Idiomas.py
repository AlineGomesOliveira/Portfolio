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
<p>In 2007 I decided to improve my English proficiency and moved to Toronto, Canada, where I stayed until 2008 studying the language and doing some construction work to pay for my stay there.</p>

<p>Between 2016 and 2018 I returned to live in Canada, this time in Montreal, and took the opportunity to learn French. I also had the opportunity to work at WADA (World Anti Doping Agency) doing administrative services, where I put into practice what I had learned about English and French.</p>

<p>And speaking of Canada, in none of these times did I ever meet Luisa!!</p>
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
