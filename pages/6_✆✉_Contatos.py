import iluminado as rua
from PIL import Image
import iluminado.fluxo.componentes.v1 as componentes

rua.definir_configuração_da_página(
    título_da_página="Contatos",
    ícone_de_página="☎️",
)

rua.escrever("## Como me encontrar:\n")

# Badge LinkedIn
componentes.HTML("""
  <!-- LinkedIn Profile Badge -->
  <script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
  <div class="badge-base LI-profile-badge"
       data-locale="pt_BR"
       data-size="medium"
       data-theme="light"
       data-type="VERTICAL"
       data-vanity="aline-gomes-oli1509"
       data-version="v1">
    <a class="badge-base__link LI-simple-link"
       href="www.linkedin.com/in/aline-gomes-oli1509">
       Aline Gomes no LinkedIn
    </a>
  </div>
""", height=300)

rua.escrever("✉️: alinegomes1509@gmail.com\n\n")
rua.escrever("GitHub: https://github.com/AlineGomesOliveira")


