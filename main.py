from Driver import *
from Log import *
from Login import *


def main():
    try:
        driver = Driver().get_driver()
        Login(driver).fazer_login()
    except Exception as e:
        print("Erro ao executar o programa: " + str(e))    

if __name__ == "__main__":
    log = Log()
    main()
