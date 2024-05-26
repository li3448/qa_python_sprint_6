from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, "//div[@id='accordion__heading-{}']" #Вопросы
    ANSWER_LOCATOR = By.XPATH, "//div[@id='accordion__panel-{}']" #Ответы
    BUTTON_ORDER_TOP = By.XPATH, "//button[@class='Button_Button__ra12g']" #Верхняя кнопка заказа
    BUTTON_ORDER_BOTTOM = By.XPATH, "//button[@class='Button_Button__ra12g.Button_Middle__1CSJM']" #Нижняя кнопка заказа