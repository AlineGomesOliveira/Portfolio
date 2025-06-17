import streamlit as st
from PIL import Image

# Page config
st.set_page_config(
    page_title="Languages",
    page_icon="🌍",
)

# Introductory text
st.markdown("""
### In 2007 I decided to improve my English proficiency and moved to Toronto, Canada, where I stayed until 2008 studying the language and doing some construction work to pay for my stay there.

### Between 2016 and 2018 I returned to live in Canada, this time in Montreal, and took the opportunity to learn French. I also had the opportunity to work at WADA (World Anti Doping Agency) doing administrative services, where I put into practice what I had learned about English and French.

### And speaking of Canada, in none of these times did I ever meet Luisa!!
""")

# Two columns: English and French
col1, col2 = st.columns(2)

with col1:
    image_en = Image.open("Bandeira_do_USA.png")
    st.image(image_en, width=200)
    st.slider("English", 0, 100, 30)

with col2:
    image_fr = Image.open("Bandeira_do_SPAN.png")  # use the name you saved for the second image
    st.image(image_fr, width=200)
    st.slider("French", 0, 100, 70)
