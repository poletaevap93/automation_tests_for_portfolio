import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


class TestAlertsFrameWindows:
    class TestBrowserWindows:

        def test_new_tab(self, driver):  # тест по открытию новой вкладки
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab()  # текст, который появляется в новой вкладке
            assert text_result == "This is a sample page", "the new tab has not opened"

        def test_new_window(self, driver):  # тест по открытию нового окна
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab()  # текст, который появляется в новом окне
            assert text_result == "This is a sample page", "the window tab has not opened"

    class TestAlertsPage:  # тест с алертами, всплывающими окнами

        def test_see_alert(self, driver):  # обычный алерт
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == "You clicked a button"  # проверка на соответствие текста в появившемся алерте

        def test_alert_appear_5_sec(self, driver):  # появление алерта через 5 сек
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == "This alert appeared after 5 seconds"  # проверка на соответствие текста в появившемся алерте

        def test_confirm_alert(self, driver):  # появление алерта с вариантами выбора
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == "You selected Ok"  # проверка на соответствие текста в появившемся алерте

        def test_pomt_alert(self, driver):  # появление алерта с вариантами выбора
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()  # два значения, т.к. метод возвращает тоже 2 значения
            assert text in alert_text  # проверяем, что значение text содержится в alert_text

    class TestFramePage:  # тестирование фрэймов - когда на экране несколько независимых окон, со своей прокруткой и тд

        def test_frames(self, driver):
            frame_page = FramesPage(driver, "https://demoqa.com/frames")
            frame_page.open()
            result_frame1 = frame_page.check_frame("frame1")
            result_frame2 = frame_page.check_frame("frame2")
            assert result_frame1 == ['This is a sample page', '500px', '350px'], "The frame does not exist" # проверка на соответствие размеров и текста внутри фрэйма
            assert result_frame2 == ['This is a sample page', '100px', '100px'], "The frame does not exist"

    class TestNestedFramesPage: # тестирование вложенных фрэймов

        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == "Parent frame"  # проверка на соответствие текста во фрэймах
            assert child_text == "Child Iframe"

    class TestModalDialodsPage: # тестирование модальных окон всплывающих

        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_dialogs_page.open()
            small, large = modal_dialogs_page.check_modal_dialogs()
            assert small[1] < large[1] # проверка, что длина small меньше чем large по количеству символов ([1] - потому что количество символов стоит вторым по порядку в массивах)
            assert small[0] == 'Small Modal'  # проверка заголовка мелкого окна
            assert large[0] == 'Large Modal'



