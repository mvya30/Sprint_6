import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.header_page_locators import HeaderPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class OrderPage(BasePage):

    @staticmethod
    def metro_option(metro):
        return (By.XPATH, f"//div[contains(@class,'Order_Text') and text()='{metro}']")

    @allure.step("Нажать на верхнюю кнопку «Заказать»")
    def click_order_button_top(self):
        self.click_element_with_wait(OrderPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать на нижнюю кнопку «Заказать»")
    def click_order_button_bottom(self):
        self.click_element_with_wait(OrderPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Заполнить первую форму заказа")
    def fill_first_form(self, name, surname, address, phone, metro=None):
        self.fill(OrderPageLocators.NAME_INPUT, name)
        self.fill(OrderPageLocators.SURNAME_INPUT, surname)
        self.fill(OrderPageLocators.ADDRESS_INPUT, address)
        if metro:
            self.fill(OrderPageLocators.METRO_INPUT, metro)
            self.click_element_with_wait(OrderPage.metro_option(metro))
            
        self.fill(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element_with_wait(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить вторую форму заказа")
    def fill_second_form(self, date, rental_period=None, color=None, comment=""):
        self.fill(OrderPageLocators.DATE_INPUT, date)
        self.find_element_with_wait(OrderPageLocators.DATE_INPUT).send_keys(Keys.ENTER)

        if rental_period:
            self.click_element_with_wait(OrderPageLocators.RENTAL_PERIOD)
            option_locator = (By.XPATH, OrderPageLocators.RENTAL_OPTION_TEMPLATE[1].format(rental_period))
            self.click_element_with_wait(option_locator)
            
        if color == 'black':
            self.click_element_with_wait(OrderPageLocators.COLOR_BLACK)
        elif color == 'grey':
            self.click_element_with_wait(OrderPageLocators.COLOR_GREY)

        if comment:
            self.fill(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Подтвердить оформление заказа")
    def confirm_order(self):
        self.click_element_with_wait(OrderPageLocators.ORDER_BUTTON)
        self.click_element_with_wait(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Получить текст сообщения об успешном заказе")
    def get_success_message(self):
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)

    @allure.step("Закрыть баннер об использовании Cookie")
    def close_cookie_banner(self):
        try:
            self.click_element_with_wait(HeaderPageLocators.COOKIE_ACCEPT_BUTTON)
        except Exception:
            pass
        