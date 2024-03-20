from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class FilterPageLocators(BasePageLocators):
    CATEGORY_BUTTON = By.XPATH, "//h3[text()='Category']"
    WOMEN_CHECK_BOX = By.XPATH, "(//div[@role='button'])[2]"
    MEN_CHECK_BOX = By.XPATH, "(//div[@role='button'])[3]"
