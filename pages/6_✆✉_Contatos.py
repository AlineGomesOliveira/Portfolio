import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Contatos",
    page_icon="✆✉",
)

st.write('### **Como me encontrar:**')

components.html("""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
<div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="aaline-gomes-563408169" data-version="v1"><a class="badge-base__link LI-simple-link" href="hhttps://www.linkedin.com/in/aline-gomes-563408169/?trk=profile-badge"></a></div>""",height=250)

# Badge LinkedIn
componentes.HTML("""
  <!-- LinkedIn Profile Badge -->
  <script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
  <div class="badge-base LI-profile-badge"
       data-locale="pt_BR"
       data-size="medium"
       data-theme="light"
       data-type="VERTICAL"
       data-vanity="SEU-VANITY"
       data-version="v1">
    <a class="badge-base__link LI-simple-link"
       href="https://www.linkedin.com/in/SEU-VANITY">
       Aline Gomes no LinkedIn
    </a>
  </div>
""", height=300)


st.write('📧:  **linegomes1509@gmail.com**')
#st.write('📱: **+559299502-1056**')
st.write('LinkedIn:  https://www.linkedin.com/in/aline-gomes-563408169/?locale=pt_BR')
st.write('GitHub:  https://github.com/AlineGomesOliveira')
