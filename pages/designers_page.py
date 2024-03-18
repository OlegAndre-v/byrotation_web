import allure
from pages.base_page import BasePage
from locators.designers_page_locators import DesignersPageLocators


class DesignersPage(BasePage):
    @allure.step('Собираем текст "Designers"')
    def get_text_designers(self):
        return self.get_text(DesignersPageLocators.DESIGNERS_TEXT)
