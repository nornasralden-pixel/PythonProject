from selenium.webdriver.common.by import By

class ShoePage():

    def __init__(self, driver):
        self.driver = driver

    def shoe_measure(self):
        measures = self.driver.find_elements(By.CLASS_NAME, "SizeItemContent_sizeInfo__bgdpC")
        index_1 = measures[0].text.replace("(", "").replace("'", "").replace(")","")
        index_2 = measures[5].text.replace("(", "").replace("'", "").replace(")","")
        measures_text = index_1, index_2
        print(measures_text)
        if (index_1) > (index_2):
            print(f"{index_1} is greater than {index_2}")
        else:
            print(f"{index_2} is greater than {index_1}")

        shoes_text = self.driver.find_element(By.CLASS_NAME, "ProductDetail_title__Go9C2.textHeadingL_className__KQ29Z").text
        return shoes_text