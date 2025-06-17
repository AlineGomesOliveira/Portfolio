import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(
    page_title="Idiomas",
    page_icon=="🌎",
)

com rua.recipiente():
    col1, col2, col3 = rua.colunas(3)

    com col1:
        rua.redução_de_preço("")

    com col2:
        rua.redução_de_preço("")

    com col3:
        rua.redução_de_preço("")

    rua.redução_de_preço("###### Em 2007 decidi melhorar minha proficiência no Inglês e me mudei para Toronto no Canadá, onde fiquei até 2008 estudando esse idioma e fazendo alguns trabalhos na área da construção para custear minha estadia por lá.")
    rua.redução_de_preço("###### Entre 2016 a 2018 voltei a morar no Canadá, dessa vez em Montreal e aproveitei para aprender o idioma Francês. Também tive a oportunidade de trabalhar na WADA(World Anti Doping Agency) fazendo serviços administrativos, onde coloquei em prática o que aprendi sobre Inglês e Francês.")
    rua.redução_de_preço("###### E por falar em Canadá, em nenhuma dessas vezes encontrei a Luísa!!")

    col4, col5 = rua.colunas(2)

    com col4:
        imagem_en = Imagem.abrir('Bandeira_do_USA.png')
        rua.imagem(imagem_en, imagem_largura=200)
        rua.controle_deslizante("Inglês", 0, 100, 30)

    com col5:
        imagem_fr = Imagem.abrir('Bandeira_do_SPAN.png')
        rua.imagem(imagem_fr, imagem_largura=200)
        rua.controle_deslizante("Francês", 0, 100, 70)

    




