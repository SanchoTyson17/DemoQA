from pages.form_page import FormPage
from selenium.webdriver.common.by import By
import time
from generator.generator import generate_person


def test_form1(browser):
    person = generate_person()
    form_page = FormPage(browser)
    form_page.open('https://demoqa.com/automation-practice-form')
    form_page.fill_in_fist_name(person.first_name)
    form_page.fill_in_last_name(person.first_name)
    form_page.fill_in_email(person.email)
    form_page.select_male_radiobutton()
    form_page.fill_in_number("1234567899")
    form_page.open_birth_date_window()
    form_page.show_year_list()
    form_page.select_year()
    form_page.select_date()
    form_page.scroll_down()
    form_page.fill_in_subject("e")
    form_page.select_subject()
    form_page.select_sports_radiobatton()
    form_page.add_picture('/Users/sasha17/PycharmProjects/DemoQA/data/ship.jpg')
    form_page.fill_in_adress(person.address)
    form_page.remove_footer()
    form_page.open_state_list()
    form_page.select_state()
    form_page.open_city_list()
    form_page.select_city()
    form_page.click_submit()
    time.sleep(2)
    form_page.check_modal_email()
    form_page.check_phone_number()
    form_page.check_gender()


def test_form2(browser):
    main_page = MainPage(browser)
    main_page.open("https://demoqa.com/")
    main_page.click_practice_form1()
    form_table_page = FormPageTable(browser)
    form_table_page.click_practice_form()
    form_page = FormPage(browser)
    form_page.fill_in_fist_name("First")
    time.sleep(10)







