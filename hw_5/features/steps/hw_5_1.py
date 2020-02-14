from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

COLOR_BUTTON_LOCATOR = (By.CSS_SELECTOR, '#variation_color_name ul[role="radiogroup"] li')
COLOR_TITLE_LOCATOR = (By.CSS_SELECTOR, '#variation_color_name .selection')
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-button')
BRIGHT_WHITE = (By.CSS_SELECTOR, '#color_name_20')

@given('Open Amazon sheets page')
def open_amazon_sheets_page(context):
    context.driver.get('https://www.amazon.com/AmazonBasics-Microfiber-Sheet-Set-Queen/dp/B00Q7O9OIM')

@when ('Get all sheets colors')
def get_all_sheets_colors(context):
    context.sheets_colors = context.driver.find_elements(*COLOR_BUTTON_LOCATOR)


@when ('Check every color has matching description')
def color_description(context):
    context.color_title = context.driver.find_element(*COLOR_TITLE_LOCATOR)
    for sheets_color in context.sheets_colors:
        sheets_color.click()
        print(context.color_title.text)
        print(sheets_color.get_attribute('title'))
        assert context.color_title.text in sheets_color.get_attribute('title'), f"Expected {context.color_title.text} in {sheets_color.get_attribute('title')}"

@when ('User chooses {selected_color} color')
def select_color(context, selected_color):
    for sheets_color in context.sheets_colors:
        if selected_color in sheets_color.get_attribute('title'):
            sheets_color.click()
            break

        sleep(2)

@when ('Add an item to shopping cart')
def add_item_to_cart(context):
    add_to_cart_button = context.driver.find_element(*ADD_TO_CART_BUTTON)
    add_to_cart_button.click()

    sleep(2)
#
#

# #
# @when ('See pop up 2')
# def see_pop_up(context):
#     pop_up_locator_2 = context.driver.find_elements(*POP_UP_LOCATOR_2)
#     context.pop_up_2 = len(pop_up_locator_2) > 0
#     sleep(2)
#
# @when ('Close pop up 2')
# def pop_up(context):
#     if context.pop_up_2 == True:
#         close_pop_up_2 = context.driver.find_element(*CLOSE_POP_UP_2)
#         close_pop_up_2.click()
#     sleep(2)


  # # if context.color_title.text == str('Bright White'):
    # for sheets_color in context.sheets_colors:
    #     sheets_color.click()
    #     selected_item_icon = context.driver.find_elements(*BRIGHT_WHITE)
    #     print(selected_item_icon)
    #     selected_item_icon.click()
    # for sheets_color in context.sheets_colors:
    #     if select_color == context.color_title.text:
    #         selected_item_icon = context.sheets_colors.find_elements(*BRIGHT_WHITE)
    #         selected_item_icon.click()

# @when ('The color Bright white - add to shopping cart')
# def add_sheets(context):
#      sheets_color = 'Bright white'
#      context.execute_steps(f'when Add an item to shopping cart')

# @when ('Click the item link')
# def choose_item(context):
#     selected_item = context.driver.find_element(*RANDOM_ITEM)
#     selected_item.click()
#
#     sleep(2)