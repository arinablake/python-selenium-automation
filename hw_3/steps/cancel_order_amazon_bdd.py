from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from time import sleep

SEARCH_INPUT_LOCATOR = (By.XPATH, "//input[@id='helpsearch']")
SEARCH_BUTTON_LOCATOR = (By.XPATH, "//span[@id='helpSearchSubmit']//input[@type='submit']")
CHECK_PAGE = (By.XPATH, "//div[@class='help-content']")

driver = webdriver.Chrome(executable_path='../../drivers/chromedriver')

# open the url
@given('Open Amazon help page')
def open_amazon_help_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when ('Input {search_text} into search field')
def search_input_field(context, search_text):
    amazon_search_input = context.driver.find_element(*SEARCH_INPUT_LOCATOR)
    amazon_search_input.clear()
    amazon_search_input.send_keys('Cancel order')

# click search
@when ('Click search button')
def click_search_button(context):
    amazon_search_button = context.driver.find_element(*SEARCH_BUTTON_LOCATOR)
    amazon_search_button.click()

# wait for 2 sec
sleep(2)

# verify
@then ('{search_text} page is shown')
def check_page(context, search_text):
    assert 'Cancel Items or Orders' in context.driver.find_element('CHECK_PAGE').text

# wait for 2 sec
sleep(2)

driver.quit()

