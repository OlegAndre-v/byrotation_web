from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class AccessoriesPageLocators(BasePageLocators):
    ACCESSORIES_TEXT = (By.XPATH, "//h1[text()='Accessories']")