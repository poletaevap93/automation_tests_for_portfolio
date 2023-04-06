import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage


class TestAlertsFrameWindows:

    class TestBrowserWindows:

        def test_new_tab(self, driver): # тест по открытию новой вкладки
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab()  # текст, который появляется в новой вкладке
            assert text_result == "This is a sample page", "the new tab has not opened"

        def test_new_window(self, driver): # тест по открытию нового окна
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab()  # текст, который появляется в новом окне
            assert text_result == "This is a sample page", "the window tab has not opened"

    class TestAlertsPage: # тест с алертами, всплывающими окнами

        def test_see_alert(self,driver):  # обычный алерт
            alert_page = AlertsPage (driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == "You clicked a button"  # проверка на соответствие текста в появившемся алерте


        def test_alert_appear_5_sec(self,driver):  # появление алерта через 5 сек
            alert_page = AlertsPage (driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == "This alert appeared after 5 seconds"  # проверка на соответствие текста в появившемся алерте


        def test_confirm_alert(self,driver):  # появление алерта с вариантами выбора
            alert_page = AlertsPage (driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == "You selected Ok"  # проверка на соответствие текста в появившемся алерте


        def test_pomt_alert(self,driver):  # появление алерта с вариантами выбора
            alert_page = AlertsPage (driver, "https://demoqa.com/alerts")
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()  # два значения, т.к. метод возвращает тоже 2 значения
            assert text in alert_text  # проверяем, что значение text содержится в alert_text
