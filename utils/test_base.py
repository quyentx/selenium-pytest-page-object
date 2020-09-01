from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.test_data import TestData


class TestBase:

    driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)
    driver.get(TestData.BASE_URL)

    #
    # def setup(self):
    #     # Setting up how we want Chrome to run
    #     chrome_options = webdriver.ChromeOptions()
    #     self.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH, options=chrome_options)
    #     # browser should be loaded in maximized window
    #     self.driver.maximize_window()
    #
    # # this function performs click on web element whose locator is passed to it.
    # def click(self, by_locator):
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
    #
    # # this function asserts comparison of a web element's text with passed in text.
    # def assert_element_text(self, by_locator, element_text):
    #     web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    #     assert web_element.text == element_text
    #
    # # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    # def enter_text(self, by_locator, text):
    #     return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
    #
    # # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # # web element if it is enabled.
    # def is_enabled(self, by_locator):
    #     return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    #
    # # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # # true or false depending upon its visibility.
    # def is_visible(self, by_locator):
    #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    #     return bool(element)
    #
    # # this function moves the mouse pointer over a web element whose locator has been passed to it.
    # def hover_to(self, by_locator):
    #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    #     ActionChains(self.driver).move_to_element(element).perform()
    #
    # def teardown(self):
    #     # To do the cleanup after test has executed.
    #     self.driver.close()
    #     self.driver.quit()
