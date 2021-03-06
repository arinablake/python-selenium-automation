from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from time import sleep

SC_LOCATOR = (By.CSS_SELECTOR, "#nav-cart")
CHECK_PAGE = (By.CSS_SELECTOR, ".sc-empty-cart-header")

# open the url
@given('Open Amazon page')
def open_amazon_help_page(context):
    context.driver.get('https://www.amazon.com')

# click
@when ('Click Shopping cart button')
def click_sc_button(context):
    amazon_sc_button = context.driver.find_element(*SC_LOCATOR)
    amazon_sc_button.click()

# wait for 2 sec
    sleep(2)

# verify
@then ('Your Shopping Cart is empty. in a header is shown')
def check_page(context):
    assert 'Your Shopping Cart is empty.' in context.driver.find_element(*CHECK_PAGE).text

# wait for 2 sec
    sleep(2)


