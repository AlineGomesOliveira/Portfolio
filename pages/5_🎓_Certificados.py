import streamlit as st
import streamlit.components.v1 as components
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Certificados",
    page_icon="🎓",
)

# Conteúdo do app continua aqui...


# Texto com alinhamento central e tamanho personalizado
st.markdown("""
<div style="text-align: justify; font-size: 18px;">
    <strong>Com grande orgulho</strong>, apresento os certificados conquistados ao longo da minha trajetória como <strong>Analista e Desenvolvedora de Sistemas</strong>, bem como durante minha formação contínua como <strong>estudante de Ciência de Dados</strong>. Cada certificado representa um passo importante no meu desenvolvimento profissional, refletindo o compromisso com a aprendizagem, a evolução constante e a busca pela excelência na área da tecnologia.
</div>
""", unsafe_allow_html=True)


st.markdown("----------------")   
st.markdown("**Certificado ADA (Certified in Power BI - ADA Community)**")
image1 = Image.open('Cert_Power BI.jpg')
st.image(image1,width=350)

st.markdown("----------------")   
st.markdown("**Certificado CISCO (Defesa de Rede - Network Defense)**")
image1 = Image.open('Cert_Cisco_Defesa_Redes.jpg')
st.image(image1,width=350)

st.markdown("----------------")   
st.markdown("**Certificado CISCO (Network Technician track exam)**")
image1 = Image.open('Cert_Cisco_T_Rede.jpg')
st.image(image1,width=350)

st.markdown("----------------")   

st.markdown("**Formação em Método KANBAN...**")
#image1 = Image.open('Cert_Kanban.png')
#st.image(image1,width=500)

st.markdown("**... que é composta pelos cursos e certificado:**")

col14, col15  = st.columns(2)
width=230
with col14:
    st.markdown(">**1. Training in Personal and Management Development using the KANBAN Method**")
    image1 = Image.open('Cert_Kanban.png')
    st.image(image1,width=width)
with col15:
    st.markdown(">**2. Mapping Processes, Tasks and Workflow, Review and Improvement**")
    image1 = Image.open('Cont_Kanban.png')
    st.image(image1,width=width)

st.markdown("----------------")   
st.markdown("**Fundamentos de Arquitetura de Sistemas.**")
image1 = Image.open('Cert_Dio_Arquitetura_Sistemas.jpg')
st.image(image1,width=350)

st.markdown("----------------")  

st.markdown("**Lean Six Sigma Whiet Belt Certification...**")
#image1 = Image.open('Cert_Kanban.png')
#st.image(image1,width=500)

st.markdown("**... que é composta pelos cursos e certificado:**")

col14, col15  = st.columns(2)
width=230
with col14:
    st.markdown(">**1. Personal and Management Development in Lean Six Sigma Whiet Belt Certification**")
    image1 = Image.open('Cert_White_Belt.png')
    st.image(image1,width=width)
with col15:
    st.markdown(">**2. BLean Six Sigma Methodology. Design and Improvement Tools, DMAIC**")
    image1 = Image.open('Cont_White_Belt.png')
    st.image(image1,width=width)


st.markdown("----------------")   
st.markdown("**Visualização de dados e Design de Dashboards**")
image1 = Image.open('Cert_Design_Dashboard.png')
st.image(image1,width=350)

st.markdown("----------------")   
st.markdown("**Conceitos de Responsividade e Experiência do Usuário**")
image1 = Image.open('Cert_Dio_Responsividade.jpg')
st.image(image1,width=350)

st.markdown("----------------")   
st.markdown("**Lógica de Programação Essencial**")
image1 = Image.open('Cert_Dio_Essencial.jpg')
st.image(image1,width=350)

st.markdown("----------------")   
st.markdown("**Introdução a Criação de Websites com HTML e CSS3**")
image1 = Image.open('Cert_Dio_HTML_CSS3.jpg')
st.image(image1,width=350)

st.markdown("----------------")   
st.markdown("**Introdução a Redes de Computadores**")
image1 = Image.open('Cert_Bradesco_Redes.jpg')
st.image(image1,width=350)


st.markdown("----------------")   
