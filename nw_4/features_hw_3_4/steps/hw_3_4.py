from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SC_LOCATOR = (By.CSS_SELECTOR, "#nav-cart")
SEARCH_INPUT = (By.CSS_SELECTOR, "#twotabsearchtextbox")
SEARCH_BUTTON = (By.CSS_SELECTOR, ".nav-input[value='Go']")
RANDOM_ITEM = (By.CSS_SELECTOR, ".s-result-list.s-search-results .s-result-item .a-size-medium")
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-button')
CHECK_PAGE = (By.CSS_SELECTOR, ".a-size-medium.sc-product-title")

POP_UP_LOCATOR_1 = (By.CSS_SELECTOR, "#attach-warranty-pane")
POP_UP_LOCATOR_2 = (By.CSS_SELECTOR, "#attach-accessory-pane")
CLOSE_POP_UP_1 = (By.CSS_SELECTOR, "#attachSiNoCoverage-announce")
CLOSE_POP_UP_2 = (By.CSS_SELECTOR, "#attach-close_sideSheet-link")

# open the url
@given('Open Amazon page')
def open_amazon_help_page(context):
    context.driver.get('https://www.amazon.com')

# click
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

@when ('Choose first item')
def choose_item(context):
    random_item = context.driver.find_element(*RANDOM_ITEM)
    random_item.click()

    sleep(2)

@when ('Add an item to shopping cart')
def add_item_to_cart(context):
    add_to_cart_button = context.driver.find_element(*ADD_TO_CART_BUTTON)
    add_to_cart_button.click()

    sleep(2)

@when ('See pop up 1')
def see_pop_up(context):
    pop_up_locator_1 = context.driver.find_elements(*POP_UP_LOCATOR_1)
    context.pop_up_1 = len(pop_up_locator_1 ) > 0
    sleep(2)

@when ('Close pop up 1')
def pop_up(context):
    if context.pop_up_1 == True:
        close_pop_up_1 = context.driver.find_element(*CLOSE_POP_UP_1)
        close_pop_up_1.click()
    sleep(2)
#
@when ('See pop up 2')
def see_pop_up(context):
    pop_up_locator_2 = context.driver.find_elements(*POP_UP_LOCATOR_2)
    context.pop_up_2 = len(pop_up_locator_2) > 0
    sleep(2)

@when ('Close pop up 2')
def pop_up(context):
    if context.pop_up_2 == True:
        close_pop_up_2 = context.driver.find_element(*CLOSE_POP_UP_2)
        close_pop_up_2.click()
    sleep(2)

@when ('Click Shopping cart button')
def click_sc_button(context):
    amazon_sc_button = context.driver.find_element(*SC_LOCATOR)
    amazon_sc_button.click()

    sleep(2)

# verify
@then ('{search_text} in Shopping Cart is shown')
def check_item_page(context, search_text):
    assert search_text in context.driver.find_element(*CHECK_PAGE).text

# wait for 2 sec
    sleep(2)

