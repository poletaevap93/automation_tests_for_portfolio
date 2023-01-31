import time

from pages.elements_page import TextBoxPage

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
