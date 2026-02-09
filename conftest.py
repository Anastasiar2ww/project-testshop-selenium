from selenium import webdriver
import pytest
from pages.main_page import MainPage
from pages.desks_page import DesksPage
from pages.product_card_page import ProductCardPage
from pages.cart_page import CartPage


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
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
