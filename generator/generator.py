# класс для генерации рандомных значений
import random

from data.data import Person
from faker import Faker   # импортирую библиотеку для рандомного заполнения полей в методе ниже

faker_ru = Faker('ru_RU') #обьязательно прописываю, указывая язык
Faker.seed()

def generated_person():
    yield Person(   # yield - это обязательная конструкция, она возвращает класс указанный   # Person - вызываю этот класс со всеми полями
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10,80),
        department=faker_ru.job(),   # какая то работа рандомная подставляется
        salary=random.randint(30000,50000),
        email= faker_ru.email(),
        current_address= faker_ru.address(),
        permanent_address= faker_ru.address(),
    )

def generated_file():  # для генерации файлов рандомных
    path = rf"D:\pythonProject\automation_tests_for_portfolio\filetest{random.randint(0,999)}.txt"  # указываю абсолютный путь до места генерации (временного) файла. Указываю просто диск С. r - регулярное выр-е
    file = open(path, "w+")  # открывается файл.  w+ означает открыть файл для записи
    file.write(f"HelloWorld{random.randint(0,999)}")  # записываю в файл рандомное значение
    file.close()
    return file.name, path   # возвращаю название файла с помощью функции file.name и путь