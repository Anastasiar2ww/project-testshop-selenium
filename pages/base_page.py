from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    base_url = 'http://testshop.qa-practice.com/'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def get_text(self, locator: tuple):
        return self.driver.find_element(*locator).text

    def wait_until_visible(self, locator: tuple,
                           timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(locator))

    def wait_for_value_in_element(self, locator: tuple,
                                  value: str,
                                  timeout=10):

        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.text_to_be_present_in_element_value(locator, value))

    def wait_for_text_in_element(self, locator: tuple,
                                 text: str,
                                 timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.text_to_be_present_in_element(locator, text))