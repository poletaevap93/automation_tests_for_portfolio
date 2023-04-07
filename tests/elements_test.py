import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()

            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()  # вводимые значения
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_field_form()  # значения табличные на выходе
            assert full_name == output_name, "the full name is not match"  # через запятую указывается комментарий, если вдруг произойдет ошибка    # расписано все по отдельности для того, чтобы если возникнет баг, в отчете было точно написано где именно в коде
            assert email == output_email, "the email is not match"
            assert current_address == output_current_address, "the current_address is not match"
            assert permanent_address == permanent_address, "the permanent_address is not match"

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result, 'checkboxes have not been selected'

    class TestRadioButton:

        def test_radio_button(self, driver):  # тестирую выбор радиобатонов
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()  # получаю текст
            radio_button_page.click_on_the_radio_button('Impressive')
            output_Impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not been select"
            assert output_Impressive == 'Impressive', "'Impressive' have not been select"
            assert output_no == 'No', "'No' have not been select"

    class TestWebTable:  # тестирование вэб таблицы

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result

        def test_web_table_search_person(self, driver):  # поиск человека в таблице по критериям
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0,
                                                                      5)]  # записываю в переменную кеу рандомно созданное либо имя новго человека, либо возраст и тд(всего 6 позиций)
            web_table_page.search_some_person(key_word)  # поиск человека в таблице по добавленному рандомному значению
            table_result = web_table_page.check_search_person()  # проверка корректности работы поиска
            assert key_word in table_result, 'the person was not found in the table'  # проверка, что кей ворд содержится в таблице

        def test_web_table_update_person_info(self, driver):  # обновление информации о человеке
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]  # создаю персонажа и записываю фамилию, 2й элемент по счету
            web_table_page.search_some_person(lastname)  # ищу по фамилии в таблице того, у кого буду менять значения
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "the person card has not been changed"  # проверяю, что новый возраст содержится в строке

        def test_web_table_delete_person(self, driver):  # тест на удаление
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]  # создаю персонажа и записываю емайл, 4й элемент по счету
            web_table_page.search_some_person(email)  # нахожу персонажа
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found"

        def test_web_table_change_count_row(self, driver):  # тест по изменению количества выводимых строк в таблице
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50,
                             100], 'The number of rows in the table has not benn changed or has changed incorrectly'

    class TestButtonPage:

        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == "You have done a double click"
            assert right == "You have done a right click"
            assert click == "You have done a dynamic click"

    class TestLinksPage:  # метод проверки открывания ссылок (рабочая и битая)

        def test_check_link(self, driver):  # проверка рабочей ссылки
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            print(href_link, current_url)

        def test_broken_link(self, driver):  # тест битой ссылки, с 400 кодом ответа
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link("https://demoqa.com/bad-request")
            assert response_code == 400

    class TestUploadAndDownload:  # тест скачивания и загрузки файла

        def test_upload_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, result = upload_download_page.upload_file()  # в обе переменные (т.к. upload_file() возвращает 2 переменные) записываю результат выполнения
            assert file_name == result, "the file has not been uploaded"

        def test_download_file(self, driver):  # cуть: картинка закодирована в ссылке, на сайте. Я этот код беру, преобразую, записываю в нужном виде в файл пустышку и проверяю, создалась ли эта картинка у меня в проекте или нет
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True, "the file has not been downloaded"  # проверка, правда ли, что происходит скачивание нужного файла

    class TestDynamicPropertiesPage:  # динамические изменения на странице

        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True, "button did not enable after 5 sec"  # проверка, что кнопка действительно кнопка станет кликабельна через 5 сек

        def test_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_of_color()  # две переменные, т.к. метод возвращает тоже 2 значения
            assert color_after != color_before, "colors have not been changed"  # проверяю, что цвета по итогу разные

        def test_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_button()
            assert appear is True, "button did not appear after 5 sec"  # проверка, что кнопка действительно появляется через 5 сек
