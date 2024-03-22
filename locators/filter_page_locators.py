from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class FilterPageLocators(BasePageLocators):
    SCROLL = By.XPATH, '//*[@data-test-id="virtuoso-scroller"]'
    CATEGORY_BUTTON = By.XPATH, "//h3[text()='Category']"
    WOMEN_CHECK_BOX = By.XPATH, "//p[contains(text(), 'Women')]"
    MEN_CHECK_BOX = By.XPATH, "//p[contains(text(), 'Men')]"
    PRODUCT_TYPE_BUTTON = By.XPATH, "//h3[text()='Product Type']"
    DRESSES_CHECKBOX = By.XPATH, "//p[contains(text(), 'Dresses')]"
    BAGS_CHECKBOX = By.XPATH, "//p[contains(text(), 'Bags')]"
    COATS_CHECKBOX = By.XPATH, "//p[contains(text(), 'Coats')]"
