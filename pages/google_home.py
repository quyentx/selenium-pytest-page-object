from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
from utils.test_data import TestData


class HomeLocators:
    STATS = "result-stats"


class GoogleHomePage(PageFactory):
    is_stat_enabled = False

    def __init__(self, driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        super().__init__()
        self.driver = driver

    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "searchBox": ('NAME', 'q'),
        "btnSubmit": ('NAME', 'btnK')
    }

    def search(self):
        # set_text(), click_button() methods are extended methods in PageFactory
        self.searchBox.set_text(TestData.SEARCH_TERM)  # edtUserName become class variable using PageFactory
        self.btnSubmit.click_button()

    def is_stats_loaded(self):
        try:
            self.driver.find_element(By.ID, HomeLocators.STATS)
            return True
        except NoSuchElementException:
            return False

    def get_stats_text(self):
        return self.driver.find_element(By.ID, HomeLocators.STATS).text
