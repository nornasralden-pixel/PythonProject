import time
import unittest

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from unicodedata import category

from kerem_qa.selenium_example.seleniumBaseDalya import seleniumBaseDalya

class pytest_advance_demo(unittest.TestCase):

    def setUp(self):
        self.base = seleniumBaseDalya()
        self.driver = self.base.selenium_start_with_url("https://advantageonlineshopping.com/#/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_dropdown_example(self):
        print("test for dropdown example")
        time.sleep(3)
        contact_us = self.driver.find_element(By.PARTIAL_LINK_TEXT, "CONTACT")
        contact_us.click()

        category = self.driver.find_element(By.NAME, "categoryListboxContactUs")
        category_as_dropdown = Select(category)
        category_as_dropdown.select_by_index(2)
        category_as_dropdown.select_by_visible_text("Mice")
        print("into text")

        time.sleep(3)
        product = self.driver.find_element(By.NAME, "productListboxContactUs")
        product_as_dropdown = Select(product)
        product_as_dropdown.select_by_index(2)
        print("into product")

        email_selection = self.driver.find_element(By.NAME, "emailContactUs")
        email_selection.click()
        email_selection.send_keys("nnnnn@email.com")
        print("into email")

        time.sleep(3)
        subject = self.driver.find_element(By.NAME, "subjectTextareaContactUs")
        subject.click()
        subject.send_keys("the mice HP Z3200 Wireless Mouse")
        print("into subject")

        send = self.driver.find_element(By.ID, "send_btn")
        is_displayed = send.is_displayed()
        assert is_displayed == True , "Send button did not displayed as expected"

