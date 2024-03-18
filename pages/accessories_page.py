import allure
from pages.base_page import BasePage
from locators.accessories_page_locators import AccessoriesPageLocators


class AccessoriesPage(BasePage):
    @allure.step('Собираем текст "Accessories"')
    def get_text_accessories(self):
        return self.get_text(AccessoriesPageLocators.ACCESSORIES_TEXT)
