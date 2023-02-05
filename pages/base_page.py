# тут создаю методы, которые будут облегчать работу с остальными страницами
# родительский класс для остальных страниц

from selenium.webdriver.support.ui import WebDriverWait as wait  # импортирую
from selenium.webdriver.support import expected_conditions as EC  # импортирую

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):   # чтобы элемент был видимый
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):   # чтобы элементы были видимы
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):   # чтобы найти элемент который представлен на странице (не обязательно в поле видимости, можно в DOMе)...и чтобы не скроллить страницу
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_presents(self, locator,timeout=5):  # чтобы найти элемент который представлен на странице (не обязательно в поле видимости, можно в DOMе)...и чтобы не скроллить страницу
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):   # чтобы элемент был невидимый
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):   # скроллит к нужному элементу
        self.driver.execute_script("arguments[0].scrollIntoView();", element)    #execute_script('') - метод, позволяющий запускать скрипты. "arguments[0].scrollIntoView();" - стандартное