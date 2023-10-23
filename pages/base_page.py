from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def element_is_visible(self):
        return Wait(self.browser, 10).until(EC.element_to_be_clickable(locator))

