from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class EmailUsPageLocators(BasePageLocators):
    SUBMIT_REQUEST_TEXT = By.XPATH, "//h1[text()='Submit a request']"
