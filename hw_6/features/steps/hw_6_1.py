from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

ACTIVE_ITEMS_LOCATOR = (By.CSS_SELECTOR, '#activeCartViewForm div[data-name="Active Items"]')
BLOG_LINK = (By.XPATH, "//div[@id='main-content']//a[text()='Learn more on our blog']")
ITEM_LOCATOR = (By.CSS_SELECTOR, "#desktop-2 div.feed-carousel div li:nth-child(3)")
SC_LOCATOR = (By.CSS_SELECTOR, "#nav-cart")
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-button')


@given('Open Amazon page')
def open_amazon_help_page(context):
    context.driver.get('https://www.amazon.com')


@when('Store original windows')
def store_original_window(context):
    context.init_window = context.driver.current_window_handle
    print(context.init_window)
    sleep(3)


@when('Click to item link')
def item_link_click(context):
    actions = ActionChains(context.driver)
    item_link = context.driver.find_element(*ITEM_LOCATOR)
    actions.key_down(Keys.COMMAND).click(item_link).key_up(Keys.COMMAND).perform()

    sleep(2)

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.all_windows = context.driver.window_handles
    context.driver.switch_to.window(context.all_windows[-1])
    sleep(3)


@when('Add an item to shopping cart')
def add_item_to_cart(context):
    add_to_cart_button = context.driver.find_element(*ADD_TO_CART_BUTTON)
    add_to_cart_button.click()

    sleep(2)


@when('User can close new window and switch back to original')
def go_back_to_origin_window(context):
    new_window = context.driver.current_window_handle
    context.driver.close()
    context.driver.switch_to.window(context.init_window)
    sleep(2)


@when('User refreshes the page')
def refresh(context):
    context.driver.refresh()
    sleep(2)


@when('Click Shopping cart button')
def click_sc_button(context):
    amazon_sc_button = context.driver.find_element(*SC_LOCATOR)
    amazon_sc_button.click()
    sleep(2)


@then('Shopping cart has {num} item')
def check_item_page(context, num):
    active_items_num = context.driver.find_elements(*ACTIVE_ITEMS_LOCATOR)
    assert (len(active_items_num)) == int(num), f'Expected {num}, but got {len(active_items_num)}'
    sleep(2)
