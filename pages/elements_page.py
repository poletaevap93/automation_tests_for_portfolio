import os
import random
import time

import requests
from selenium.webdriver.common.by import By
from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxLocators, CheckBoxLocators, RadioButtonLocators, WebTableLocators, \
    ButtonsPageLocators, LinksPageLocators, UploadAndDownloadPageLocators
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
            return [firstname, lastname,  str(age), email, str(salary), department]  # чтобы выводилось в листе и все значения в строках str

    def check_new_added_person(self):  # метод проверки правильности добавления человека в таблицу

        people_list = self.element_are_presents(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())   # добавляю в буфер строки из таблицы, разделяя на разные слова
        return data

    def search_some_person(self, key_word):  # функция поиска какого либо человека в таблице
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):  # проверка найденного в поиске человека, что он есть по итогу в таблице и совпадает. Поиск будет по gjzdkz.otqcz функции удаления
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)  # поиск в родительской строке через функцию удаления
        return row.text.splitlines()

    def update_person_info(self):   # метод изменения инфы человека в таблице
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    def delete_person(self):   # метод удаления из таблицы
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted(self):   # метод проверки удаления из таблицы
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    def select_up_to_some_rows(self):   # метод выбора количества выводимых строк
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)  #чтобы скролил до появления строки выбора строк
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"]')).click()  # использую форматирование строки f. На каждой интерации на х будет подставляться то 5, то 10 и тд и сразу кликать
            data.append(self.check_count_rows())   # сюда добавляется количество строк после каждого клика на список
        return data


    def check_count_rows(self):  # метод проверки количества строк
        list_rows = self.element_are_presents(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)  # возвращаю количество, длинну списка



class ButtonsPage(BasePage):   # 3 кнопки: с двойным нажатием, правой, и обычный

    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click):  # громоздко, но все понятно и в одном методе 3 нажатия
        if type_click =="double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)

        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)

        if type_click == "click":
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)


    def check_clicked_on_the_button(self, element):   # проверка текста, который появляется после нажатия на кнопки
        return self.element_is_present(element).text


class LinksPage (BasePage):    # проверка ссылок на странице
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)  # импорт спец библиотеки для возможности отправки запроса по нужной ссылке
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1]) # смысл такой: драйвер, переключи свое внимание на окно с индексом 1, и он переключает на новую вкладку, которая окрывается после клика
            url = self.driver.current_url   # эту ссылку вытягиваю из открывшегося окна, чтобы можно было сравнить
            return link_href, url
        else:
            return request.status_code, link_href

    def check_broken_link(self, url):   # проверка поломанной ссылки
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST).click()
        else:
            return request.status_code

class UploadAndDownloadPage (BasePage):
    locators = UploadAndDownloadPageLocators()

    def upload_file(self):
        file_name, path = generated_file()# создаю файл через генератор
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path) # пихаю созданный файл на страницу
        os.remove(path)  # сразу удаляю рандомно созданный файл
        text = self.element_is_present(self.locators.UPLOADED_RESULT).text #  сохраняю название загруженного на страницу рандомного файла
        return file_name.split("\\")[-1], text.split("\\")[-1]  # тут с помощью регулярки я вытаскиваю и возвращаю только последнюю часть названия созданного в моей папке рандомного файла и часть названия, которое отобразилось на странице после загрузки (т.к. их пути не совпадают полностью). Разбиваю по слешам и с помощью [-1] достаю именно послее значение





    #def download_file(self):

















