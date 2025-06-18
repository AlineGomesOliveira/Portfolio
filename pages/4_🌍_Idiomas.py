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
<p>Ao longo dos anos, desenvolvi diferentes níveis de proficiência em inglês, espanhol e holandês — cada um deles moldado por experiências pessoais e significativas..</p>

<p>Comecei a aprender espanhol sozinha, inspirada por familiares que moraram em Buenos Aires e sempre compartilharam comigo a cultura e o idioma. Essa influência despertou minha curiosidade e me ajudou a alcançar um nível avançado.</p>

<p>Quanto ao holandês e ao inglês, tive contato frequente com os dois graças à minha tia, que vive em Amsterdã há mais de 20 anos. Cada ligação com ela é uma verdadeira aula de idiomas — ela nos incentiva a praticar e conversar em ambas as línguas, o que tem me ajudado a manter um nível básico de holandês e a desenvolver um nível intermediário de inglês com o uso constante.</p>
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
