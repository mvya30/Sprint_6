from selenium.webdriver.common.by import By

class OrderPageLocators:

    # Первая форма: «Для кого самокат»
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//div[contains(@class,'select-search__option')][1]")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая форма: «Про аренду»
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class,'Dropdown-control')]")
    RENTAL_OPTION_TEMPLATE = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='{}']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH,  "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[normalize-space()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class,'Order_ModalHeader')]")

#Локаторы кнопок "Заказать"
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")
    