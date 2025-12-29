from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

class selenium_base_mango():

    def selenium_start_with_url(self,url):
        print("*** test started ***")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        return self.driver


    def selenium_stop(self):
        print("***** test stopped *****")
        self.driver.close()