import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.new_in_page import NewInPage
from pages.designers_page import DesignersPage
from pages.collections_page import CollectionsPage
from pages.dresses_page import DressesPage
from pages.clothing_page import ClothingPage
from pages.accessories_page import AccessoriesPage
from pages.men_page import MenPage
from pages.resale_page import ResalePage
from data import *


@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def main_page(driver):
    url_path = ''
    return MainPage(driver, url_path)


@pytest.fixture(scope='function')
def new_in_page(driver):
    url_path = Url.NEW_IN_PAGE_PATH
    return NewInPage(driver, url_path)


@pytest.fixture(scope='function')
def designers_page(driver):
    url_path = Url.NEW_IN_PAGE_PATH
    return DesignersPage(driver, url_path)


@pytest.fixture(scope='function')
def collections_page(driver):
    url_path = Url.COLLECTIONS_PAGE_PATH
    return CollectionsPage(driver, url_path)


@pytest.fixture(scope='function')
def dresses_page(driver):
    url_path = Url.DRESSES_PAGE_PATH
    return DressesPage(driver, url_path)


@pytest.fixture(scope='function')
def clothing_page(driver):
    url_path = Url.DRESSES_PAGE_PATH
    return ClothingPage(driver, url_path)


@pytest.fixture(scope='function')
def accessories_page(driver):
    url_path = Url.ACCESSORIES_PAGE_PATH
    return AccessoriesPage(driver, url_path)


@pytest.fixture(scope='function')
def men_page(driver):
    url_path = Url.MEN_PAGE_PATH
    return MenPage(driver, url_path)


@pytest.fixture(scope='function')
def resale_page(driver):
    url_path = Url.RESALE_PAGE_PATH
    return ResalePage(driver, url_path)
