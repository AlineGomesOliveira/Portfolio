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
        st.markdown("### 📊 1. Projeto de Previsão de Notas de Filmes com Machine Learning")

    with col14:

        image = Image.open('ProjetoDSCS.jpg')
        st.image(image,width=250)
    
    col15 = st.columns(1)

    st.markdown("**Resumo:** " )
    st.markdown("> 📌 Neste projeto existiram 2 objetivos principais:")
    st.markdown("> O 1º objetivo foi aplicar conceitos de Ciência de Dados para analisar um dataset com avaliações de filmes feitas por usuários (MovieLens dataset), investigando padrões de nota com relação a gênero, ano de lançamento e número de avaliações.")
    st.markdown("> O 2º objetivo foi construir um modelo de Machine Learning para prever a nota que um usuário daria a um determinado filme. Foram testados os modelos de Regressão Linear, Random Forest e XGBoost.")
    st.markdown("> 0 2º objetivo foi criar modelos de Machine Learning para Prever de Consumo de Combustível. Para esta previsão foi usado um modelo de Regressão(Benchmark), um modelo SVM e um modelo SVM com otimização de parâmetros através da biblioteca Python SciKit-learn.")
    st.markdown("> As métricas usadas foram Coeficiente R2 e RMSE.") 
    st.markdown("> O objetivo foi alcançar um Coeficiente R2 de 70%.")
    st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/EvandroCleto/Projeto_Previsao_Consumo_Combustivel")

with st.container():

    st.markdown("----------------")
    
    col10, col11 = st.columns(2)

    with col10:
        st.markdown("**3. Projeto com Feedback:**" )
        st.markdown("### Análise de Risco no Transporte Público.")

    with col11:

        image = Image.open('Projeto03.png')
        st.image(image,width=350)
    
    col12 = st.columns(1)
    
    st.markdown("**Arquitetura do Projeto:** " )
    
    image = Image.open('Infra_Projeto.png')
    st.image(image,width=650)   
        
    col13 = st.columns(1)
    
    st.markdown("**Resumo:** " )
    st.markdown("> Objetivo deste projeto foi responder 10 perguntas de negócios sobre transporte publico em Londres através de análise de dados usando os pacotes SparkSQL, PandaSQL, SQLAlchemy, MySql e Docker.")
    st.markdown("> Este foi um projeto desafiador pois foi desenvolvido no Linux Ubuntu 22.04, inicializado através de virtualização pelo Oracle VM VirtualBox que foi instalado em uma máquina com Windows 11.")
    st.markdown("> O projeto teve início baixando um dataset do Microsoft Excel do link https://data.world/makeovermonday/2018w51, no Linux Ubuntu, onde foi instalado o Anaconda Python.")
    st.markdown("> O dataset foi carregado através do pacote Pandas, que também foi usado para análise exploratória, em formato de dataframe.") 
    st.markdown("> A biblioteca SQLAlchemy foi utilizada para criar uma tabela no SGBD MySQL, criar o dicionário de dados e popular esta tabela à partir do dataframe do Pandas ")
    st.markdown("> Para extração dos dados do MySQL foi usada a biblioteca PandaSQL e o SQLAlchemy como conector com Python.")
    st.markdown("> Já o MySQL é executado à partir de um container Docker. Ambos, devido à falta de suporte à KVM pelo VirtualBox, foram instalados via command line.")
    st.markdown("> As 10 pergutas de negócio foram respondidas usando querys pelo SparkSQL, que alimentaram gráficos plotados através do pacote Plotly. ")
    st.markdown("O guia para a instalação do Docker está aqui: https://github.com/EvandroCleto/Projeto03_V3_Analise_Risco_Transporte/blob/main/Guia_Instalacao_Docker_Linux.txt")
    st.markdown("E o guia para instalação do container com o MySQL está aqui: https://github.com/EvandroCleto/Projeto03_V3_Analise_Risco_Transporte/blob/main/Guia_Instalacao_MySQL_Docker.txt")

    st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/EvandroCleto/Projeto03_V3_Analise_Risco_Transporte/blob/main/Projeto03_V3_Risco_Transp.ipynb")
  
