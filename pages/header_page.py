import allure
from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators
from selenium.webdriver.support import expected_conditions as EC

class HeaderPage(BasePage):

    @allure.step("Нажать на логотип Самокат")
    def click_scooter_logo(self):
        self.click_element_with_wait(HeaderPageLocators.SCOOTER_LOGO)
       
    @allure.step("Нажать на логотип Яндекс и переключиться на новую вкладку")
    def click_yandex_logo(self):
        previous_handles = self.driver.window_handles

        self.click_element_with_wait(HeaderPageLocators.YANDEX_LOGO)
        self.switch_to_new_window(previous_handles)

    @allure.step("Дождаться перехода на URL, содержащий одну из подстрок: {substrings}")
    def wait_for_url_contains(self, substrings):
        return self.wait_for_url_contains_any(substrings)    
