from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


BESTSELLERS_LOCATOR = (By.CSS_SELECTOR,"#nav-xshop a[href*='bestsellers']")
TABS = (By.CSS_SELECTOR, "#zg_tabs a")
BANNER_TEXT = (By.CSS_SELECTOR, "#zg_banner_text")

# @given('Open Amazon page')
# def open_amazon_help_page(context):
#     context.driver.get('https://www.amazon.com')

@when('Click bestsellers link')
def bestsellers_link(context):
    bestsellers = context.driver.find_element(*BESTSELLERS_LOCATOR)
    bestsellers.click()

    sleep(2)

@when ('Get all tabs')
def get_all_tabs(context):
    context.tab_titles = context.driver.find_elements(*TABS)
    print(*context.tab_titles, sep='\n')
    print(len(context.tab_titles))

@then ('Check 1 tab has matching banner')
def tab_match1(context):
    context.banner_title = context.driver.find_element(*BANNER_TEXT)
    context.tab_titles = context.driver.find_elements(*TABS)
    tab1 = context.tab_titles[0]
    assert tab1.text in context.banner_title.text, f"Expected {tab1.text} in {context.banner_title.text}"

@then ('Check 2 tab has matching banner')
def tab_match2(context):
    context.banner_title = context.driver.find_element(*BANNER_TEXT)
    context.tab_titles = context.driver.find_elements(*TABS)
    tab2 = context.tab_titles[1]
    tab2.click()
    context.banner_title = context.driver.find_element(*BANNER_TEXT)
    context.tab_titles = context.driver.find_elements(*TABS)
    tab2 = context.tab_titles[1]
    assert tab2.text in context.banner_title.text, f"Expected {tab2.text} in {context.banner_title.text}"
    sleep(1)

@then ('Check 3 tab has matching banner')
def tab_match3(context):
    context.banner_title = context.driver.find_element(*BANNER_TEXT)
    context.tab_titles = context.driver.find_elements(*TABS)
    tab3 = context.tab_titles[2]
    tab3.click()
    context.banner_title = context.driver.find_element(*BANNER_TEXT)
    context.tab_titles = context.driver.find_elements(*TABS)
    tab3 = context.tab_titles[2]
    assert tab3.text in context.banner_title.text, f"Expected {tab3.text} in {context.banner_title.text}"

    sleep(1)

@then ('Check 4 tab has matching banner')
def tab_match4(context):
    context.banner_title = context.driver.find_element(*BANNER_TEXT)
    context.tab_titles = context.driver.find_elements(*TABS)
    tab4 = context.tab_titles[3]
    tab4.click()
    context.banner_title = context.driver.find_element(*BANNER_TEXT)
    context.tab_titles = context.driver.find_elements(*TABS)
    tab4 = context.tab_titles[3]
    assert tab4.text in context.banner_title.text, f"Expected {tab4.text} in {context.banner_title.text}"

    sleep(1)

@then ('Check 5 tab has matching banner')
def tab_match5(context):
    context.banner_title = context.driver.find_element(*BANNER_TEXT)
    context.tab_titles = context.driver.find_elements(*TABS)
    tab5 = context.tab_titles[4]
    tab5.click()
    context.banner_title = context.driver.find_element(*BANNER_TEXT)
    context.tab_titles = context.driver.find_elements(*TABS)
    tab5 = context.tab_titles[4]
    assert tab5.text in context.banner_title.text, f"Expected {tab5.text} in {context.banner_title.text}"

    sleep(1)

