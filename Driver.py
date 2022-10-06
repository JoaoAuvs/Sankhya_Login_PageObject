from subprocess import CREATE_NO_WINDOW

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Driver():
    
    def __init__(self):
        chrome_service = Service(ChromeDriverManager().install())
        chrome_service.creationflags = CREATE_NO_WINDOW
        self.driver = webdriver.Chrome(service=chrome_service, options=options)

    def get_driver(self):
        try:
            self.driver.maximize_window()
            self.driver.switch_to.window(self.driver.window_handles[0])
            return self.driver
        except Exception as e:
            raise(logging.error(e))
    
    def quit_driver(self):
        self.driver.quit()
            
options=Options()
options.add_argument("--window-position=1920,0")
options.add_argument('-ignore-certificate-errors')
options.add_argument('-ignore-ssl-errors')
options.add_argument("--disable-notifications")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument('--disable-infobars')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--force-renderer-accessibility')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--enable-automation')
