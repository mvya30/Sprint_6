from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

#Открыть страницу по URL
    def open(self, url=None):
        self.driver.get(url or self.BASE_URL)

# Ждёт пока элемент станет видимым на странице
    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

# Ждёт пока элемент станет кликабельным и кликает по нему
    def click_element_with_wait(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

# Вводит текст в поле, прежде очистив его
    def fill(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

# Получить текст элемента
    def get_text(self, locator):
        return self.find_element_with_wait(locator).text

# Дождаться появления текста в элементе
    def wait_for_text(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    #Проверка, открылась ли нужная страница по указанному URL
    def is_url_opened(self, url):
        try:
            self.wait.until(EC.url_to_be(url))
            return True
        except TimeoutException:
            return False
        