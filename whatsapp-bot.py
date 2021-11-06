# Importações do python:
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Navegar até o zap web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

# Definir tudo foda pra krl aeee
contatos = ['grupo1', 'Mandioca cozida com frango', 'Testes' ]
mensagem = 'To testando um bot de zap no py pode ignorar essa msg aqui :)'

# em busca dos contato automatico:
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)
    

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)

# campo de pesquisa 'copyable-text selectable-text'
# campo de msg privada'copyable-text selectable-text'
# enviar msg para os contatins:

