from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from user_variables import *
from datetime import datetime as dt_datetime
import os
from dotenv import load_dotenv
from time import sleep
import pandas as pd

from func_get_day_name import get_day_name

load_dotenv()
default_time_sleep = 2

# define variavel meses do ano
meses_do_ano = ['','janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

class FirefoxNevagator(Options):
    def __init__(self):
        options = self

        super().__init__(options)


def service_webscrap():

    # configs do user
    USER_ID = os.getenv('USER_ID')
    PASS_ID = os.getenv('PASS_ID')
    
    # pega o mês atual para usar como referencia futuramente
    data_mes_atual = dt_datetime.now().month
    data_mes_seguinte = data_mes_atual + 1

    options = Options()
    
    options.add_argument('--headless'), # interface gráfica, exibição do navegador
    options.add_argument('--no-sandbox'), # reduz consumo de recursos
    options.add_argument('--disable-geolocation'), # geolocalização
    options.add_argument('--disable-dev-shm-usage'), # compartilhamento de memoria temporaria
    options.add_argument('--disable-notifications'), # notificações 
    options.add_argument('--disable-popup-blocking'), # pop-ups
    options.add_argument('--disable-gpu') # aceleração de hardware



    # # configurações do Firefox
    

    # # execução sem interface gráfica
    # options.add_argument('--headless')

    # Inicializar o driver do Firefox
    driver = webdriver.Firefox(options=options)
   
    # vai para a página de login
    driver.get(login_url)

    # pega xpath do campo de username, password e submit button
    sleep(default_time_sleep)
    username = driver.find_element(By.XPATH, username_xpath)
    password = driver.find_element(By.XPATH, password_xpath)
    submit = driver.find_element(By.XPATH, submit_xpath)

    # faz o login, passa o username, password e clica no botão submit
    sleep(default_time_sleep)
    username.send_keys(USER_ID)
    
    sleep(default_time_sleep)
    password.send_keys(PASS_ID)
    
    sleep(default_time_sleep)
    submit.submit()

    # pega xpath do mes atual e do mes seguinte
    mes_seguite_xpath_button = f'//button[p[contains(text(), "{meses_do_ano[data_mes_atual + 1]}")]]'

    # vai para pagina do calendario
    sleep(default_time_sleep * 2)
    driver.get(calendar_url)

    # pega xpath do mes seguinte
    sleep(default_time_sleep)
    button_mes_seguinte = driver.find_element(By.XPATH, mes_seguite_xpath_button)
    
    # pega os valores da página atual através da função get_div_values
    dados_mes_atual = get_div_values(driver, mes=data_mes_atual)

    # passa os dados do mes atual para a função [salvar_em_csv] que irá salvar os dados em formato csv
    salvar_em_csv(dados_mes_atual)

    # vai para a página do próximo mês
    button_mes_seguinte.click()
    
    # pega os valores da página seguinte
    dados_pagina_seguinte = get_div_values(driver, mes=data_mes_seguinte)
    
    # passa os dados do mes atual para a função [salvar_em_csv] que irá salvar os dados em formato csv
    salvar_em_csv(dados_pagina_seguinte)
    
    # encerra o driver
    driver.close()

# essa função retornará demais valores dentro das div que estão dentro do button
def get_div_values(driver:webdriver.Firefox, mes):

    # pega conteudo html dentro dos buttons
    sleep(default_time_sleep)
    buttons = driver.find_elements(By.XPATH, button_xpath)
    
    dados = []
    for button in buttons:
        servicos = []
        try:
            # pega o dia a pertencente a cada campo do calendario por dia
            dia = int(button.find_element(By.TAG_NAME, 'p').text)
            
            # pega valores dentro das divs que estão dentros do button
            div_element = button.find_element(By.XPATH, './div/div')

            # pega todas tags '<p>' que estão dentro das divs
            p_elements = div_element.find_elements(By.TAG_NAME, 'p')
                        
            # passa por cada '<p>' e retorna seu valor textual
            for p_element in p_elements:
                p_text = p_element.text                
                servicos.append(p_text)
        except:
            pass
        
        if not servicos == []:
            
            # retorna nome do dia do mês de cada campo do calendario
            dia_do_mes = get_day_name(day_id=dia, month_id=mes)
            
            # adiciona à lista dados um dict com os valores obtidos
            dados.append(
                {
                    'dia':dia,
                    'mes':meses_do_ano[mes],
                    'ano':dt_datetime.now().year,
                    'dia_do_mes':dia_do_mes,
                    'servico':servicos
                })
        else:
            pass

    return dados

# passa os dados para formato DataFrame (pandas.DataFrame) e salva em formato csv
def salvar_em_csv(dados):
    print(dados)
    if dados == []:
        return
    pd.DataFrame(dados).to_csv(f"{dados[0]['mes']}.csv", index=False)
    
if __name__ == '__main__':
    service_webscrap()