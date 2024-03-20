import allure


@allure.story('Тесты куков')
class TestCookies:
    @allure.title('Тест наличия запроса на использования кук')
    def test_cookie_policy(self, main_page):
        main_page.open()
        assert main_page.get_text_cookies() == 'Accept All'