with st.container():

    st.markdown("----------------") 
    col4, col5 = st.columns(2)

    with col4:
        st.markdown("**2. Projeto com Feedback:**" )
        st.markdown("### Machine Learning na Segurança do Trabalho Prevendo a Eficiência de Extintores de Incêndio.")

    with col5:

        image = Image.open('Projeto02r.png')
        st.image(image,width=350)
    
    col6 = st.columns(1)
    
    st.markdown("**Resumo:** " )
    st.markdown("> Criação de projeto de Machine Learning para segurança do trabalho “Prevendo a Eficiênciade Extintores de Incêndio” e com o objetivo da Classificação preditiva atingir 85% de acurácia.") 
    st.markdown("> O projeto foi realizado de forma independente por 4 semanas para carregar, analisar, limpar, pré-processar, realizar a análises estatísticas e criar e avaliar os modelos de Machine Learning, utilizando linguagem R e seus pacotes readxl (para importar a fonte dedados em Excel), car (para geração de qqPlots), e1071 (para analisar Assimetria e Curtose), caTools (para divisão em de dados em treino e teste), pROC (para visualizar, suavizar e comparar as características de curvas ROC) e multiROC (para calcular métricas deSpecificity, Sensitivity e AUC).")
    st.markdown("> Os algorítimos de Machine Learning utilizados neste projeto para criação dos modelos de Classificação foram: Regressão Logistica (Benchmark), KNN (2 versões), Naive Bayes (2 versões) e SVM (2 versões). Na avaliação dos modelos verificou-se que o modelo KNN V1 teve a maior acurácia (0.9312) e o maior AUC (0.9311), sendo este o escolhido para deploy pois obteve melhor desempenho em 2 das 3 métricas analisadas.")
    st.markdown("O Dataset utilizado no projeto foi obtido em: https://www.muratkoklu.com/datasets/vtdhnd07.php")
    st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/EvandroCleto/Projeto02_V2_Eficiencia_Extintores_Incendio/blob/main/Projeto02V3_0-Eficiencia_Extintores_Incendio.R")

with st.container():

    st.markdown("----------------")    
    
    col1, col2 = st.columns(2)

    with col1:
        
        st.markdown("**1. Projeto com Feedback:**" )
        st.markdown("### Machine Learning em Logística - Prevendo o Consumo de Energia de Carros Elétricos.")   


    with col2:
       
        image = Image.open('Projeto01R.png')
        st.image(image,width=350)

    
    col3 = st.columns(1)
    
    st.markdown("**Resumo:** ")
    st.markdown("> Realizado desenvolvimento do projeto de previsão de Consumo de Energia de Carros Elétricos, utilizando diversos modelos de veículos e com o objetivo de atingir uma precisãode 80% pelo modelo de Regressão.")
    st.markdown("> Na modelagem preditiva de Regressão, foram utilizados os algoritmos RegressãoLinear (Benchmark), Radom Forest e SVM (2 versões).")
    st.markdown("> O Radom Forest também foi utilizado para Feature Selection.")
    st.markdown("> Foram construídas 4 versões de modelos preditivos usando diferentes abordagens.")
    st.markdown("> Na avaliação, o modelo que apresentou melhor performace foi o modelo de Benchmark (usando Regressão Linear) com Rsquared = 0.7945 e Residual standard error = 0.1173 que praticamente atingiu métrica definida no início do projeto(80%).")
    st.markdown("O Dataset utilizado no projeto foi obtido em: https://data.mendeley.com/datasets/tb9yrptydn/2")
    st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/EvandroCleto/Machine-Learning-em-Logistica-Prevendo-o-Consumo-de-Energia-de-Carros-Eletricos/blob/main/Projeto01V3_0-Consumo_Carros_Eletricos.R")
    
with st.container():

    st.markdown("----------------")
    
    col7, col8 = st.columns(2)

    with col7:
        st.markdown("**0. Projeto com Feedback:**" )
        st.markdown("### Detecção de Fraudes no Tráfego de Cliques em Propagandas de Aplicações Mobile.")

    with col8:

        image = Image.open('Projeto00.jpg')
        st.image(image,width=350)
    
    col9 = st.columns(1)
    
    st.markdown("**Resumo:** " )
    st.markdown("> Este é um projeto de Prevenção de Fraude e seu objetivo foi construir um modelo de aprendizado (classificação) de máquina para determinar se um clique em um site é fraudulento ou não.")
    st.markdown("> Ele foi meu primeiro projeto independente em Ciência de Dados, onde me dediquei durante 1 mês para concluí-lo, utilizando meu tempo livre.")
    st.markdown("> O projeto foi construído em Linguagem R para importar, extrair, limpar, analisar e visualizar os dados.") 
    st.markdown("> Na análise dos dados, foi verificado que as classes da variável Target estavam desbalanceadas e foi necessário aplicar técnica de oversampling (ROSE) para seu balanceamento.")
    st.markdown("> Já para criação dos modelos de Machine Learning foram usados os algorítimos C5.0, SVM e KNN.")
    st.markdown("> Na avaliação das Confusions Matrix, foi verificado que os modelos C5.0 e SVM apresentaram performance semelhantes (acurácia de 0.8396 e 0.8408 respecitvamente) e ambos podem ser utilizados para previsões de possíveis fraudes com boa performance.")

    st.markdown("O Dataset utilizado no projeto foi obtido em: https://www.kaggle.com/c/talkingdata-adtracking-fraud-detection/data")
    st.markdown("**Acesse o fonte do projeto aqui:** https://github.com/EvandroCleto/Projeto01_Deteccao_Fraudes_Trafego_Cliques/blob/main/Projeto01_Detec%C3%A7%C3%A3o_Fraudes_Trafego_Cliques.R")
  
    st.markdown("----------------")
