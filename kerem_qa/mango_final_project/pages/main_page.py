from selenium.webdriver.common.by import By

class main_page():

    def __init__(self, driver):
        self.driver = driver

    def cookies_message(self):
        cookies_message = self.driver.find_element(By.ID,"cookies.button.acceptAll")
        cookies_message.click()
        cookies_message2 = self.driver.find_element(By.ID,"changeCountryAccept")
        cookies_message2.click()

    def click_on_search_button(self):
        search_button = self.driver.find_element(By.CLASS_NAME,"ButtonInspirational_text__EQKli")
        search_button.click()
        return search_button

    def click_on_kids_section(self):
        categories = self.driver.find_elements(By.CLASS_NAME,"LineAnimatedBase_text__g03Hw")
        kids_category = categories[3]
        kids_category.click()

    def cheking_for_the_five_buttons(self):
        five_buttons_text = []
        five_buttons = self.driver.find_elements(By.ID, "wrapperMenu")
        for button in five_buttons:
            five_buttons_text.append(button.text)
        print(five_buttons_text)
