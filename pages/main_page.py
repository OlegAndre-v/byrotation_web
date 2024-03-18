import allure
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators


class MainPage(BasePage):
    @allure.step('Клик по "New In"')
    def click_new_in_button(self):
        self.click_element(BasePageLocators.NEW_IN_BUTTON)

    @allure.step('Переход по выпадающему списку "Designers">"Show all"')
    def click_show_all_designers(self):
        self.mouseover_element(BasePageLocators.DESIGNERS_BUTTON)
        self.click_element(BasePageLocators.SHOW_ALL_BUTTON)

    @allure.step('Переход по выпадающему списку "Collections">"Show all"')
    def click_show_all_collections(self):
        self.mouseover_element(BasePageLocators.COLLECTIONS_BUTTON)
        self.click_element(BasePageLocators.SHOW_ALL_BUTTON)

    @allure.step('Переход по выпадающему списку "Dresses">"Show all"')
    def click_show_all_dresses(self):
        self.mouseover_element(BasePageLocators.DRESSES_BUTTON)
        self.click_element(BasePageLocators.SHOW_ALL_BUTTON)

    @allure.step('Переход по выпадающему списку "Clothing">"Show all"')
    def click_show_all_clothing(self):
        self.mouseover_element(BasePageLocators.CLOTHING_BUTTON)
        self.click_element(BasePageLocators.SHOW_ALL_BUTTON)

    @allure.step('Переход по выпадающему списку "Accessories">"Show all"')
    def click_show_all_accessories(self):
        self.mouseover_element(BasePageLocators.ACCESSORIES_BUTTON)
        self.click_element(BasePageLocators.SHOW_ALL_BUTTON)

    @allure.step('Переход по выпадающему списку "Men">"Show all"')
    def click_show_all_men(self):
        self.mouseover_element(BasePageLocators.MEN_BUTTON)
        self.click_element(BasePageLocators.SHOW_ALL_BUTTON)

    @allure.step('Клик по "Resale"')
    def click_resale_button(self):
        self.click_element(BasePageLocators.RESALE_BUTTON)
