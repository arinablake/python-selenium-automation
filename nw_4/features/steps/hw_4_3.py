from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BOX = (By.CSS_SELECTOR, ".benefit-container .benefit-box")

@given('Open Amazon prime page')
def open_amazon_help_page(context):
    context.driver.get('https://www.amazon.com/amazonprime')


@when('See box')
def see_box(context):
    box = context.driver.find_elements(*BOX)
    context.box = len(box) > 0
    sleep(2)


@then ('Amazon prime page will have {num} boxes')
def amazon_prime_box(context, num):
    if context.box == True:
        box = context.driver.find_elements(*BOX)
        assert (len(box)) == int(num), f'Expected {num}, but got {len(box)}'

    sleep(2)

