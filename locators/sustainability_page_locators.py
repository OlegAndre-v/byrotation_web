from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class SustainabilityPageLocators(BasePageLocators):
    SUSTAINABILITY_TEXT = By.XPATH, "//h1[text()='Sustainability']"
