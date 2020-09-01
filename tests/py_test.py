import unittest

from selenium import webdriver

from pages.google_home import GoogleHomePage
from utils.test_base import TestBase


class GoogleSearch(TestBase):
    def test_google_search(self):
        google_home_page = GoogleHomePage(self.driver)
        google_home_page.search()