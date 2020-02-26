from hw_7.pages.main_page import MainPage
from hw_7.pages.results_page import ResultsPage

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.results_page = ResultsPage(self.driver)
