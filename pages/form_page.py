from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


first_name = (By.XPATH, "/input[@id='firstName']")
first1 = "First"

class FormPage(BasePage):

    def open(self):
        self.browser.get("https://demoqa.com/automation-practice-form")

    def fill_in_firs_name(self):
        self.element_is_visible(first_name).send_keys(first1)



