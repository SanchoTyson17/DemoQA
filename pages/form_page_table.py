from pages.base_page import BasePage
from locators.form_page_table_locators import FormPageTableLocators


class FormPageTable(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self, url):
        self.browser.get(url)

    def click_practice_form(self):
        self.wait_and_click(FormPageTableLocators.practice_form_button)