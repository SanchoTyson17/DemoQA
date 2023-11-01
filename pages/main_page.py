from pages.base_page import BasePage
from locators.main_page_locators import MainPageTableLocators


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self, url):
        self.browser.get(url)

    def click_practice_form1(self):
        self.wait_and_click(MainPageTableLocators.practice_form_main)