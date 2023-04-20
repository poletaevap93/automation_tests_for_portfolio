import time

from pages.widgets_page import AccordianPage, AutoCompletePage


class TestWidgets:

    class TestAccordianPage:  # вкладки раскрывающиеся с текстом

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0  # сравниваются заголовки вкладок и что текст внутри не равен нулю
            assert second_title == 'Where does it come from?' and second_content > 0
            assert third_title == 'Why do we use it?' and third_content > 0

    class TestAutoCompletePage:  # тестирование форм, куда можно забивать цвета, в один инпут вставляется одно название, в другой можно несколько цветов

        def test_fill_multi_autocomplete(self, driver): # тест по втавлению цвета в строку
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.chech_color_in_multi()
            assert colors == colors_result  # проверка, что выбранные цвета в инпуте совпадают с вообще возможными, котороые можно выбрать (что не вбились левые названия)

        def test_remove_value_from_multi(self, driver):  # тест позволяющий удалить цвета
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi() # сначала также вбиваю цвет
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()  # сюда приходит количество цветов до удаления и после
            assert count_value_before != count_value_after   # проверка на то, что до удаления и после удаления количество цветов разное


        def test_fill_single_autocomplete(self,driver):  # тест проверки одиночного вбивания цвета
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result






