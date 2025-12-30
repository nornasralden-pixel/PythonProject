from selenium.webdriver.common.by import By


class MainPageLocators(object):
    SEARCH_BUTTON =(By.CLASS_NAME,"ButtonInspirational_text__EQKli")
    KIDS_SECTION = (By.CLASS_NAME,"LineAnimatedBase_text__g03Hw")
    BUTTONS = (By.CLASS_NAME, "BrandEntry_brandLi__545zJ")
    COOKIES_MESSAGE = (By.ID,"cookies.button.acceptAll")
    COOKIES_MESSAGE2 = (By.ID,"changeCountryAccept")

class ShoesPageLocators(object):
    SHOES_MEASURE = (By.CLASS_NAME, "SizeItemContent_sizeInfo__bgdpC")
    SHOES_TEXT = (By.CLASS_NAME, "ProductDetail_title__Go9C2.textHeadingL_className__KQ29Z")

class KidsPageLocators(object):
    GIRLS_SECTION = (By.PARTIAL_LINK_TEXT,"GIRLS")

class SearchPageLocators(object):
    PRODUCT_NAME = (By.NAME,"search")
    PRODUCT_NUMBER = (By.CLASS_NAME,"Slideshow_slide__ACcLa")
    WORNG_PRODUCT_NAME = (By.NAME,"search")
    SHOE_CLICK = (By.CLASS_NAME,"Slideshow_slide__ACcLa")