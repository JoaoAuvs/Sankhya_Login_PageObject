import logging
import os
import time

from BasePage import *
from Locators import *


class Login(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.url = "http://sankhya.kothe.com.br:8080/mge"
        self.username = os.environ.get("USER_NAME_SANKHYA")
        self.password = os.environ.get("SENHA_SANKHYA")

    def fazer_login(self) -> None:
        logging.info("Iniciando a funcao -> FAZER LOGIN <-")
        try:
            self.navegar(self.url)
            time.sleep(3)
            self.escrever(Locators.ID_LOGIN, self.username)
            self.escrever(Locators.ID_SENHA, self.password)
            self.click(Locators.BTN_ENTRAR)
            time.sleep(10)
            self.aguardar_elemento_desaparecer(Locators.BTN_ENTRAR)
        except Exception as e:
            raise (logging.warning("Erro na funcao -> FAZER LOGIN <- " + str(e)))
