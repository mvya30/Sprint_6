import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Прокрутить страницу к разделу «Вопросы о важном»")     
    def scroll_to_faq(self):
        element = self.find_element_with_wait(MainPageLocators.FAQ_BUTTONS)
        self.scroll_to_element(element)

    @allure.step("Открыть вопрос FAQ с индексом {index}")
    def open_faq(self, index):
        self.click_element_by_index(MainPageLocators.FAQ_BUTTONS, index)
                
    @allure.step("Получить текст ответа FAQ с индексом {index}")
    def faq_answer(self, index):
        panels = self.find_elements_with_wait(MainPageLocators.FAQ_PANEL)
        return panels[index].text
  