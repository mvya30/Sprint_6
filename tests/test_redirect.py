import allure
from pages.header_page import HeaderPage

@allure.feature("Навигация по сайту")
@allure.story("Редиректы по логотипам")
class TestRedirect:
    
    @allure.title("Клик по логотипу Самоката ведёт на главную страницу")
    def test_scooter_logo_redirects_to_main(self, driver):
        header = HeaderPage(driver)
        header.open()
        header.click_scooter_logo()
        assert "qa-scooter" in driver.current_url

    @allure.title("Клик по логотипу Яндекса открывает Дзэн")
    def test_yandex_logo_opens_dzen(self, driver):
        header = HeaderPage(driver)
        header.open()
        header.click_yandex_logo()
        header.wait_for_url_contains(["dzen.ru", "yandex.ru"])

        assert "dzen.ru" in driver.current_url or "yandex.ru" in driver.current_url
      