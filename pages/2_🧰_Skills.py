import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Skills",
    page_icon="🧰",
)

st.markdown("## Estes são os skills em Data Science que domino:")

col1, col2 = st.columns(2)

with col1:
    
   st.slider("SQL",0,100, 50)

with col2:
    r = st.slider('Python', 0, 100, 90)
    
    
col3, col4 = st.columns(2)

with col3:
    ml = st.slider('Machine Learning', 0, 100, 60)

with col4:
    prompt = st.slider('Prompt Engineering', 0, 100, 40)

col5, col6 = st.columns(2)

with col5:
    llm = st.slider('LLM', 0, 100, 40)
    
with col6:
    rl = st.slider('Linguagem R', 0, 100, 80)
    
col7, col8 = st.columns(2)

with col7:
   docker = st.slider('Docker', 0, 100, 75)

with col8:
    git = st.slider('Git/GitHub', 0, 100, 90)

col9, col10 = st.columns(2)

with col9:
    gcp = st.slider('GCP (VertexIA | Big Query)', 0, 100, 70)    
    
with col10:
    aml = st.slider('Azure Machine Learning', 0, 100, 50)
    
col11, col12 = st.columns(2) 

with col11:
    linux = st.slider('Linux', 0, 100, 80)

with col12:
    powerbi = st.slider('Power BI', 0, 100, 95)

col13, col14 = st.columns(2) 

with col13:
    Excel = st.slider('Microsoft Excel', 0, 100, 100)

with col14:
    vm = st.slider('Oracle VM', 0, 100, 75)

col15, col16 = st.columns(2) 

with col15:
    pnl = st.slider('PNL', 0, 100, 45)

with col16:
    scrum = st.slider('Scrum', 0, 100, 75)
    




