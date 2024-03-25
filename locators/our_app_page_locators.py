from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class OurAppPageLocators(BasePageLocators):
    APP_FEATURES_TEXT = By.XPATH, "//h5[text()='App Features:']"
