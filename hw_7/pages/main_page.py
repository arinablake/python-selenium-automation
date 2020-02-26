from hw_7.pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    ORDERS = (By.XPATH, "//span[@class='nav-line-2'][text()='& Orders']")
    SC_LOCATOR = (By.CSS_SELECTOR, "#nav-cart")
    HAM_MENU = (By.CSS_SELECTOR, "#nav-hamburger-menu")
    AM_LINK = (By.XPATH, "//div[@id='hmenu-content']//ul[@class='hmenu  hmenu-visible']//a[@data-menu-id='3']")
    #(By.CSS_SELECTOR, "#hmenu-content .hmenu-translateX li:nth-child(3) a")

    def open(self):
        self.open_page('https://www.amazon.com')

    def click_link(self):
        self.click(*self.ORDERS)

    def click_icon(self):
        self.click(*self.SC_LOCATOR)

    def click_h_menu(self):
        self.click(*self.HAM_MENU)

    def click_menu_link(self):
        self.click(*self.AM_LINK)


