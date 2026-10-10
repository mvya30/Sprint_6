import allure
import pytest
from pages.order_page import OrderPage
from order_data import ORDER_DATA

@allure.feature("Оформление заказа")
@allure.story("Полный флоу заказа")
@allure.description(
"Проверяем полный флоу заказа с двух точек входа "
"и на двух наборах данных."
)
class TestOrder:
    
    @allure.title("Оформление заказа: точка входа — {entry_point}")
    @pytest.mark.parametrize("entry_point", ["top", "bottom"])
    @pytest.mark.parametrize("data", ORDER_DATA)
    def test_order_flow(self, driver, entry_point, data):

        order = OrderPage(driver)
        order.open()
        order.close_cookie_banner()

        order_buttons = {
            "top": order.click_order_button_top,
            "bottom": order.click_order_button_bottom,
        }
        order_buttons[entry_point]()
                   
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
      