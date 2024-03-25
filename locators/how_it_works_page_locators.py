from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class HowItWorksPageLocators(BasePageLocators):
    HOW_IT_WORKS_TEXT = By.XPATH, "//h1[text()='How it Works']"
