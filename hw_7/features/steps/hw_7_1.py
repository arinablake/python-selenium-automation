from behave import given, when, then


@given ('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open()

@when ('Click Amazon Orders link')
def click_orders(context):
    context.app.main_page.click_link()

@then ('Verify {expected} page is opened')
def verify_result(context, expected):
    context.app.results_page.verify_result(expected)


@when ('Click on cart icon')
def click_cart(context):
    context.app.main_page.click_icon()



@then ('Verify {expected} text present')
def check_page(context, expected):
    context.app.results_page.check_cart(expected)
