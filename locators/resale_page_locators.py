from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class ResalePageLocators(BasePageLocators):
    RESALE_TEXT = (By.XPATH, "//h1[text()='Second Hand Designer Dresses & Accessories']")
