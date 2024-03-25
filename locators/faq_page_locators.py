from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class FAQPageLocators(BasePageLocators):
    FOR_LENDERS_BUTTON = By.XPATH, "//span[text()='For Lenders']"
