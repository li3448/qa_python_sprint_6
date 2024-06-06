from selenium.webdriver.common.by import By

#Локаторы страницы заказа
class OrderPageLocators:
    NAME_FIELD = By.XPATH, "//input[@placeholder='* Имя']" #Поле имя
    SECOND_NAME_FIELD = By.XPATH, "//input[@placeholder='* Фамилия']" #Поле фамилия
    ADRESS_FIELD = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    PHONE_FIELD = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    METRO_FIELD = By.XPATH, "//input[@placeholder='* Станция метро']"
    METRO_STATION = By.XPATH, "//div[text()='Сокольники']"

    BUTTON_NEXT = By.XPATH, "//button[text()='Далее']" #Кнопка далее


    DAY_ORDER = By.XPATH, "//input[@placeholder='* Когда привезти самокат']" #Дата заказа
    DAY_CALENDAR = By.XPATH, "//div[text()='9']" #Календарь
    RENT = By.XPATH, "//div[@class='Dropdown-root']" #Срок аренды
    RENT_DURATION = By.XPATH, "//div[text()='сутки']"
    COLOR_BLACK = By.XPATH, "//input[@id='black']" #Черный самокат
    COLOR_GREY = By.XPATH, "//input[@id='grey']" #Серый самокат
    COMMENTARY = By.XPATH, "//input[@placeholder='Комментарий для курьера']" #Комментарий

    BUTTON_ORDER = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"

    BUTTON_CONFIRMED_YES = By.XPATH, "//button[text()='Да']"
    BUTTON_CONFIRMED_NO = By.XPATH, "//button[text()='Нет']"

    ORDER_MESSAGE = By.XPATH, "//div[text()='Заказ оформлен']"
    BUTTON_STATUS = By.XPATH, "//button[text()='Посмотреть статус']"

    MODAL_FRAME = By.XPATH, "//div[@class='Order_Overlay__3KW-T']"

    LOGO_SCOOTER = By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']"
    LOGO_YANDEX = By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']"