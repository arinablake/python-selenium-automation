from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.CSS_SELECTOR, "#searchval")
SEARCH_BUTTON = (By.CSS_SELECTOR, ".banner-search-btn")
TITLES = (By.CSS_SELECTOR, "a.description:not(.ossRelatedLinks)")
ITEM_BLOCKS =(By.CSS_SELECTOR, "#product_listing .ag-item.gtm-product")
ADD_TO_CART = (By.CSS_SELECTOR, ".btn[name='addToCartButton']")
CART_BUTTON = (By.CSS_SELECTOR, "a[href*='viewcart']")
EMPTY_CART_BUTTON = (By.CSS_SELECTOR, "a[href*='emptycart']")
CONFIRMATION_EMPTY = (By.CSS_SELECTOR, ".modal-footer .btn-primary")

@given ('Open webstaurant store')
def open_website(context):
    context.driver.get('https://www.webstaurantstore.com')


@when ('Search for {search_text}')
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

@when('Check the search result ensuring every product item has the word {search_word} its title')
def check_titles(context, search_word):
    get_titles = context.driver.find_elements(*TITLES)
    print(len(get_titles))
    for title in get_titles:
        #print(title.text)
        assert search_word in title.text, f"Expected {search_word} in {title.text}"
    sleep(6)


@when ('Add the last of found items to Cart')
def add_last(context):
    get_item_blocks = context.driver.find_elements(*ITEM_BLOCKS)
    last_item_block = get_item_blocks[-1]
    add_to_cart_last = last_item_block.find_element(*ADD_TO_CART)
    add_to_cart_last.click()

    sleep(6)

@then ('Empty Cart')
def empty_cart(context):
    cart = context.driver.find_element(*CART_BUTTON)
    cart.click()
    sleep(3)
    empty_cart_button = context.driver.find_element(*EMPTY_CART_BUTTON)
    empty_cart_button.click()
    sleep(3)
    confirm_empty = context.driver.find_elements(*CONFIRMATION_EMPTY)
    confirm_empty[-1].click()
    sleep(1)