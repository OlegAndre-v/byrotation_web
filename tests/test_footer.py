import allure
import pytest

from data import *
import time

from locators.footer_page_locators import FooterPageLocators
from locators.journal_page_locators import JournalPageLocators
from locators.community_page_locators import CommunityPageLocators
from locators.our_story_page_locators import OurStoryPageLocators
from locators.charity_page_locators import CharityPageLocators
from locators.events_page_locators import EventsPageLocators
from locators.gift_card_page_locators import GiftCardPageLocators
from locators.how_it_works_page_locators import HowItWorksPageLocators
from locators.sustainability_page_locators import SustainabilityPageLocators
from locators.press_page_locators import PressPageLocators
from locators.our_app_page_locators import OurAppPageLocators
from locators.mailer_bags_page_locators import MailerBagsPageLocators
from locators.tote_bag_page_locators import ToteBagPageLocators
from locators.faq_page_locators import FAQPageLocators
from locators.email_us_page_locators import EmailUsPageLocators

@allure.story('Тесты футера')
class TestFooter:

    # Не к чему привязаться
    # @allure.title('Тест кнопки ЭплСтор')
    # def test_appstore_button(self, driver, main_page):
    #     main_page.open()
    #     main_page.accept_cookies()
    #     main_page.go_to_footer()
    #     time.sleep(5)
    #     main_page.click_element(FooterPageLocators.APP_STORE_BUTTON)
    #     time.sleep(5)
    # @allure.title('Тест перехода в "Journal"')
    # def test_journal_navigation(self, driver, main_page):
    #     main_page.open()
    #     main_page.accept_cookies()
    #     main_page.go_to_footer()
    #     main_page.click_element(FooterPageLocators.JOURNAL_BUTTON)
    #     assert driver.current_url == Url.JOURNAL_PAGE and main_page.get_text(JournalPageLocators.HOME_BUTTON) == 'Home'

    # @allure.title('Тест перехода в "The Community"')
    # def test_community_navigation(self, driver, main_page):
    #     main_page.open()
    #     main_page.accept_cookies()
    #     main_page.go_to_footer()
    #     main_page.click_element(FooterPageLocators.THE_COMMUNITY_BUTTON)
    #     main_page.find_element(CommunityPageLocators.WHAT_ROTATORS_SAYING_TEXT)
    #     assert (driver.current_url == Url.BASE_PAGE + Url.COMMUNITY_PAGE_PATH
    #             and main_page.get_text(CommunityPageLocators.WHAT_ROTATORS_SAYING_TEXT) == 'What our Rotators are Saying')

    # @allure.title('Тест перехода в "Our Story"')
    # def test_our_story_navigation(self, driver, main_page):
    #     main_page.open()
    #     main_page.accept_cookies()
    #     main_page.go_to_footer()
    #     main_page.click_element(FooterPageLocators.OUR_STORY_BUTTON)
    #     main_page.find_element(OurStoryPageLocators.ABOUT_US_TEXT)
    #     assert (driver.current_url == Url.BASE_PAGE + Url.OUR_STORY_PAGE_PATH
    #             and main_page.get_text(OurStoryPageLocators.ABOUT_US_TEXT) == 'About Us')

    # @allure.title('Тест перехода в "Charity"')
    # def test_charity_navigation(self, driver, main_page):
    #     main_page.open()
    #     main_page.accept_cookies()
    #     main_page.go_to_footer()
    #     main_page.click_element(FooterPageLocators.CHARITY_BUTTON)
    #     main_page.find_element(CharityPageLocators.CHARITY_TEXT)
    #     assert (driver.current_url == Url.BASE_PAGE + Url.CHARITY_PAGE_PATH
    #             and main_page.get_text(CharityPageLocators.CHARITY_TEXT) == 'Charity')

    # @allure.title('Тест перехода в "Events"')
    # def test_events_navigation(self, driver, main_page):
    #     main_page.open()
    #     main_page.accept_cookies()
    #     main_page.go_to_footer()
    #     main_page.click_element(FooterPageLocators.EVENTS_BUTTON)
    #     main_page.find_element(EventsPageLocators.EVENTS)
    #     assert (driver.current_url == Url.BASE_PAGE + Url.EVENTS_PAGE_PATH
    #             and main_page.get_text(EventsPageLocators.EVENTS) == 'EVENTS')

    # @allure.title('Тест перехода в "Gift Card"')
    # def test_gift_card_navigation(self, driver, main_page):
    #     main_page.open()
    #     main_page.accept_cookies()
    #     main_page.go_to_footer()
    #     main_page.click_element(FooterPageLocators.GIFT_CARD_BUTTON)
    #     main_page.find_element(GiftCardPageLocators.GIVE_GIFT_TEXT)
    #     assert (driver.current_url == Url.BASE_PAGE + Url.GIFT_CARD_PAGE_PATH
    #             and main_page.get_text(GiftCardPageLocators.GIVE_GIFT_TEXT) == 'Give The Gift of Rotating')

    # @allure.title('Тест перехода в "How it works"')
    # def test_how_it_works_navigation(self, driver, main_page):
    #     main_page.open()
    #     main_page.accept_cookies()
    #     main_page.go_to_footer()
    #     main_page.click_element(FooterPageLocators.HOW_IT_WORKS_BUTTON)
    #     main_page.find_element(HowItWorksPageLocators.HOW_IT_WORKS_TEXT)
    #     assert (driver.current_url == Url.BASE_PAGE + Url.HOW_IT_WORKS_PAGE_PATH
    #             and main_page.get_text(HowItWorksPageLocators.HOW_IT_WORKS_TEXT) == 'How it Works')

    # @allure.title('Тест перехода в "Sustainability"')
    # def test_sustainability_navigation(self, driver, main_page):
    #     main_page.open()
    #     main_page.accept_cookies()
    #     main_page.go_to_footer()
    #     main_page.click_element(FooterPageLocators.SUSTAINABILITY_BUTTON)
    #     main_page.find_element(SustainabilityPageLocators.SUSTAINABILITY_TEXT)
    #     assert (driver.current_url == Url.BASE_PAGE + Url.SUSTAINABILITY_PAGE_PATH
    #             and main_page.get_text(SustainabilityPageLocators.SUSTAINABILITY_TEXT) == 'Sustainability')

    @allure.title('Тест перехода в "Press"')
    def test_how_it_works_navigation(self, driver, main_page):
        main_page.open()
        main_page.accept_cookies()
        main_page.go_to_footer()
        main_page.click_element(FooterPageLocators.PRESS_BUTTON)
        main_page.find_element(PressPageLocators.PRESS_TEXT)
        assert (driver.current_url == Url.BASE_PAGE + Url.PRESS_PAGE_PATH
                and main_page.get_text(PressPageLocators.PRESS_TEXT) == 'In the Press')
