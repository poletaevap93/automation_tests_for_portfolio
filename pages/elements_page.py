import time

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxLocators()

    def fill_all_fields(self):   # метод по заполнению всех полей   #send_keys - для вставки в поле
        person_info = next(generated_person())   # позволяет делать экземпляр класса с рандомнами значениями только 1 раз!
        full_name = person_info.full_name  #заполняю поля рандомом, повторяющимся 1 раз
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)   # подставляю сгенерированые поля
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_field_form(self):   # проверка получившейся таблицы
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]   #.split(":")[1]  - чтобы получить 2ю часть таблички, именно со значением
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


