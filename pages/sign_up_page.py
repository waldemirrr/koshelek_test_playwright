from playwright.sync_api import Page, expect, Locator
import re


class SignUpPage:
    URL = 'https://koshelek.ru/authorization/signup'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_field = self.page.locator('[data-wi="user-name"]').locator('input')
        self.email_field = self.page.locator('[data-wi="identificator"]').locator('input')
        self.password_field = self.page.locator('[data-wi="password"]').locator('input')
        self.referral_code_field = self.page.locator('[data-wi="referral"]').locator('input')
        self.checkbox = self.page.locator('[data-wi="user-agreement"]').locator('input')
        self.submit_button = self.page.locator('[data-wi="submit-button"]').locator('button')
        self.username_error_message = self.page.locator('[data-wi="user-name"]').locator('.v-text-field__details')
        self.email_error_message = self.page.locator('[data-wi="identificator"]').locator('.v-text-field__details')
        self.password_error_message = self.page.locator('[data-wi="password"]').locator('.v-text-field__details')
        self.referral_code_error_message = self.page.locator('[data-wi="referral"]').locator('.v-text-field__details')
        self.checkbox_status = self.page.locator('[class="k-checkbox-auth"]').locator('use')

    def navigate_to_page(self) -> None:
        self.page.goto(self.URL)

    def fill_username_form_field(self, value: str) -> None:
        self.username_field.fill(value)

    def fill_email_form_field(self, value: str) -> None:
        self.email_field.fill(value)

    def fill_password_form_field(self, value: str) -> None:
        self.password_field.fill(value)

    def fill_referral_code_field(self, values:str) -> None:
        self.referral_code_field.fill(values)

    def check_checkbox(self, value: str) -> None:
        if value:
            self.checkbox.click()

    def submit_form(self, value: str) -> None:
        if value:
            self.submit_button.click()

    def check_username_error_message(self, value: str) -> None:
        expect(self.username_error_message).to_contain_text(value)

    def check_email_error_message(self, value: str) -> None:
        expect(self.email_error_message).to_contain_text(value)

    def check_password_message(self, is_password_correct: bool, value: str) -> None:
        if is_password_correct:
            correct_message = self.page.locator('div[data-pw="auth-widget-password-input-message"] div')
            expect(correct_message).to_contain_text(re.compile(r'(низкая|средняя|выше среднего)'))
        else:
            expect(self.password_error_message).to_contain_text(value)

    def check_referral_code_message(self, value: str) -> None:
        expect(self.referral_code_error_message).to_contain_text(value)

    def check_checkbox_status(self, value: str) -> None:
        if value == 'Unchecked':
            expect(self.checkbox_status).to_have_attribute('href', '#system--default--$checkboxError')
        if value == 'Checked':
            expect(self.checkbox_status).to_have_attribute('href', '#system--default--$checkboxOnNew')
        if value == 'Off':
            expect(self.checkbox_status).to_have_attribute('href', '#system--default--$checkboxOff')

    def is_submit_form_button_disabled(self, value: str) -> None:
        if value:
            expect(self.submit_button).to_have_attribute('disabled', 'disabled')

