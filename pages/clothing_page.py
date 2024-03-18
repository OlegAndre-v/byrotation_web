import allure
from pages.base_page import BasePage
from locators.clothing_page_locators import ClothingPageLocators


class ClothingPage(BasePage):
    @allure.step('Собираем текст "Women"')
    def get_text_clothing(self):
        return self.get_text(ClothingPageLocators.WOMEN_TEXT)
