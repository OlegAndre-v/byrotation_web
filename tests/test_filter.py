import allure
import pytest
import time
from data import *
from locators.filter_page_locators import FilterPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@allure.story('Тесты фильтров')
class TestFilter:
    # @allure.title('Тест фильтра "Category"')
    # @pytest.mark.parametrize('category, result', [[FilterPageLocators.WOMEN_CHECK_BOX, 'Women'],
    #                                               [FilterPageLocators.MEN_CHECK_BOX, 'Men']])
    # def test_category_filter(self, driver, new_in_page, category, result):
    #     new_in_page.open()
    #     new_in_page.click_element(FilterPageLocators.CATEGORY_BUTTON)
    #     new_in_page.click_element(category)
    #     assert result in driver.current_url
    @allure.title('Тест фильтра "Product Type"')
    def test_product_type_filter(self, driver, new_in_page):
        new_in_page.open()
        new_in_page.click_element(FilterPageLocators.PRODUCT_TYPE_BUTTON)
        time.sleep(1)
        element = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[3]/div/div[3]/div')
        driver.execute_script("arguments[0].scrollBy(0, 100);", element)
        time.sleep(3)

