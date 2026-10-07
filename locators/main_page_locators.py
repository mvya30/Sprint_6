from selenium.webdriver.common.by import By


class MainPageLocators:
    #Локаторы кнопок "Заказать"
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")
    #ORDER_BUTTON_BOTTOM = (By.XPATH, "(//div[contains(@class, 'Home_FinishButton__1_cWm')]//button[contains(text(), 'Заказать')]")

    #Локаторы текстов вопросов FAQ (стрелки)
    FAQ_BUTTONS = (By.CSS_SELECTOR, ".accordion__button")

    #Локаторы текстов ответов
    FAQ_PANEL = (By.CSS_SELECTOR, ".accordion__panel") 
    
    #Локатор логотипа Самокат
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")

    #Локатор ЯндексСамокат
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")

    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")
