from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators
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