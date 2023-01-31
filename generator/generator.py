#
from data.data import Person
from faker import Faker   # импортирую библиотеку для рандомного заполнения полей в методе ниже

faker_ru = Faker('ru_RU') #обьязательно прописываю, указывая язык
Faker.seed()

def generated_person():
    yield Person(   # yield - это обязательная конструкция, она возвращает класс указанный   # Person - вызываю этот класс со всеми полями
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        email= faker_ru.email(),
        current_address= faker_ru.address(),
        permanent_address= faker_ru.address(),
    )