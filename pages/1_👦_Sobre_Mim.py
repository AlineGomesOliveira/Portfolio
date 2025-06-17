import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(
    page_title="Sobre Mim",
    page_icon="👦",
)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div style="font-size: 14px">Olá! Eu sou Aline Gomes!!</div>', unsafe_allow_html=True)
    
    st.markdown('<div style="font-size: 14px">Sou estudante de Ciência de Dados, formada em Análise e Desenvolvimento de Sistemas e certificada como Data Science and Artificial Intelligence Certified Specialist pela Data Science Academy.</div>', unsafe_allow_html=True)

    st.markdown('<div style="font-size: 14px">Tenho uma trajetória de mais de três anos na área tecnológica, com foco crescente na aplicação de Inteligência Artificial, Ciência de Dados e Machine Learning para solucionar desafios e explorar o potencial dos dados na tomada de decisões estratégicas.</div>', unsafe_allow_html=True)

    st.markdown('<div style="font-size: 14px">Sou apaixonada por tecnologia, arte e aprendizado contínuo. Desenvolvi projetos de pesquisa voltados ao aprendizado de IA, onde aprimorei minhas habilidades em análise e interpretação de dados. Atualmente, estou imersa em estudos e aplicações práticas com tecnologias de ponta, como Transformers, LLMs, LangChain, Vector Databases e a plataforma Hugging Face, que representam o estado da arte em IA Generativa.</div>', unsafe_allow_html=True)

    st.markdown('<div style="font-size: 14px">Além disso, me dedico ao desenvolvimento de soluções e plataformas que otimizam a coleta, o processamento e a visualização de dados, utilizando ferramentas como Excel, Power BI, Tableau, além das linguagens de programação Python e R.</div>', unsafe_allow_html=True)

    st.markdown('<div style="font-size: 14px">Fora do universo dos dados, também me aventuro na música como violinista e no desenho artístico, com foco no estilo realista — áreas que traduzem meu olhar criativo e atento aos detalhes.</div>', unsafe_allow_html=True)

    st.markdown('<div style="font-size: 14px">📌 Conheça mais sobre minha trajetória e projetos no meu LinkedIn:</div>', unsafe_allow_html=True)
    st.write('LinkedIn: https://www.linkedin.com/in/evandro-cleto/?locale=pt_BR')
    
    st.markdown('<div style="font-size: 14px">É um prazer ter você por aqui!</div>', unsafe_allow_html=True)
    st.text("")
    #st.markdown('<div style="font-size: 14px">Ah, se você estiver com pressa, o meu currículo está aqui:</div>', unsafe_allow_html=True)
    #st.text("")
    #pdfFileObj = open("/mount/src/portifolio/Curriculo_DS_PT_V1.pdf", 'rb')
    #pdfFileObj = open("Curriculo_DS_PT_V1.pdf", 'rb')
    #st.download_button('Baixe meu CV:',pdfFileObj,file_name='Curriculo_Evandro_Cleto.pdf',mime='pdf')

with col2:
    image = Image.open('Main_Photor.jpg')
    st.image(image,width=280,caption='2022 EMADT Violin Graduation')


with col2:
    image = Image.open('Main_Photor2.jpg')
    st.image(image,width=280,caption='2022 EMADT - 1st Place in the classl')

    
