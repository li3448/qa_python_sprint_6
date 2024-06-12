from selenium import webdriver
import pytest
from test_page_object.data import MAIN_URL
from test_page_object.pages.main_page import MainPage
from test_page_object.pages.order_page import OrderPage

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.get(MAIN_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)


@pytest.fixture(scope='function')
def order_page(driver):
    return OrderPage(driver)


