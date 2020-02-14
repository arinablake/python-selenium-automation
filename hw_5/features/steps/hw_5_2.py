from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.CSS_SELECTOR, "#twotabsearchtextbox")
SEARCH_BUTTON = (By.CSS_SELECTOR, ".nav-input[value='Go']")
SEARCH_RESULTS_LOCATOR = (By.CSS_SELECTOR, '.s-result-list.s-search-results > div[data-index]')
BEST_SELLER = (By.CSS_SELECTOR, ".a-badge-label")


@given('Open Amazon page')
def open_amazon_help_page(context):
    context.driver.get('https://www.amazon.com')

@when ('Search input fill {search_text}')
def input_text(context, search_text):
    search_input = context.driver.find_element(*SEARCH_INPUT)
    search_input.clear()
    search_input.send_keys(search_text)

    sleep(2)

@when ('Click search button')
def click_button(context):
    search_button = context.driver.find_element(*SEARCH_BUTTON)
    search_button.click()

    sleep(2)


@then ('Counting best sellers fantasy books')
def count_bsfantasy_books(context):
    best_seller_count = 0
    bsfantasy_books_list = context.driver.find_elements(*BEST_SELLER)
    best_seller_count += len(bsfantasy_books_list)
    print(best_seller_count)

