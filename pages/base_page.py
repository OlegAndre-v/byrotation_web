import allure

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from data import Url
from locators.base_page_locators import *


class BasePage:
    def __init__(self, driver, url_path):
        self.driver = driver
        url = Url.BASE_PAGE
        self.url = url + url_path

    @allure.step('Открыть браузер на заданом урле')
    def open(self):
        url = self.url
        return self.driver.get(url)

    @allure.step('Ожидаем и собираем текущий "URL')
    def get_url(self, time=15):
        WebDriverWait(self.driver, time).until(ec.url_changes(self.driver.current_url))
        return self.driver.current_url

    @allure.step('Ожидаем и собирает текст элемента')
    def get_text(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(locator)).text

    @allure.step('Ищем эллемент по локатору')
    def find_element(self, locator, time=15):
        WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ждем изменения текста в эллементе')
    def wait_for_text_to_change(self, locator, time=15):
        old_text = self.driver.find_element(*locator).text
        WebDriverWait(self.driver, time).until(
            lambda driver: driver.find_element(*locator).text != old_text
        )

    @allure.step('Нажимаем "Enter" по локатору')
    def send_enter(self, locator):
        self.find_element(locator).send_keys(Keys.ENTER)

    @allure.step('Ожидание и клик по элементу')
    def click_element(self, locator, time=15):
        WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(locator)).click()

    @allure.step('Наведение курсора на элемент')
    def mouseover_element(self, locator):
        ac(self.driver).move_to_element(self.find_element(locator)).perform()

    @allure.step('Ожидание элемента и ввод данных')
    def send_input(self, locator, data, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator)).send_keys(data)

    @allure.step('Ожидание и клик по лого "Byrotation"')
    def click_byrotation_logo(self):
        self.click_element(BasePageLocators.BY_ROTATION_LOGO)

    @allure.step('Принятие куков')
    def accept_cookies(self, time=10):
        shadow_host = self.driver.find_element(By.ID, "usercentrics-root")
        shadow_root = self.driver.execute_script("return arguments[0].shadowRoot", shadow_host)
        WebDriverWait(shadow_root, time).until(
            ec.visibility_of_element_located(BasePageLocators.ACCEPT_ALL_COOKIES_BUTTON)).click()

    @allure.step('Берем текст из кук')
    def get_text_cookies(self, time=10):
        shadow_host = self.driver.find_element(By.ID, "usercentrics-root")
        shadow_root = self.driver.execute_script("return arguments[0].shadowRoot", shadow_host)
        return WebDriverWait(shadow_root, time).until(
            ec.visibility_of_element_located(BasePageLocators.ACCEPT_ALL_COOKIES_BUTTON)).text

    @allure.step('Переход к футеру')
    def go_to_footer(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
