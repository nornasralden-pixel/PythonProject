from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from kerem_qa.mango_final_project.locators import SearchPageLocators


class SearchPage():
    def __init__(self, driver):
        self.driver = driver

    def write_product_in_search_filed(self,item_name):
        click_search = self.driver.find_element(*SearchPageLocators.PRODUCT_NAME)
        click_search.click()
        click_search.send_keys(item_name)
        click_search.send_keys(Keys.ENTER)

    def show_the_product_numbers_that_showed(self):
        number_of_shirts = self.driver.find_elements(*SearchPageLocators.PRODUCT_NUMBER)
        number_of_shirts = len(number_of_shirts)
        if number_of_shirts > 0:
            print(number_of_shirts)

    def write_worng_product_in_search_filed(self,worng_product_name):
        click_search = self.driver.find_element(*SearchPageLocators.WORNG_PRODUCT_NAME)
        click_search.click()
        click_search.send_keys(worng_product_name)
        click_search.send_keys(Keys.ENTER)
        message = self.driver.find_element(By.CLASS_NAME,"NoResults_noResultContent__x4HqL")
        print(message.text)

    def click_on_shoe(self):
        shoe = self.driver.find_elements(*SearchPageLocators.SHOE_CLICK)
        shoe[0].click()