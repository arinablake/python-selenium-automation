from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.CSS_SELECTOR, "#twotabsearchtextbox")
SEARCH_BUTTON = (By.CSS_SELECTOR, ".nav-input[value='Go']")
ITEM_LOCATOR = (By.CSS_SELECTOR, ".s-include-content-margin:not(.s-border-top-overlap)")

ITEM_HEADER_LOCATOR = (By.CSS_SELECTOR, ".s-result-list.s-search-results .a-size-medium")

BEST_SELLER = (By.CSS_SELECTOR, ".a-badge-label")
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-button')


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

@then ("Amazon page will have {num} history book items")
def count_hist_books(context, num):
    hist_books_list = context.driver.find_elements(*ITEM_LOCATOR)
    assert(len(hist_books_list)) == int(num), f'Expected {num}, but got {len(hist_books_list)}'
    print(len(hist_books_list))

@when ("See last item")
def last_item(context):
    hist_books_list = context.driver.find_elements(*ITEM_LOCATOR)
    list_items = list(hist_books_list)
    context.last_item = list_items[-1]
    print(last_item)
    sleep(2)

@then ("Last item has {search_text} label")
def last_best_seller(context, search_text):
    last_item_best_sel = context.last_item.find_elements(*BEST_SELLER)
    context.last_item_b = len(last_item_best_sel) > 0
    sleep(2)

@when ("Click the item link")
def last_best_seller_c(context):
    if context.last_item_b == True:
        last_item_header = context.last_item.find_elements(*ITEM_HEADER_LOCATOR)
        last_item_header.click()

@when('Add an item to shopping cart')
def add_item_to_cart(context):
    if context.last_item_b == True:
        add_to_cart_button = context.driver.find_elements(*ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

        sleep(2)

