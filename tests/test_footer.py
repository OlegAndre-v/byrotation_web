import allure
import pytest
import time

from locators.footer_page_locators import FooterPageLocators

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
