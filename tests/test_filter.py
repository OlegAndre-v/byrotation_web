import allure
import pytest
import time
from data import *
from locators.filter_page_locators import FilterPageLocators
from locators.search_page_locators import SearchPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@allure.story('Тесты фильтров')
class TestFilter:
    # @allure.title('Тест фильтра "Category"')
    # @pytest.mark.parametrize('category, result, label',
    #                          [[FilterPageLocators.WOMEN_CHECK_BOX, 'Women', FilterPageLocators.WOMEN_LABEL],
    #                           [FilterPageLocators.MEN_CHECK_BOX, 'Men', FilterPageLocators.MEN_LABEL]
    #                           ])
    # def test_category_filter(self, driver, new_in_page, category, result, label):
    #     new_in_page.open()
    #     new_in_page.click_element(FilterPageLocators.CATEGORY_BUTTON)
    #     new_in_page.click_element(category)
    #     assert result in driver.current_url and result == new_in_page.get_text(label)

    @allure.title('Тест фильтра "Product Type"')
    def test_product_type_filter(self, driver, new_in_page):
        new_in_page.open()
        new_in_page.click_element(FilterPageLocators.PRODUCT_TYPE_BUTTON)
        new_in_page.click_element(FilterPageLocators.BAGS_CHECKBOX)
        new_in_page.accept_cookies()
        assert ('Bags' == new_in_page.get_text(FilterPageLocators.BAGS_LABEL)
                and 'Bag' in new_in_page.get_text(SearchPageLocators.ITEM_INFO))
