from pages.sign_up_page import SignUpPage
from test_data.sign_up_data import sign_up_data
import pytest


sign_up_test_data = [tuple(my_dict.values()) for my_dict in sign_up_data]


@pytest.mark.parametrize('test_data', sign_up_test_data)
def test_negative_sign_up_scenarios(sign_up_page: SignUpPage, test_data) -> None:
    username, username_error, email, email_error, password, is_password_correct, password_error, \
        referral_code, referral_code_error, click_checkbox, checkbox_status, \
        submit_form, is_submit_button_inactive = test_data

    sign_up_page.fill_username_form_field(username)
    sign_up_page.fill_email_form_field(email)
    sign_up_page.fill_password_form_field(password)
    sign_up_page.fill_referral_code_field(referral_code)
    sign_up_page.check_checkbox(click_checkbox)
    sign_up_page.submit_form(submit_form)
    sign_up_page.check_username_error_message(username_error)
    sign_up_page.check_email_error_message(email_error)
    sign_up_page.check_password_message(is_password_correct, password_error)
    sign_up_page.check_referral_code_error_message(referral_code_error)
    sign_up_page.check_checkbox_status(checkbox_status)


