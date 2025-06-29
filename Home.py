import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Aline Gomes Portifolio",
    page_icon="🏚️",
)



#image = Image.open('Home_DSr.jpg')
#st.image(image,width=620)

st.markdown('<div style="text-align: center;font-size: 40px"><b>Aline Gomes</b></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;font-size: 23px"><b>Portfólio Profissional – Ciência de Dados & Inteligência Artificial</b></div>', unsafe_allow_html=True)


st.text("")


col1, col2, col3  = st.columns(3)

with col1:
    image = Image.open('Badge_CISCO1.png')
    st.image(image,width=160)

with col2:
    image = Image.open('Badge_CISCO2.png')
    st.image(image,width=160)
    
with col3:
    image = Image.open('Badge_IBM.png')
    st.image(image,width=140)


col4, col5, col6 = st.columns(3)


with col4:
    image = Image.open('Badge_DSCP.png')
    st.image(image,width=160)
    
with col5:
    image = Image.open('Badge_MICROSOFT1.png')
    st.image(image,width=140)

with col6:
    image = Image.open('Badge_MICROSOFT.png')
    st.image(image,width=140)




