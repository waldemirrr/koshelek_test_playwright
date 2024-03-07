import pytest
from pages.sign_up_page import SignUpPage
from playwright.sync_api import Page


@pytest.fixture
def sign_up_page(page: Page) -> SignUpPage:
    sign_up_page = SignUpPage(page)
    sign_up_page.navigate_to_page()
    return sign_up_page

