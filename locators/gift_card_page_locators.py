from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class GiftCardPageLocators(BasePageLocators):
    GIVE_GIFT_TEXT = By.XPATH, "//h1[text()='Give The Gift of Rotating ']"
