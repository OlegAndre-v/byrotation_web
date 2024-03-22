from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class FooterPageLocators(BasePageLocators):
    APP_STORE_BUTTON = By.XPATH, '//*[@id="appleStore_button"]/svg/path[2]'
