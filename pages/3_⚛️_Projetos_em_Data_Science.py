import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(
    page_title="Projetos em Data Science",
    page_icon="⚛️",
)

st.markdown("# Projetos em Data Science")

st.markdown("Aqui estão alguns dos projetos de Data Science que desenvolvi ao longo da minha carreira.")


with st.container():

    st.markdown("----------------")
    
    col13, col14 = st.columns(2)

    with col13:
        st.markdown("**1. Projeto com Feedback:**" )
        st.markdown("### Projeto de Previsão de Notas de Filmes com Machine Learning")

    with col14:

        image = Image.open('ProjetoDSCS.jpg')
        st.image(image,width=350)
    
    col15 = st.columns(1)

    st.markdown("**Resumo:** " )
    st.markdown("> 📌 Neste projeto existiram 2 objetivos principais:")
    st.markdown("> O 1º objetivo foi aplicar conceitos de Ciência de Dados para analisar um dataset com avaliações de filmes feitas por usuários (MovieLens dataset), investigando padrões de nota com relação a gênero, ano de lançamento e número de avaliações.")
    st.markdown("> O 2º objetivo foi construir um modelo de Machine Learning para prever a nota que um usuário daria a um determinado filme. Foram testados os modelos de Regressão Linear, Random Forest e XGBoost.")
    st.markdown("> 📈 As métricas usadas para avaliação dos modelos foram RMSE e MAE.") 
    st.markdown("> 🎯 O objetivo foi alcançar um RMSE abaixo de 0.9, mostrando que o modelo consegue capturar razoavelmente bem as preferências dos usuários.")
    st.markdown("**✅ Acesse o fonte do projeto aqui:🔗 https://github.com/AlineGomesOliveira/Projeto_Previsao_Notas_Filmes")

with st.container():

    st.markdown("----------------")
    
    col10, col11 = st.columns(2)

    with col10:
        st.markdown("**2. Projeto com Feedback:**" )
        st.markdown("### Análise de Dados sobre Acidentes de Trânsito no Brasil com SparkSQL e Dashboards.")

    with col11:

        image = Image.open('Projeto02.png')
        st.image(image,width=350)
    
    col12 = st.columns(1)
    
    st.markdown("**Arquitetura do Projeto:** " )
    
    image = Image.open('arquitetura_projet01.png')
    st.image(image,width=350)   
        
    col13 = st.columns(1)
    
    st.markdown("**✅ Resumo do Projeto:** " )
    st.markdown("> 📌 O objetivo deste projeto foi responder perguntas de negócio sobre a segurança viária no Brasil, utilizando dados públicos de acidentes de trânsito. Através de análise exploratória de dados e visualização interativa, buscamos identificar padrões, comportamentos críticos e insights relevantes para auxiliar na prevenção e redução de acidentes.")
    st.markdown("> Este foi um projeto desafiador pois foi desenvolvido no Linux Ubuntu 22.04, inicializado através de virtualização pelo Oracle VM VirtualBox instalado em uma máquina com Windows 11..")
    st.markdown("> 🛠️ Tecnologias e Ferramentas Utilizadas.")
    st.markdown(">> - Python 3.11 com Anaconda.")
    st.markdown(">> - Pandas e NumPy para análise exploratória.")
    st.markdown(">> - Matplotlib e Seaborn para gráficos estatísticos")
    st.markdown(">> - Plotly para visualização interativa")
    st.markdown(">> - SQLAlchemy + MySQL para gerenciamento relacional dos dados")
    st.markdown(">> - PandaSQL para executar consultas SQL diretamente sobre DataFrames")
    st.markdown(">> - Docker para executar o MySQL em ambiente isolado")
    st.markdown(">> - Jupyter Notebook como ambiente de desenvolvimento")
    
    st.markdown("> O dataset foi carregado através do pacote Pandas, que também foi usado para análise exploratória, em formato de dataframe.") 
    st.markdown("> A biblioteca SQLAlchemy foi utilizada para criar uma tabela no SGBD MySQL, criar o dicionário de dados e popular esta tabela à partir do dataframe do Pandas ")
    st.markdown("> Para extração dos dados do MySQL foi usada a biblioteca PandaSQL e o SQLAlchemy como conector com Python.")
    st.markdown("> Já o MySQL é executado à partir de um container Docker. Ambos, devido à falta de suporte à KVM pelo VirtualBox, foram instalados via command line.")
    st.markdown("> As 10 pergutas de negócio foram respondidas usando querys pelo SparkSQL, que alimentaram gráficos plotados através do pacote Plotly. ")
    st.markdown("O guia para a instalação do Docker está aqui: https://github.com/AlineGomesOliveira/Projeto_Analise_Acidentes_Transito_no_Brail/blob/main/Guia_Instalacao_Docker_Linux.txt")
    st.markdown("E o guia para instalação do container com o MySQL está aqui: https://github.com/AlineGomesOliveira/Projeto_Analise_Acidentes_Transito_no_Brail/blob/main/Guia_Instalacao_MySQL_Docker.txt")

    st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/AlineGomesOliveira/Projeto_Analise_Acidentes_Transito_no_Brasil/blob/main/Projeto_Analise_Acidentes_Transito.ipynb")
  


    st.markdown("----------------")
    
    
