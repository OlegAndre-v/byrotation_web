from selenium.webdriver.common.by import By


class BasePageLocators:
    BY_ROTATION_LOGO = (By.XPATH, "//div[@class='MuiBox-root css-1q6tf9f']")
    ACCEPT_ALL_COOKIES_BUTTON = (By.CSS_SELECTOR, "[data-testid='uc-accept-all-button']")
    NEW_IN_BUTTON = (By.XPATH, "//a[text()='New In']")
    DESIGNERS_BUTTON = (By.XPATH, "//h3[text()='Designers']")
    COLLECTIONS_BUTTON = (By.XPATH, "//h3[text()='Collections']")
    DRESSES_BUTTON = (By.XPATH, "//h3[text()='Dresses']")
    CLOTHING_BUTTON = (By.XPATH, "//h3[text()='Clothing']")
    ACCESSORIES_BUTTON = (By.XPATH, "//h3[text()='Accessories']")
    MEN_BUTTON = (By.XPATH, "//h3[text()='Men']")
    RESALE_BUTTON = (By.XPATH, "//a[text()='Resale']")
    SHOW_ALL_BUTTON = (By.XPATH, "//p[text()='Show All']")
