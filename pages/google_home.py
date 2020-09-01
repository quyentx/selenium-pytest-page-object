from seleniumpagefactory.Pagefactory import PageFactory
from utils.test_data import TestData


class GoogleHomePage(PageFactory):

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
