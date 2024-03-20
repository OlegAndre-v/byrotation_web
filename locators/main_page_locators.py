from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class MainPageLocators(BasePageLocators):
    SEARCH_INPUT = By.XPATH, "//input[@type='search']"
