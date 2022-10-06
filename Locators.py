from selenium.webdriver.common.by import By


class Locators():

    # --- LOGIN ---
    ID_LOGIN = (By.ID, "login")
    ID_SENHA = (By.ID, "password")
    BTN_ENTRAR = (By.CLASS_NAME, "btn-login")
    ALERTA = (By.XPATH, "/html/body/div[6]")
