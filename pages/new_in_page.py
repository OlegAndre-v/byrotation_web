import allure
from pages.base_page import BasePage
from locators.new_in_page_locators import NewInPageLocators


class NewInPage(BasePage):
    @allure.step('Собираем текст "New in"')
    def get_text_new_in(self):
        return self.get_text(NewInPageLocators.NEW_IN_TEXT)
