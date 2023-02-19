import random
import time
from selenium.webdriver.common.by import By
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxLocators, CheckBoxLocators, RadioButtonLocators, WebTableLocators
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


class CheckBoxPage(BasePage):
    locators = CheckBoxLocators()

    def open_full_list(self):   # открытие всего списка нажатием на +
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):   # чтобы клики происходили рандомно в чекбоксах, во исполнение 5го принципа тестирования
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21   # количество итераций
        while count !=0:        # пока count не равен нулю,
            item = item_list[random.randint(1,15)]   #выбирается случайный чек бокс в диапазоне
            if count > 0:
                self.go_to_element(item)   # self.go_to_element - чтобы чекбоксы не перекрывались экраном,чтобы скролить
                item.click()
                print(item)
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):  # получить выбранные чекбоксы
        checked_list = self.element_are_presents(self.locators.CHECKED_ITEMS)
        data = []   # пустой массив, выполняющий роль буфера, в который будут складываться нужные,выборочные данные
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()  #Форматирую строку,чтоб был одинаковый текст. str(data) - оборачивание массива в строку, чтобы применить replace. Удаляю doc, точки и пробелы. Применяю lower чтобы убрать заглавные


    def get_output_result(self):  # метод получения списка отображаемых названий выбранных чекбоксов
        result_list = self.element_are_presents(self.locators.OUTPUT_RESULT)
        data = []  # пустой массив, выполняющий роль буфера
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower() # тоже форматирую


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    def click_on_the_radio_button(self, choice): # создаю словарь
        choices = {'yes': self.locators.YES_RADIOBUTTON,   # прям тут на месте ключа указываю локаторы
        'Impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
        'no': self.locators.NO_RADIOBUTTON}

        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):   # получаю текст, который подсвечивается при нажатии на баттон
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):   # работа с таблицей
    locators = WebTableLocators()

    def add_new_person(self):  # метод по нажатию кнопки добавит ьчеловека, заполнению полей и нажатию ОК
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary =person_info.salary
            department = person_info.department

            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -=1
            return firstname, lastname, email, age, salary, department







