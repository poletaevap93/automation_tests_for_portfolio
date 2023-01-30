import time
from locators.elements_page_locators import TextBoxLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxLocators()

    def fill_all_fields(self):   # метод по заполнению всех полей   #send_keys - для вставки в поле
        self.element_is_visible(self.locators.FULL_NAME).send_keys('gerg')
        self.element_is_visible(self.locators.EMAIL).send_keys('wefwef@nmtyj.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('feweeeeeewwwww')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('tththththth5545')
        self.element_is_visible(self.locators.SUBMIT).click()

    def check_field_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]   #.split(":")[1]  - чтобы получить 2ю часть таблички, именно со значением
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


