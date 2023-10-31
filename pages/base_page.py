from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def _element_is_located(self, locator: tuple):
        return Wait(self.browser, 20).until(EC.element_to_be_clickable(locator))
    def _element_is_clickabe(self, locator: tuple):
        return Wait(self.browser, 10).until(EC.element_to_be_clickable(locator))


    def wait_and_fill_in(self, locator: tuple, text: str):
        self._element_is_located(locator)
        self.browser.find_element(*locator).send_keys(text)

    def wait_and_click(self, locator: tuple):
        self._element_is_clickabe(locator)
        self.browser.find_element(*locator).click()

    def get_text(self, locator: tuple):
        return self.browser.find_element(*locator).text






