import random
import time

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators
from locators.elements_page_locators import FramesPageLocators, NestedFramesPageLocators, ModalDialodsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):  # проверка открытия новой вкладки
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[
                                         1])  # это переключатель на вновь открытую вкладку (поэтому 1 стоит, но можно и 2 и 3 и тд). Смысл такой: драйвер, переключи свое внимание на окно с индексом 1, и он переключает на новую вкладку, которая окрывается после клика
        text_title = self.element_is_present(
            self.locators.TITLE_NEW).text  # получение текста новой вкладки в момент переключения
        return text_title

    def check_opened_new_window(self):  # проверка открытия новой вкладки
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[
                                         1])  # это переключатель на вновь открытое окно (поэтому 1 стоит, но можно и 2 и 3 и тд). Смысл такой: драйвер, переключи свое внимание на окно с индексом 1, и он переключает на новую вкладку, которая окрывается после клика
        text_title = self.element_is_present(
            self.locators.TITLE_NEW).text  # получение текста новой вкладки в момент переключения
        return text_title


class AlertsPage(BasePage):  # тесты на всплывающие алерты

    locators = AlertsPageLocators()

    def check_see_alert(self):  # тест на обычный алерт
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert  # переключатель на появившийся алерт
        return alert_window.text

    def check_alert_appear_5_sec(self):  # тест на алерт появляющийся после 5 сек после нажатия
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(5)
        alert_window = self.driver.switch_to.alert  # переключатель на появившийся алерт
        return alert_window.text

    def check_confirm_alert(self):  # тест на алерт c возможностью выбора ответа
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert  # переключатель на появившийся алерт
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    def check_prompt_alert(self):  # тест на алерт c возможностью ввода какого-то значения
        text = f"autotest{random.randint(0, 999)}"  # это рандомный текст, который будет вставляться в алерт
        self.element_is_visible(self.locators.PROMT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert  # переключатель на появившийся алерт
        alert_window.clear()
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMT_RESULT).text
        return text, text_result


class FramesPage(BasePage):  # тестирование фрэймов - когда на экране несколько независимых окон, со своей прокруткой и тд

    locators = FramesPageLocators()

    def check_frame(self, frame_num):   # frame_num - порядковый номер фрэйма. В одном методе 2 теста сразу
        if frame_num == "frame1":
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute("width")  # вытаскиваю ширину фрэйма
            height = frame.get_attribute("height") # вытаскиваю высоту фрэйма
            self.driver.switch_to.frame(frame)   # переключатель на фрэйм (в скобках указан локатор нужного фрэйма)
            text = self.element_is_present(self.locators.TITLE_FRAME).text  # достаю текст из фрэйма
            self.driver.switch_to.default_content()  # переключатель в исходное положение, чтобы смог выполниться следующий тест
            return [text, width, height]
        if frame_num == "frame2":   # маленький фрэйм
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute("width")  # вытаскиваю ширину фрэйма
            height = frame.get_attribute("height") # вытаскиваю высоту фрэйма
            self.driver.switch_to.frame(frame)   # переключатель на фрэйм (в скобках указан локатор нужного фрэйма)
            text = self.element_is_present(self.locators.TITLE_FRAME).text  # достаю текст из фрэйма
            self.driver.switch_to.default_content()
            return [text, width, height]

class NestedFramesPage(BasePage):  # тестирование вложенных фрэймов

    locators = NestedFramesPageLocators()

    def check_nested_frame(self):  # тут без переключателя в дефолтный контент, т.к. вложенные!
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)  # переключатель
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text  # достаю текст из фрэйма

        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)  # переключатель
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text

class ModalDialogsPage(BasePage):  # тестирование модульных всплывающих окон (маленького и большого). Без использования переключателя switch_to

    locators = ModalDialodsPageLocators()

    def check_modal_dialogs(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        title_small = self.element_is_visible(self.locators.SMALL_MODAL_TITLE).text # вытаскиваю заголовок окна
        text_small = self.element_is_visible(self.locators.SMALL_MODAL_TEXT).text # вытаскиваю текст внутри окна
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()   # закрываю окно

        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        title_large = self.element_is_visible(self.locators.LARGE_MODAL_TITLE).text  # вытаскиваю заголовок окна
        text_large = self.element_is_visible(self.locators.LARGE_MODAL_TEXT).text  # вытаскиваю текст внутри окна
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()
        return [title_small, len(text_small)], [title_large, len(text_large)]  # len(text_large) - беру количество символов в тексте
