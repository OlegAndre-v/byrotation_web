import allure
import pytest

from data import *
from locators.main_page_locators import MainPageLocators
from locators.search_page_locators import SearchPageLocators


@allure.story('Тесты поиска')
class TestSearch:
    @allure.title('Тест поиска по бренду')
    @pytest.mark.parametrize('brand', [TDSearch.BRAND_1, TDSearch.BRAND_2, TDSearch.BRAND_3,
                                       TDSearch.BRAND_4, TDSearch.BRAND_5])
    def test_search_for_brand(self, driver, main_page, brand):
        main_page.open()
        main_page.accept_cookies()
        main_page.send_input(MainPageLocators.SEARCH_INPUT, brand)
        main_page.send_enter(MainPageLocators.SEARCH_INPUT)
        assert main_page.get_text(SearchPageLocators.ITEM_INFO) == brand

    @allure.title('Тест поиска по типу продукта')
    @pytest.mark.parametrize('product_type', [TDSearch.PRODUCT_TYPE_1, TDSearch.PRODUCT_TYPE_2, TDSearch.PRODUCT_TYPE_3])
    def test_search_for_product_type(self, driver, main_page, product_type):
        main_page.open()
        main_page.accept_cookies()
        main_page.send_input(MainPageLocators.SEARCH_INPUT, product_type)
        main_page.send_enter(MainPageLocators.SEARCH_INPUT)
        assert product_type in main_page.get_text(SearchPageLocators.ITEM_INFO)

    @allure.title('Тест поиска по цвету продукта')
    @pytest.mark.parametrize('colour', [TDSearch.PRODUCT_COLOUR_1, TDSearch.PRODUCT_COLOUR_2, TDSearch.PRODUCT_COLOUR_3])
    def test_search_for_colour(self, driver, main_page, colour):
        main_page.open()
        main_page.accept_cookies()
        main_page.send_input(MainPageLocators.SEARCH_INPUT, colour)
        main_page.send_enter(MainPageLocators.SEARCH_INPUT)
        assert (colour in main_page.get_text(SearchPageLocators.ITEM_INFO) or
                colour in main_page.get_text(SearchPageLocators.BRAND_NAME))
