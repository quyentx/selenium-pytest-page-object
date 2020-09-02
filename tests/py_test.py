from pages.google_home import GoogleHomePage
from utils.test_base import TestBase


class GoogleSearch(TestBase):
    def test_google_search(self):
        google_home_page = GoogleHomePage(self.driver)
        google_home_page.search()
        assert "Khoảng" and "kết quả" in google_home_page.get_stats_text()

    def test_google_search2(self):
        google_home_page = GoogleHomePage(self.driver)
        google_home_page.search()
        assert google_home_page.is_stats_loaded() == True
