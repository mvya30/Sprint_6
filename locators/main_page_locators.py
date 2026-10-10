from selenium.webdriver.common.by import By

class MainPageLocators:
       
    #Локаторы текстов вопросов FAQ (стрелки)
    FAQ_BUTTONS = (By.CSS_SELECTOR, ".accordion__button")

    #Локаторы текстов ответов
    FAQ_PANEL = (By.CSS_SELECTOR, ".accordion__panel") 
    