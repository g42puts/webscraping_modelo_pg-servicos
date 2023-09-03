from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


# link do site do google
google_url = "https://www.google.com/"

# opções para o nevagador
options = Options()
#options.add_argument('--headless'), # interface gráfica, exibição do navegador
options.add_argument('--no-sandbox'), # reduz consumo de recursos
options.add_argument('--disable-geolocation'), # geolocalização
options.add_argument('--disable-dev-shm-usage'), # compartilhamento de memoria temporaria
options.add_argument('--disable-notifications'), # notificações 
options.add_argument('--disable-popup-blocking'), # pop-ups
options.add_argument('--disable-gpu') # aceleração de hardware

# defino a variavel driver, meu navegador
driver = webdriver.Firefox()

# navega até o site google.com.br
driver.get(google_url)

# pega o conteúdo do html da página referem a div e classe passada e o img
google_logo_xpath = '//div[@class="k1zIA rSk4se"]//img'
google_logo = driver.find_element(By.XPATH, google_logo_xpath)

# Obtenha o valor do atributo 'src' da logo
logo_link = google_logo.get_attribute("src")

# printar o link da logo
print("Link da logo do google", logo_link)

# fecha o selenium
driver.quit()