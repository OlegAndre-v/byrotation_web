import allure
from pages.base_page import BasePage
from locators.collections_page_locators import CollectionsPageLocators


class CollectionsPage(BasePage):
    @allure.step('Собираем текст "Collections"')
    def get_text_collections(self):
        return self.get_text(CollectionsPageLocators.COLLECTIONS_TEXT)
