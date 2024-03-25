from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class PressPageLocators(BasePageLocators):
    PRESS_TEXT = By.XPATH, "//h1[text()='In the Press']"
