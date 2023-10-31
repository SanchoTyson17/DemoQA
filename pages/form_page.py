from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from locators.form_page_locators import FormPageLocators
from generator.generator import generate_person


class FormPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)


    def open(self, url):
        self.browser.get(url)

    def fill_in_fist_name(self, text: str):
        self.wait_and_fill_in(FormPageLocators.first_name, text)

    def fill_in_last_name(self, text: str):
        self.wait_and_fill_in(FormPageLocators.last_name, text)

    def fill_in_email(self, text: str):
        self.wait_and_fill_in(FormPageLocators.email, text)

    def select_male_radiobutton(self):
        self.wait_and_click(FormPageLocators.gender_checkbox_male)

    def fill_in_number(self, text: str):
        self.wait_and_fill_in(FormPageLocators.number, text)

    def open_birth_date_window(self):
        self.wait_and_click(FormPageLocators.birth_date)

    def show_year_list(self):
        self.wait_and_click(FormPageLocators.display_list_year)

    def select_year(self):
        self.wait_and_click(FormPageLocators.select_year)

    def select_date(self):
        self.wait_and_click(FormPageLocators.select_date)

    def fill_in_subject(self, text: str):
        self.wait_and_fill_in(FormPageLocators.subject, text)

    def select_subject(self):
        self.wait_and_click(FormPageLocators.select_computer_subject)

    def scroll_down(self):
        self.browser.execute_script("window.scrollTo(0, 500)")

    def select_sports_radiobatton(self):
        self.wait_and_click(FormPageLocators.hobbies_checkbox_sports)

    def add_picture(self, path):
        self.wait_and_fill_in(FormPageLocators.picture, path)

    def fill_in_adress(self, text: str):
        self.wait_and_fill_in(FormPageLocators.current_address, text)

    def remove_footer(self):
        self.browser.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.browser.execute_script("document.getElementById('fixedban').style.display='none'")

    def open_state_list(self):
        self.wait_and_click(FormPageLocators.state_list)

    def select_state(self):
        self.wait_and_click(FormPageLocators.NCR)

    def open_city_list(self):
        self.wait_and_click(FormPageLocators.city_list)

    def select_city(self):
        self.wait_and_click(FormPageLocators.DELHI)

    def click_submit(self):
        self.wait_and_click(FormPageLocators.btn_submit)

    def check_modal_email(self):
        email_text = self.get_text(FormPageLocators.modal_email)
        assert email_text == "test123@gmail.com"

    def check_phone_number(self):
        phone_text = self.get_text(FormPageLocators.modal_mobile_number)
        assert phone_text == "1132124499"

    def check_gender(self):
        gender_text = self.get_text(FormPageLocators.modal_gender_male)
        assert gender_text == "Male"


















