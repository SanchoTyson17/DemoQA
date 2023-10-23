from pages.form_page import FormPage
import time

def test_form1(browser):
    form_page = FormPage(browser)
    form_page.open()
    form_page.fill_in_firs_name()


