from behave import given, when, then
from time import sleep

@when ('Click on hamburger menu')
def click_ham_menu(context):
    context.app.main_page.click_h_menu()

@when ('Click on Amazon Music menu item')
def click_cart(context):
    context.app.main_page.click_menu_link()
    sleep(3)

@then ('{num} menu items are present')
def verify_list_number(context, num):
    context.app.results_page.check_number(num)

