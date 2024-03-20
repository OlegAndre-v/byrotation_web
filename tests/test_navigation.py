import allure
from data import *
from locators.base_page_locators import BasePageLocators


@allure.story('Тесты переходов по разделам сайта')
class TestNavigation:
    @allure.title('Тест перехода в раздел "New In"')
    def test_navigate_to_new_in(self, driver, main_page, new_in_page):
        main_page.open()
        main_page.click_new_in_button()
        assert (main_page.get_url() == Url.BASE_PAGE + Url.NEW_IN_PAGE_PATH
                and new_in_page.get_text_new_in() == 'New In')

    @allure.title('Тест перехода в раздел "Designers" > "Show all"')
    def test_navigate_to_designers(self, driver, main_page, designers_page):
        main_page.open()
        main_page.accept_cookies()
        main_page.click_show_all_designers()
        assert (main_page.get_url() == Url.BASE_PAGE + Url.DESIGNERS_PAGE_PATH
                and designers_page.get_text_designers() == 'Designers')

    @allure.title('Тест перехода в раздел "Collections" > "Show all"')
    def test_navigate_to_collections(self, driver, main_page, collections_page):
        main_page.open()
        main_page.click_show_all_collections()
        assert (main_page.get_url() == Url.BASE_PAGE + Url.COLLECTIONS_PAGE_PATH
                and collections_page.get_text_collections() == 'Collections')

    @allure.title('Tecт перехода в раздел "Dresses" > "Show all"')
    def test_navigate_to_dresses(self, driver, main_page, dresses_page):
        main_page.open()
        main_page.click_show_all_dresses()
        assert (main_page.get_url() == Url.BASE_PAGE + Url.DRESSES_PAGE_PATH
               and dresses_page.get_text_dresses() == 'Dresses')

    @allure.title('Tecт перехода в раздел "Clothing" > "Show all"')
    def test_navigate_to_clothing(self, driver, main_page, clothing_page):
        main_page.open()
        main_page.accept_cookies()
        main_page.click_show_all_clothing()
        assert (main_page.get_url() == Url.BASE_PAGE + Url.CLOTHING_PAGE_PATH
               and clothing_page.get_text_clothing() == 'Women')

    @allure.title('Tecт перехода в раздел "Accessories" > "Show all"')
    def test_navigate_to_accessories(self, driver, main_page, accessories_page):
        main_page.open()
        main_page.click_show_all_accessories()
        assert (main_page.get_url() == Url.BASE_PAGE + Url.ACCESSORIES_PAGE_PATH
               and accessories_page.get_text_accessories() == 'Accessories')

    @allure.title('Tecт перехода в раздел "Men" > "Show all"')
    def test_navigate_to_men(self, driver, main_page, men_page):
        main_page.open()
        main_page.click_show_all_men()
        assert (main_page.get_url() == Url.BASE_PAGE + Url.MEN_PAGE_PATH
               and men_page.get_text_men() == 'Men')

    @allure.title('Tecт перехода в раздел "Resale"')
    def test_navigate_to_resale(self, driver, main_page, resale_page):
        main_page.open()
        main_page.click_resale_button()
        assert (main_page.get_url() == Url.BASE_PAGE + Url.RESALE_PAGE_PATH
               and resale_page.get_text_resale() == 'Second Hand Designer Dresses & Accessories')

    @allure.title('Тест перехода на mainpage по клику logo')
    def test_navigate_to_main(self, new_in_page):
        new_in_page.open()
        new_in_page.click_element(BasePageLocators.BY_ROTATION_LOGO)
        assert new_in_page.get_url() == Url.BASE_PAGE
