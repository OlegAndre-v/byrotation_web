import allure
from pages.base_page import BasePage
from locators.men_page_locators import MenPageLocators


class MenPage(BasePage):
    @allure.step('Собираем текст "Men"')
    def get_text_men(self):
        return self.get_text(MenPageLocators.MEN_TEXT)