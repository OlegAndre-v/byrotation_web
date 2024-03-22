from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class FilterPageLocators(BasePageLocators):
    SCROLL = By.XPATH, "//*[@data-test-id='virtuoso-scroller']"
    CATEGORY_BUTTON = By.XPATH, "//h3[text()='Category']"
    PRODUCT_TYPE_BUTTON = By.XPATH, "//h3[text()='Product Type']"
    WOMEN_CHECK_BOX = By.XPATH, "//p[contains(text(), 'Women')]"
    MEN_CHECK_BOX = By.XPATH, "//p[contains(text(), 'Men')]"
    DRESSES_CHECKBOX = By.XPATH, "//p[contains(text(), 'Dresses')]"
    BAGS_CHECKBOX = By.XPATH, "//p[contains(text(), 'Bags')]"
    TOPS_CHECKBOX = By.XPATH, "//p[contains(text(), 'Tops')]"
    COATS_CHECKBOX = By.XPATH, "//p[contains(text(), 'Coats')]"
    WOMEN_LABEL = By.XPATH, "//span[text()='Women']"
    MEN_LABEL = By.XPATH, "//span[text()='Men']"
    BAGS_LABEL = By.XPATH, "//span[text()='Bags']"
    TOPS_LABEL = By.XPATH, "//span[text()='Tops']"
    BAG_CONTAIN = By.XPATH, "//h2[contains(text(), 'Bag')]"
