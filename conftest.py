from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages.main_page import MainPage
from pages.desks_page import DesksPage
from pages.product_card_page import ProductCardPage
from pages.cart_page import CartPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')

    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()

@pytest.fixture()
def main_page(driver):
    return MainPage(driver)


@pytest.fixture()
def desks_page(driver):
    return DesksPage(driver)

@pytest.fixture()
def product_card_page(driver):
    return ProductCardPage(driver)

@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)
