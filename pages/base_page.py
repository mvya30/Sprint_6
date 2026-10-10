import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step ("Открыть страницу: {url}")
    def open(self, url=None):
        self.driver.get(url or self.BASE_URL)

    @allure.step ("Дождаться видимости элемента: {locator}")
    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Дождаться появления всех элементов: {locator}")
    def find_elements_with_wait(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    @allure.step("Дождаться кликабельности и нажать на элемент: {locator}")
    def click_element_with_wait(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    @allure.step("Ввести текст '{text}' в поле: {locator}, прежде очистив его")
    def fill(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("Дождаться появления текста '{text}' в элементе: {locator}")
    def wait_for_text(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    @allure.step("Проверить, открылась ли страница по URL: {url}")
    def is_url_opened(self, url):
        try:
            self.wait.until(EC.url_to_be(url))
            return True
        except TimeoutException:
            return False

    @allure.step("Прокрутить страницу к элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",
            element
    )   

    @allure.step("Найти элемент по индексу {index} и нажать на него: {locator}")
    def click_element_by_index(self, locator, index):
        elements = self.find_elements_with_wait(locator)
        element = elements[index]
        self.scroll_to_element(element)
        element.click()

    @allure.step("Дождаться открытия нового окна или вкладки")
    def wait_for_new_window(self, previous_handles):
        self.wait.until(
            EC.new_window_is_opened(previous_handles)
        )

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_window(self, previous_handles):
        self.wait_for_new_window(previous_handles)

        new_handles = [
            handle for handle in self.driver.window_handles
            if handle not in previous_handles
        ]
        self.driver.switch_to.window(new_handles[0])

    @allure.step("Дождаться, пока URL будет содержать одну из подстрок: {substrings}")
    def wait_for_url_contains_any(self, substrings):
        return self.wait.until(
            lambda driver: any(
                substring in driver.current_url
                for substring in substrings
            )
        )
    