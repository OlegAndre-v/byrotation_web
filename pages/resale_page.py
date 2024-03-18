import allure
from pages.base_page import BasePage
from locators.resale_page_locators import ResalePageLocators


class ResalePage(BasePage):
    @allure.step('Собираем текст "Resale"')
    def get_text_resale(self):
        return self.get_text(ResalePageLocators.RESALE_TEXT)
