import time
import unittest
from selenium.webdriver.common.by import By
from kerem_qa.mango_final_project.globals import BACE_URL, ITEM_NAME, WORNG_PROUDCT_NAME, SHOE_NAME
from kerem_qa.mango_final_project.pages.kids_page import kids_page
from kerem_qa.mango_final_project.pages.main_page import main_page
from kerem_qa.mango_final_project.pages.search_page import SearchPage
from kerem_qa.mango_final_project.pages.shoe_page import ShoePage
from kerem_qa.mango_final_project.tests.selenuim_base_mango import selenium_base_mango

class mangoMainTests(unittest.TestCase):

    def setUp(self):
        self.base = selenium_base_mango()
        self.driver = self.base.selenium_start_with_url(BACE_URL)
        self.main_page =main_page (self.driver)
        self.SearchPage = SearchPage(self.driver)
        self.main_page.cookies_message()
        self.kids_page = kids_page(self.driver)
        self.shoe_page = ShoePage(self.driver)

    def tearDown(self):
        self.base.selenium_stop()

    def test_search(self):
         self.main_page.click_on_search_button()
         time.sleep(1)
         self.SearchPage.write_product_in_search_filed(ITEM_NAME)
         self.SearchPage.show_the_product_numbers_that_showed()
         time.sleep(2)
         url = self.driver.current_url
         assert url == "https://shop.mango.com/us/en/search/women?q=shirt"

    def test_find_message(self):
        self.main_page.click_on_search_button()
        time.sleep(1)
        self.SearchPage.write_worng_product_in_search_filed(WORNG_PROUDCT_NAME)
        url = self.driver.current_url
        assert url == "https://shop.mango.com/us/en/search/women?q=hbcheqcnjnc"

    def test_find_girls_clothes(self):
        self.main_page.click_on_kids_section()
        self.kids_page.pick_girls_filed_and_item_price()
        time.sleep(2)
        url = self.driver.current_url
        assert url == "https://shop.mango.com/us/en/c/kids/girls/sale-50-off_0a0619fb"

    def test_looking_for_five_buttons(self):
        buttons = self.main_page.cheking_for_the_five_buttons()
        assert buttons == 5 , "these are not the five buttons"

    def test_shoes_number(self):
        self.main_page.click_on_search_button()
        time.sleep(1)
        self.SearchPage.write_product_in_search_filed(SHOE_NAME)
        time.sleep(1)
        self.SearchPage.click_on_shoe()
        shoes_text = self.shoe_page.shoe_measure()
        assert shoes_text == "SATIN COURT SHOES" , "shoes text should be SATIN COURT SHOES"
