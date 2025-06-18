import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Contatos",
    page_icon="✆✉",
)

# Título com emoji
st.markdown("## 📇 Como me encontrar:")

# Badge do LinkedIn incorporado
components.html("""
<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
<div class="badge-base LI-profile-badge" 
     data-locale="en_US" 
     data-size="medium" 
     data-theme="light" 
     data-type="VERTICAL" 
     data-vanity="aline-gomes-563408169" 
     data-version="v1">
  <a class="badge-base__link LI-simple-link" href="https://www.linkedin.com/in/aline-gomes-563408169/?trk=profile-badge">
  </a>
</div>
""", height=250)

# Linha divisória elegante
st.markdown("---")

# Contatos com ícones e links clicáveis
st.markdown("📧 **Email:** [linegomes1509@gmail.com](mailto:linegomes1509@gmail.com)")
st.markdown("🌐   **LinkedIn:** [linkedin.com/in/aline-gomes-563408169](https://www.linkedin.com/in/aline-gomes-563408169/?locale=pt_BR)")
st.markdown("</>  **GitHub:** [github.com/AlineGomesOliveira](https://github.com/AlineGomesOliveira)")

# Linha final
st.markdown("---")



