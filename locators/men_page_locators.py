from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class MenPageLocators(BasePageLocators):
    MEN_TEXT = (By.XPATH, "//h1[text()='Men']")