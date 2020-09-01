from pages.google_home import GoogleHomePage
from utils.test_base import TestBase


def test_google_search():
    googleHomePage = GoogleHomePage(TestBase.driver)
    googleHomePage.search()
