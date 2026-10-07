import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

ORDER_DATA = [
    {
        "name": "Марина",
        "surname": "Ярцева",
        "address": "Москва, Красная, 145",
        "metro": "Тверская",
        "phone": "+79184470134",
        "date": "15.10.2026",
        "rental_period": "сутки",
        "color": "black",
        "comment": "Позвонить за час",
    },
    {
        "name": "Анна",
        "surname": "Сидорова",
        "address": "Санкт-Петербург, Невский, 10",
        "metro": "Невский проспект",
        "phone": "+79990001122",
        "date": "08.10.2026",
        "rental_period": "двое суток",
        "color": "grey",
        "comment": "Оставить у двери",
    },
]
@allure.feature("Заказ самоката")
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
