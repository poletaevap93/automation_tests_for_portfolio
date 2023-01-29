import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# в этом файле прописываются фикстуры - это некие функции, декораторы, применяя которую в Функции, появляется возможность выполнять что-либо ДО и/или ПОСЛЕ выполнения тестов


# эта фикстура позволяет создавать драйвер и открывать и закрывать браузер
@pytest.fixture(scope="function")  #по дефолту фикстура всегда имеет scope="function". Но лучше указать явно, т.к. есть необходимость чтобы драйвер открывал и закрывал браузер для КАЖДОГО ТЕСТА, чтоб тесты были независимы
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())    #сначала установить через терминал pip install selenium, потом импортировать вэбдрайвер из селениума. Потом скачиваю библиотеку (файл-сеттингс) webdriver-manager. И вставляю driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()   #открывает окно браузера на весь экран
    yield driver   # все, что выше - это будет выполняться до тестов, ниже фразы yield - после тестов. Означает "Верни драйвер"
    driver.quit()


