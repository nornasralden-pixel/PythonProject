from selenium.webdriver.common.by import By


class ShoePage():

    def __init__(self, driver):
        self.driver = driver

    def shoe_measure(self):
        min_measure = 0
        max_measure = 0
        measures = self.driver.find_elements(By.CLASS_NAME,"SizesList_listItem__UsAJg")
        for measure in measures:
            if min_measure == 5:
                print(min_measure)
            if max_measure == 10:
                print(max_measure)
