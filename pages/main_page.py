from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MainPage(BasePage):

    #Прокрутить к разделу Вопросы      
    def scroll_to_faq(self):
        element = self.find_element_with_wait(MainPageLocators.FAQ_BUTTONS)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element)

    #Открыть вопрос FAQ по индексу
    def open_faq(self, index):
        buttons = self.driver.find_elements(*MainPageLocators.FAQ_BUTTONS)
        button = buttons[index]
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", button
        )
        button.click()
                
    #Получить текст ответа FAQ
    def faq_answer(self, index):
        panels = self.driver.find_elements(*MainPageLocators.FAQ_PANEL)
        return panels[index].text

    #Нажать на верхнюю кнопку Заказать
    def click_order_button_top(self):
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_TOP)

    #Нажать на нижнюю кнопку Заказать
    def click_order_button_bottom(self):
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_BOTTOM)

    #Нажать на логотип Самокат
    def click_scooter_logo(self):
        self.click_element_with_wait(MainPageLocators.SCOOTER_LOGO)
       
    #Закрыть баннер с сообщением об использовании Куки
    def close_cookie_banner(self):
        try:
            self.click_element_with_wait(MainPageLocators.COOKIE_ACCEPT_BUTTON)
        except Exception:
            pass

    #Нажать на логотип Яндекс
    def click_yandex_logo(self):
        self.click_element_with_wait(MainPageLocators.YANDEX_LOGO)
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    #Дождаться, пока URL будет содержать одну из подстрок
    def wait_for_url_contains(self, substrings):
        WebDriverWait(self.driver, 10).until(
            lambda d: any(s in d.current_url for s in substrings)
        )
        