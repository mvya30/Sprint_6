import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

ORDER_DATA = [
    {
        "name": "Марина",
        "surname": "Ярцева",
        "address": "Москва, Красная, 145",
        "metro": "Царицыно",
        "phone": "+79184470134",
        "date": "15.10.2026",
        "rental_period": "двое суток",
        "color": "black",
        "comment": "Позвонить за час",
    },
    {
        "name": "Анна",
        "surname": "Сидорова",
        "address": "Санкт-Петербург, Невский, 10",
        "metro": "Октябрьское поле",
        "phone": "+79990001122",
        "date": "08.10.2026",
        "rental_period": "семеро суток",
        "color": "grey",
        "comment": "Оставить у двери",
    },
]
@allure.description("Проверяем полный флоу заказа с двух точек входа и на двух наборах данных")
class TestOrder:

    @pytest.mark.parametrize("entry_point", ["top", "bottom"])
    @pytest.mark.parametrize("data", ORDER_DATA)
    def test_order_flow(self, driver, entry_point, data):

        main = MainPage(driver)
        main.open()
        main.close_cookie_banner()

        if entry_point == "top":
            main.click_order_button_top()
        else:
            main.click_order_button_bottom()

        order = OrderPage(driver)
        
        order.fill_first_form(
             name=data["name"],
             surname=data["surname"],
             address=data["address"],
             metro=data["metro"],
             phone=data["phone"],
        )

        order.fill_second_form(
            date=data["date"],
            rental_period=data["rental_period"],
            color=data["color"],
            comment=data["comment"],
        )
        order.confirm_order()

        success_text = order.get_success_message()
        assert "Заказ оформлен" in success_text
        
    @allure.story("Редиректы по логотипам")
    def test_scooter_logo_redirects_to_main(self, driver):
        main = MainPage(driver)
        main.open()
        main.click_order_button_top()
        MainPage(driver).click_scooter_logo()
        assert "qa-scooter" in driver.current_url

    def test_yandex_logo_opens_dzen(self, driver):
        main = MainPage(driver)
        main.open()
        main.click_yandex_logo()
        main.wait_for_url_contains(["dzen.ru", "yandex.ru"])

        assert "dzen.ru" in driver.current_url or "yandex.ru" in driver.current_url
        