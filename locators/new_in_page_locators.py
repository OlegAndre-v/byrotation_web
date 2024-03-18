from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class NewInPageLocators(BasePageLocators):
    NEW_IN_TEXT = (By.XPATH, "//h1[text()='New In']")
