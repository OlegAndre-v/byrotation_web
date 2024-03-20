import allure
import pytest
import time
from data import *
from locators.filter_page_locators import FilterPageLocators


@allure.story('Тесты фильтров')
class TestFilter:
    @allure.title('Тест фильтра "Category"')
    @pytest.mark.parametrize('category, result', [[FilterPageLocators.WOMEN_CHECK_BOX, 'Women'],
                                                  [FilterPageLocators.MEN_CHECK_BOX, 'Men']])
    def test_category_filter(self, driver, new_in_page, category, result):
        new_in_page.open()
        new_in_page.click_element(FilterPageLocators.CATEGORY_BUTTON)
        new_in_page.click_element(category)
        assert result in driver.current_url
