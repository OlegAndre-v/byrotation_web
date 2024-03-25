from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class FooterPageLocators(BasePageLocators):
    APP_STORE_BUTTON = By.XPATH, "//*[@id='appleStore_button']/svg/path[2]"
    JOURNAL_BUTTON = By.XPATH, "//p[text()='Journal']"
    THE_COMMUNITY_BUTTON = By.XPATH, "//p[text()='The Community']"
    OUR_STORY_BUTTON = By.XPATH, "//p[text()='Our Story']"
    CHARITY_BUTTON = By.XPATH, "//p[text()='Charity']"
    EVENTS_BUTTON = By.XPATH, "//p[text()='Events']"
    GIFT_CARD_BUTTON = By.XPATH, "//p[text()='Gift Card']"
    HOW_IT_WORKS_BUTTON = By.XPATH, "//p[text()='How It Works']"
    SUSTAINABILITY_BUTTON = By.XPATH, "//p[text()='Sustainability']"
    PRESS_BUTTON = By.XPATH, "//p[text()='Press']"
    OUR_APP_BUTTON = By.XPATH, "//p[text()='Our App']"
    MAILER_BAGS_BUTTON = By.XPATH, "//p[text()='Mailer Bags']"
    TOTE_BAG_BUTTON = By.XPATH, "//p[text()='Tote Bag']"
    FAQ_BUTTON = By.XPATH, "//p[text()='FAQ']"
    EMAIL_US_BUTTON = By.XPATH, "//p[text()='Email Us']"
