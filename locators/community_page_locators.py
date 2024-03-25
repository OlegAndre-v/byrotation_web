from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class CommunityPageLocators(BasePageLocators):
    WHAT_ROTATORS_SAYING_TEXT = By.XPATH, "//h4[text()='What our Rotators are Saying']"
