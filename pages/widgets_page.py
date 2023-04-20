import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):

    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):  # тут используется словарик для компактности теста. Он позволит удобно обращаться к элементам
        accordian = {'first': # первая вкладка
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_CONTENT_FIRST},
                     'second': # вторая вкладка
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_CONTENT_SECOND},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_CONTENT_THIRD}
                     }

        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()  # будет кликать подряд на каждую
        try:  # это потому, что когда изначально загружается страница, первая вкладка уже раскрыта
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
            section_title.click()
        except TimeoutException: # если она была открыта, то я ее выше закрыл. И если так, то снова проделываю тоже самое:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
            section_title.click()
        return [section_title.text, len(section_content)]

class AutoCompletePage(BasePage): # тестирование форм, куда можно забивать цвета, в один инпут вставляется одно название, в другой можно несколько

    locators = AutoCompletePageLocators()

    def fill_input_multi(self):   # тест со множеством значений в инпуте
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))   # переменная, в которой хранится выбранный из генератора цвет. random sample - выбор уникального рандомного элемента из массива, k= - количество вбиваемых цветом, рандомно
        for color in colors:  # цикл для того, что каждый цвет по отдельности вбивался в инпут
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)  # спец библиотека, нажатие enter
        return colors

    def remove_value_from_multi(self): # метод позволяющий удалить выбранный цвет из строки. Чтобы проверить, надо взять результат ДО и ПОСЛЕ
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))  # количество значение ДО вбивания цвета
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_DELETE)  # это список данных значений
        for value in remove_button_list:
            value.click()
            break  # в итоге из списка значений удалится только одно значение, и этого хватит, чтобы сранвить до и после, что разница есть, удаление работает

        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE)) # проверяем сколько там ПОСЛЕ
        return count_value_before, count_value_after

    def chech_color_in_multi(self): # проверка какие именно цвета выбрались в строке
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)  # список со всеми цветами
        colors = []
        for color in color_list:  # в массив вытягивается текст, названия цветов
            colors.append(color.text)
        return colors


    def fill_input_single(self):   # тестирования одиночного вбивания цвета
        color = random.sample(next(generated_color()).color_name, k=1)  # переменная, в которой хранится выбранный из генератора цвет. random sample - выбор уникального рандомного элемента из массива, k=1 - количество вбиваемых цветом
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)  # выбираем  цвет
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)  # нажимается энтер
        return color[0]  # потому что возвращается в тесте значение в виде массива

    def check_color_in_single(self):  # проверка выбранного цвета
        color = self.element_is_present(self.locators.SINGLE_VALUE)
        return color.text



