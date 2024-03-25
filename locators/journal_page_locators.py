from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class JournalPageLocators(BasePageLocators):
    HOME_BUTTON = By.XPATH, "//a[text()='Home']"
