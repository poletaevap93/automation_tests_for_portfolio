import random
import time

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):  # проверка открытия новой вкладки
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1]) # это переключатель на вновь открытую вкладку (поэтому 1 стоит, но можно и 2 и 3 и тд). Смысл такой: драйвер, переключи свое внимание на окно с индексом 1, и он переключает на новую вкладку, которая окрывается после клика
        text_title = self.element_is_present(self.locators.TITLE_NEW).text  # получение текста новой вкладки в момент переключения
        return text_title

    def check_opened_new_window(self):  # проверка открытия новой вкладки
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1]) # это переключатель на вновь открытое окно (поэтому 1 стоит, но можно и 2 и 3 и тд). Смысл такой: драйвер, переключи свое внимание на окно с индексом 1, и он переключает на новую вкладку, которая окрывается после клика
        text_title = self.element_is_present(self.locators.TITLE_NEW).text  # получение текста новой вкладки в момент переключения
        return text_title

class AlertsPage(BasePage): # тесты на всплывающие алерты

    locators = AlertsPageLocators()

    def check_see_alert(self):  # тест на обычный алерт
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert # переключатель на появившийся алерт
        return alert_window.text

    def check_alert_appear_5_sec(self):  # тест на алерт появляющийся после 5 сек после нажатия
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(5)
        alert_window = self.driver.switch_to.alert # переключатель на появившийся алерт
        return alert_window.text

    def check_confirm_alert(self):  # тест на алерт c возможностью выбора ответа
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert  # переключатель на появившийся алерт
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    def check_prompt_alert(self):  # тест на алерт c возможностью ввода какого-то значения
        text = f"autotest{random.randint(0,999)}"  # это рандомный текст, который будет вставляться в алерт
        self.element_is_visible(self.locators.PROMT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert  # переключатель на появившийся алерт
        alert_window.clear()
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMT_RESULT).text
        return text, text_result