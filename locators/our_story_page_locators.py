from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class OurStoryPageLocators(BasePageLocators):
    ABOUT_US_TEXT = By.XPATH, "//h2[text()='About Us']"
