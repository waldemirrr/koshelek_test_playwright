from pages.sign_up_page import SignUpPage
from test_data.sign_up_data import sign_up_data
import pytest


# Преобразовываем тестовые данные из списка словарей в список кортежей
sign_up_test_data = [tuple(my_dict.values()) for my_dict in sign_up_data]


# Параметризируем тест
@pytest.mark.parametrize('test_data', sign_up_test_data)
def test_negative_sign_up_scenarios(sign_up_page: SignUpPage, test_data) -> None:
    # Распаковка тестовых данных из параметризации
    username, username_error, email, email_error, password, is_password_correct, password_error, \
        referral_code, referral_code_message, click_checkbox, checkbox_status, \
        submit_form, is_submit_button_disabled = test_data

    # Заполнить поле имени пользователя
    sign_up_page.fill_username_form_field(username)

    # Заполнить полe email
    sign_up_page.fill_email_form_field(email)

    # Заполнить поле пароля
    sign_up_page.fill_password_form_field(password)

    # Заполнить поле реферального кода
    sign_up_page.fill_referral_code_field(referral_code)

    # Кликнуть чекбокс
    sign_up_page.check_checkbox(click_checkbox)

    # Нажать на кнопку отправки формы "Далее"
    sign_up_page.submit_form(submit_form)

    # Проверить сообщение об ошибке поля пользователя
    sign_up_page.check_username_error_message(username_error)

    # Проверить сообщение об ошибке поля email
    sign_up_page.check_email_error_message(email_error)

    # Проверить сообщение о поле пароль (Не только ошибки)
    sign_up_page.check_password_message(is_password_correct, password_error)

    # Проверить сообщение о поле реферального года
    sign_up_page.check_referral_code_message(referral_code_message)

    # Проверить статус чекбокса
    sign_up_page.check_checkbox_status(checkbox_status)

    # Проверить неактивна ли кнопка
    sign_up_page.is_submit_form_button_disabled(is_submit_button_disabled)


