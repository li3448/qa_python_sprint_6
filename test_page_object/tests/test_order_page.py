import pytest
import time
import allure
from test_page_object.pages.order_page import OrderPage
from ..data import *
from test_page_object.locators.main_page_locators import *
from test_page_object.locators.order_page_locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestOrderPage:
    @allure.title('Проверка позитивного сценария оформления заказа c двумя точками входа')
    @allure.description('Тест для кнопок Заказать в заголовке и середине главной страницы')
    @pytest.mark.parametrize(
        "expected_result",
        [
            (OrderAnswer.ANSWER_0)
        ]
    )
    def test_positive_order(self, driver, expected_result):
        main_page = OrderPage(driver)
        result = main_page.take_positive_order(MainPageLocators.BUTTON_ORDER_TOP,
                                        OrderPageLocators.BUTTON_NEXT,
                                        OrderPageLocators.NAME_FIELD,
                                        OrderAnswer.NAME_1,
                                        OrderPageLocators.SECOND_NAME_FIELD,
                                        OrderAnswer.SECOND_NAME_1,
                                        OrderPageLocators.ADRESS_FIELD,
                                        OrderAnswer.ADRESS,
                                        OrderPageLocators.METRO_FIELD,
                                        OrderPageLocators.METRO_STATION,
                                        OrderPageLocators.PHONE_FIELD,
                                        OrderAnswer.PHONE,
                                        OrderPageLocators.DAY_ORDER,
                                        OrderPageLocators.DAY_CALENDAR,
                                        OrderPageLocators.RENT,
                                        OrderPageLocators.RENT_DURATION,
                                        OrderPageLocators.COLOR_BLACK,
                                        OrderPageLocators.COMMENTARY,
                                        OrderAnswer.COMMENTARY_1,
                                        OrderPageLocators.BUTTON_ORDER,
                                        OrderPageLocators.BUTTON_CONFIRMED_YES,
                                        OrderPageLocators.ORDER_MESSAGE)
        assert OrderPage.check(result, expected_result)


    def test_logo_scooter(self, driver):
        main_page = OrderPage(driver)
        current_page = main_page.order_page(MainPageLocators.BUTTON_ORDER_TOP,
                             OrderPageLocators.LOGO_SCOOTER)
        assert current_page == MAIN_URL

    def test_logo_ya(self, driver):
        main_page = OrderPage(driver)
        main_page.order_page(MainPageLocators.BUTTON_ORDER_TOP, OrderPageLocators.LOGO_YANDEX)
        main_page.switch_to_new_window()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_is("Дзен"))

        assert driver.current_url == YA_URL