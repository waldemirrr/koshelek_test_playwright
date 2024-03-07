from playwright.sync_api import expect
from pages.sign_up_page import SignUpPage


def test_sign_up_page_has_title(sign_up_page: SignUpPage, page) -> None:
    sign_up_page.navigate_to_page()
    expect(sign_up_page.page).to_have_title('Криптовалютная экосистема в кошельке')


