import logging
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from Locators import *


class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    # NAVEGAR
    def navegar(self, url) -> str:
        try:
            self.driver.get(url)  
        except Exception as e:
            raise ("Não foi possível acessar a URL: {} Erro: ".format(url) + e)
            
    # CLIQUE
    def click(self, by_locator) -> None:
        try:
            web_element = self.wait.until(EC.visibility_of_element_located(by_locator))
            if web_element.is_displayed():
                web_element.click()
            else:
                raise Exception("Elemento não encontrado")
        except Exception as e:
            raise ("Não foi possível encontrar o elemento: {} Erro: ".format(by_locator) + e)

    # DUPLO CLIQUE
    def duplo_click(self, by_locator) -> None:
        try:
            web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            if web_element.is_displayed():
                ActionChains(self.driver).double_click(web_element).perform()
            else:
                raise Exception("Elemento não encontrado")
        except Exception as e:
            raise ("Não foi possível encontrar o elemento: {} Erro: ".format(by_locator) + e)

    # CLICAR EM UM ELEMENTO DA TABELA
    def click_elemento_tabela(self, by_locator, text) -> None:
        try:
            web_element = self.wait.until(EC.visibility_of_element_located(by_locator))
            rows = web_element.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                if row.text == text:
                    row.click()
                    break
        except Exception as e:
            raise ("Não foi possível encontrar o elemento: {} Erro: ".format(by_locator) + e)

    # CLICAR EM UM ELEMENTO QUE CONTEM O TEXTO
    def click_texto(self, by_locator, text) -> None:
        try:
            web_element = self.wait.until(EC.visibility_of_element_located(by_locator))
            if web_element.is_displayed():
                if text in web_element.text:
                    web_element.click()
                else:
                    raise Exception("Elemento não encontrado")
            else:
                raise Exception("Elemento não encontrado")
        except Exception as e:
            raise ("Não foi possível encontrar o elemento: {} Erro: ".format(by_locator) + e)
    
    # ESCREVER
    def escrever(self, by_locator, text) -> None:
        try:
            web_element = self.wait.until(EC.visibility_of_element_located(by_locator))
            if web_element.is_displayed():
                web_element.send_keys(text)
            else:
                raise Exception("Elemento não encontrado")
        except Exception as e:
            raise ("Não foi possível encontrar o elemento: {} Erro: ".format(by_locator) + e)
    
    # ESCREVER E ENTER
    def escrever_enter(self, by_locator, text) -> None:
        try:
            web_element = self.wait.until(EC.visibility_of_element_located(by_locator))
            if web_element.is_displayed():
                web_element.clear()
                web_element.send_keys(text, Keys.ENTER)
            else:
                raise Exception("Elemento não encontrado")
        except Exception as e:
            raise ("Não foi possível encontrar o elemento: {} Erro: ".format(by_locator) + e)

    # FUNÇÃO PARA ACESSAR UM IFRAME
    def acessar_iframe(self, by_locator) -> None:
        try:
            iframe = self.wait.until(EC.visibility_of_element_located((by_locator)))
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            raise (logging.warning("Erro ao acessar iframe: " + str(e)))

    # FUNÇÃO PARA SAIR DE UM IFRAME
    def close_iframe(self) -> None:
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            raise ("Não foi possível sair do iframe: " + e)

    # OBTER O TEXTO DE UM ELEMENTO
    def obter_text(self, by_locator) -> str:
        try:
            web_element = self.wait.until(EC.visibility_of_element_located(by_locator))
            if web_element.is_displayed():
                return web_element.text
            else:
                raise Exception("Elemento não encontrado")
        except Exception as e:
            raise ("Não foi possível encontrar o elemento: {} Erro: ".format(by_locator) + e)

    # OBTER O VALOR DE UM ELEMENTO UTILIZANDO O ATRIBUTO VALUE
    def obter_valueJS(self, query) -> str:
        try:
            text = self.driver.execute_script("return document.querySelector('"+ query + "').value")
            return text
        except Exception as e:
            raise ("Não foi possível encontrar o elemento: {} Erro: ".format(query) + e)

    # VALIDAR SE O ELEMENTO CONTÉM O TEXTO ESPERADO
    def assert_element_text(self, by_locator, element_text) -> None:
        web_element = self.wait.until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # SE EXISTE ELEMENTO
    def is_enabled(self, by_locator) -> bool:
        return bool(self.wait.until(EC.visibility_of_element_located(by_locator)))

    # AGUARDAR ELEMENTO DESAPARECER
    def aguardar_elemento_desaparecer(self, by_locator) -> None:
        try:
            self.wait.until(EC.invisibility_of_element_located(by_locator))
        except Exception as e:
            raise ("Não foi possível encontrar o elemento: {} Erro: ".format(by_locator) + e)

    # AGUARDAR ELEMENTO ESTAR VISÍVEL
    def aguardar_elemento(self, by_locator) -> str:
        tentativa = 0
        try:
            web_element = self.wait.until(EC.visibility_of_element_located(by_locator))
            while True:
                if web_element.is_displayed():
                    break
                tentativa += 1
                if tentativa > 10:
                    raise Exception('Tempo de espera excedido')
        except Exception as e:
            raise ("Não foi possível encontrar o elemento: {} Erro: ".format(by_locator) + e)

    # AGUARDAR TEXTO ESTAR VISÍVEL
    def aguardar_texto_visivel(self, by_locator, text) -> str:
        try:
            web_element = self.wait.until(EC.visibility_of_element_located(by_locator))
            if web_element.is_displayed():
                if text in web_element.text:
                    return True
                else:
                    raise Exception("Elemento não encontrado")
        except Exception as e:
            raise ("Não foi possível encontrar o elemento: {} Erro: ".format(by_locator) + e) 

    # AGUARDAR ATRIBUTO NÃO ESTAR VAZIO
    def aguardar_elemento_texto(self, by_locator) -> str:
        tentativa = 0
        try:
            web_element = self.wait.until(EC.visibility_of_element_located(by_locator))
            if web_element.is_displayed():
                while web_element.get_attribute('value') != '':
                    time.sleep(1)
                    tentativa += 1
                    if tentativa > 10:
                        raise Exception('Tempo de espera excedido')
                return web_element
        except Exception as e:
            raise ("Não foi possível encontrar o elemento: {} Erro: ".format(by_locator) + e)

    # SE ELEMENTO ESTÁ VISÍVEL
    def is_visible(self,by_locator) -> bool:
        return bool(self.wait.until(EC.visibility_of_element_located(by_locator)))

    # SE ELEMENTO EXISTE RETORNA O TEXTO SE NÃO RETORNA FALSE
    def is_present(self,by_locator) -> bool:
        if self.is_visible(by_locator):
            text = self.wait.until(EC.presence_of_element_located(by_locator).text)
            return text
        else:
            return False
        return bool(self.wait.until(EC.presence_of_element_located(by_locator)))
    
    # CLICAR EM UM ELEMENTO COM MOUSE
    def move_mouse(self, by_locator) -> None:
        try:
            web_element = self.wait.until(EC.visibility_of_element_located(by_locator))
            if web_element.is_displayed():
                ActionChains(self.driver).move_to_element(web_element).perform()
            else:
                raise Exception("Elemento não encontrado")
        except Exception as e:
            raise ("Não foi possível encontrar o elemento: {} Erro: ".format(by_locator) + e)

    # FUNÇÃO PARA VALIDAR SE É DIFERENTE
    def validar_diferente(self, by, elemento, texto) -> None:
        tentativa = 0
        try:
            elemento = self.wait.until(EC.visibility_of_element_located((by, elemento)))
            while tentativa < 20:
                if elemento.text != texto:
                    return True
                else:
                    time.sleep(1)
                    tentativa += 1
            raise (logging.warning("Texto nao é diferente: " + texto))
        except Exception as e:
            raise (logging.warning("Erro ao Aguardar Elemento: " + str(e)))
