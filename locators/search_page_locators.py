from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class SearchPageLocators(BasePageLocators):
    BRAND_NAME = By.XPATH, "//h2[@class='MuiTypography-root MuiTypography-body1 css-19ugv2d']"
    ITEM_INFO = By.XPATH, "//h2[@class='MuiTypography-root MuiTypography-body1 css-3tuih8']"
