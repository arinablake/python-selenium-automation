from hw_7.pages.base_page import Page
from selenium.webdriver.common.by import By

class ResultsPage(Page):
    SIGN_IN = (By.XPATH, "//form[@name='signIn']")
    CHECK_PAGE = (By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty")
    LINKS = (By.CSS_SELECTOR, ".hmenu-item[href*='music']")

    def verify_result(self, expected_text: str):
        self.verify_text(expected_text, *self.SIGN_IN)

    def check_cart(self, expected_text: str):
        self.verify_text(expected_text, *self.CHECK_PAGE)

    def check_number(self, num: int):
        self.verify_number(num, *self.LINKS)