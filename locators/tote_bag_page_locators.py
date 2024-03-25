from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class ToteBagPageLocators(BasePageLocators):
    WHATS_MINE_TEXT = By.XPATH, "//h1[text()='What’s Mine Is Yours Tote Bag']"
