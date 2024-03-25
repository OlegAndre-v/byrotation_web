from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class EventsPageLocators(BasePageLocators):
    EVENTS_TEXT = By.XPATH, "//h1[text()='EVENTS']"
