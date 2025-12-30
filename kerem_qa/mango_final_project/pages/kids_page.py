import time
from selenium.webdriver.common.by import By

from kerem_qa.mango_final_project.locators import KidsPageLocators


class kids_page:

    def __init__(self, driver):
        self.driver = driver


    def pick_girls_filed_and_item_price(self):
        girls_section= self.driver.find_element(*KidsPageLocators.GIRLS_SECTION)
        girls_section.click()
        time.sleep(2)
        price_item = self.driver.find_elements(By.CLASS_NAME,"SinglePrice_center__SWK1D.textBodyM_className__v9jW9.SinglePrice_finalPrice__hZjhM")
        for i in range(0,7):
            print(price_item[i].text)




