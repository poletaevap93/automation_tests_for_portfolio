import time

from pages.alerts_frame_windows_page import BrowserWindowsPage


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


