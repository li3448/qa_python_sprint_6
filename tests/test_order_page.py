import pytest
import time
from test_page_object.pages.order_page import OrderPage
from test_page_object.locators.main_page_locators import *
from test_page_object.locators.order_page_locators import *


class TestOrderPage:

    @pytest.mark.parametrize(
        "expected_result",
        [
            (OrderAnswer.ANSWER_0)
        ]
    )
    #Успешный заказ
    def test_successful_order(self, driver, expected_result):
        main_page = OrderPage(driver)
        result = main_page.take_successful_order(MainPageLocators.BUTTON_ORDER_TOP,
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
        print(result)
        assert OrderPage.check(result, expected_result)

#Точка входа в сценарий
    def test_logo_scooter(self, driver):
        main_page = OrderPage(driver)
        current_page = main_page.order_page(MainPageLocators.BUTTON_ORDER_TOP,
                             OrderPageLocators.LOGO_SCOOTER)
        assert current_page == MAIN_URL

