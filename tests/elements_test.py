import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()

            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()  #вводимые значения
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_field_form()  #значения табличные на выходе
            assert full_name == output_name, "the full name is not match" # через запятую указывается комментарий, если вдруг произойдет ошибка    # расписано все по отдельности для того, чтобы если возникнет баг, в отчете было точно написано где именно в коде
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
            output_yes = radio_button_page.get_output_result() # получаю текст
            radio_button_page.click_on_the_radio_button('Impressive')
            output_Impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not been select"
            assert output_Impressive == 'Impressive', "'Impressive' have not been select"
            assert output_no == 'No', "'No' have not been select"

    class TestWebTable: # тестирование вэб таблицы

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result





