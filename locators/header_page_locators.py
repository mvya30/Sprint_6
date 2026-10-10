from selenium.webdriver.common.by import By

class HeaderPageLocators:

    #Локатор логотипа Самокат
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")

    #Локатор ЯндексСамокат
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")

    #Локатор баннера с сообщением об использовании Куки
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")
