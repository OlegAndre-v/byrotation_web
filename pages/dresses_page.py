import allure
from pages.base_page import BasePage
from locators.dresses_page_locators import DressesLocators


class DressesPage(BasePage):
    @allure.step('Собираем текст "Dresses"')
    def get_text_dresses(self):
        return self.get_text(DressesLocators.DRESSES_TEXT)
