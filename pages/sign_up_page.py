from playwright.sync_api import Page


class SignUpPage:
    URL = 'https://exchange.konomik.com/authorization/signup'

    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate_to_page(self) -> None:
        self.page.goto(self.URL)


