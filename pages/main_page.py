from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
          
    def scroll_to_faq(self):
        element = self.find_element_with_wait(MainPageLocators.FAQ_BUTTONS)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element)

    def open_faq(self, index):
        buttons = self.driver.find_elements(*MainPageLocators.FAQ_BUTTONS)
        button = buttons[index]
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", button
        )
        button.click()

    def faq_answer(self, index):
        panels = self.driver.find_elements(*MainPageLocators.FAQ_PANEL)
        return panels[index].text

    #Нажать на верхнюю кнопку Заказать
    def click_order_button_top(self):
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_TOP)

    #Нажать нижнюю кнопку Заказать с прокруткой до неё
    def click_order_button_bottom(self):
        button = self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click() 

    #Нажать на логотип Самокат
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    #Нажать на логотип Яндекс
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    def close_cookie_banner(self):
        try:
            self.click_element_with_wait(MainPageLocators.COOKIE_ACCEPT_BUTTON)
        except Exception:
            pass