from selenium.webdriver.common.by import By

from kerem_qa.mango_final_project.locators import MainPageLocators


class main_page():

    def __init__(self, driver):
        self.driver = driver

    def cookies_message(self):
        cookies_message = self.driver.find_element(*MainPageLocators.COOKIES_MESSAGE)
        cookies_message.click()
        cookies_message2 = self.driver.find_element(*MainPageLocators.COOKIES_MESSAGE2)
        cookies_message2.click()

    def click_on_search_button(self):
        search_button = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        search_button.click()
        return search_button

    def click_on_kids_section(self):
        categories = self.driver.find_elements(*MainPageLocators.KIDS_SECTION)
        kids_category = categories[3]
        kids_category.click()

    def cheking_for_the_five_buttons(self):
        buttons = self.driver.find_elements(*MainPageLocators.BUTTONS)
        buttons_count = len(buttons)
        print(buttons_count)
        return buttons_count

