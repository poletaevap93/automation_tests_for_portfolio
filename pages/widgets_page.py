from selenium.common import TimeoutException

from locators.widgets_page_locators import AccordianPageLocators
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