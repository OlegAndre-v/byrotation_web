import allure
import pytest


from locators.filter_page_locators import FilterPageLocators
from locators.search_page_locators import SearchPageLocators


@allure.story('Тесты фильтров')
class TestFilter:
    @allure.title('Тест фильтра "Category"')
    @pytest.mark.parametrize('category, result, label',
                             [[FilterPageLocators.WOMEN_CHECK_BOX, 'Women', FilterPageLocators.WOMEN_LABEL],
                              [FilterPageLocators.MEN_CHECK_BOX, 'Men', FilterPageLocators.MEN_LABEL]
                              ])
    def test_category_filter(self, driver, new_in_page, category, result, label):
        new_in_page.open()
        new_in_page.click_element(FilterPageLocators.CATEGORY_BUTTON)
        new_in_page.click_element(category)
        assert result in driver.current_url and result == new_in_page.get_text(label)

    @allure.title('Тест фильтра "Product Type"')
    def test_product_type_filter(self, driver, new_in_page):
        new_in_page.open()
        new_in_page.click_element(FilterPageLocators.PRODUCT_TYPE_BUTTON)
        new_in_page.click_element(FilterPageLocators.BAGS_CHECKBOX)
        new_in_page.wait_for_text_to_change(SearchPageLocators.ITEM_INFO)
        assert ('Bags' == new_in_page.get_text(FilterPageLocators.BAGS_LABEL)
                and 'Bag' in new_in_page.get_text(SearchPageLocators.ITEM_INFO))

    @allure.title('Тест фильтра "Brand"')
    def test_brand_filter(self, driver, new_in_page):
        new_in_page.open()
        new_in_page.click_element(FilterPageLocators.BRAND_BUTTON)
        new_in_page.click_element(FilterPageLocators.RIXO_CHECKBOX)
        new_in_page.wait_for_text_to_change(SearchPageLocators.ITEM_INFO)
        assert ('Rixo' == new_in_page.get_text(FilterPageLocators.RIXO_LABEL)
                and 'Rixo' == new_in_page.get_text(SearchPageLocators.BRAND_NAME))

    @allure.title('Тест фильтра "Subcategory"')
    def test_subcategory_filter(self, driver, new_in_page):
        new_in_page.open()
        new_in_page.click_element(FilterPageLocators.PRODUCT_TYPE_BUTTON)
        new_in_page.click_element(FilterPageLocators.BAGS_CHECKBOX)
        new_in_page.accept_cookies()
        new_in_page.click_element(FilterPageLocators.SUBCATEGORY_BUTTON)
        new_in_page.click_element(FilterPageLocators.HANDBAG_CHECKBOX)
        assert 'Handbags' == new_in_page.get_text(FilterPageLocators.HANDBAG_LABEL)

    @allure.title('Тест фильтра "Size"')
    def test_size_filter(self, driver, new_in_page):
        new_in_page.open()
        new_in_page.click_element(FilterPageLocators.SIZE_BUTTON)
        new_in_page.click_element(FilterPageLocators.SIZE_4_CHECKBOX)
        new_in_page.accept_cookies()
        new_in_page.wait_for_text_to_change(SearchPageLocators.ITEM_INFO)
        assert ('UK4' == new_in_page.get_text(FilterPageLocators.SIZE_4_LABEL)
                and 'UK 4' in new_in_page.get_text(SearchPageLocators.ITEM_INFO))

    @allure.title('Тест фильтра "Colour"')
    def test_colour_filter(self, driver, new_in_page):
        new_in_page.open()
        new_in_page.click_element(FilterPageLocators.COLOUR_BUTTON)
        new_in_page.click_element(FilterPageLocators.BLACK_CHECKBOX)
        new_in_page.accept_cookies()
        new_in_page.wait_for_text_to_change(SearchPageLocators.ITEM_INFO)
        assert ('Black' == new_in_page.get_text(FilterPageLocators.BLACK_LABEL)
                and 'Black' in new_in_page.get_text(SearchPageLocators.ITEM_INFO))

    @allure.title('Тест фильтра "Collection"')
    def test_collection_filter(self, driver, new_in_page):
        new_in_page.open()
        new_in_page.accept_cookies()
        new_in_page.click_element(FilterPageLocators.COLLECTION_BUTTON)
        new_in_page.click_element(FilterPageLocators.WEDDING_GUEST_CHECKBOX)
        new_in_page.wait_for_text_to_change(SearchPageLocators.ITEM_INFO)
        assert ('Wedding Guest' == new_in_page.get_text(FilterPageLocators.WEDDING_GUEST_LABEL)
                and 'Wedding Guest' == new_in_page.get_text(FilterPageLocators.WEDDING_GUEST_PHOTO_LABEL))

    @allure.title('Тест фильтра "Price Per Day"')
    def test_price_filter(self, driver, new_in_page):
        new_in_page.open()
        new_in_page.accept_cookies()
        new_in_page.click_element(FilterPageLocators.PRICE_PER_DAY_BUTTON)
        new_in_page.click_element(FilterPageLocators.MIN_BUTTON)
        new_in_page.click_element(FilterPageLocators.MIN_INPUT)
        new_in_page.send_input(FilterPageLocators.MIN_INPUT, 5)
        assert '25' in driver.current_url

    @allure.title('Тест фильтра "Postage"')
    def test_postage_filter(self, driver, new_in_page):
        new_in_page.open()
        new_in_page.accept_cookies()
        new_in_page.click_element(FilterPageLocators.POSTAGE_BUTTON)
        assert 'postageAvailable' in driver.current_url

    @allure.title('Тест фильтра "Resale"')
    def test_resale_filter(self, driver, new_in_page):
        new_in_page.open()
        new_in_page.accept_cookies()
        new_in_page.click_element(FilterPageLocators.RESALE_BUTTON)
        assert 'resaleAvailable' in driver.current_url
