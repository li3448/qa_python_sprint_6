from test_page_object.pages.base_page import BasePage


class OrderPage(BasePage):
    def take_positive_order(self,
                              locator_button_order_top,
                              locator_button_next,
                              name_locator,
                              name,
                              second_name_locator,
                              second_name,
                              adress_locator,
                              adress,
                              metro_locator,
                              metro,
                              phone_locator,
                              phone,
                              date_locator,
                              date_calendar,
                              rent_locator,
                              rent_duration,
                              radio_button,
                              commentary_locator,
                              commentary,
                              button_order,
                              button_confirmed,
                              order_text):
        OrderPage.push_button(self, locator_button_order_top)
        OrderPage.first_fill(self,
                            name_locator,
                            name,
                            second_name_locator,
                            second_name,
                            adress_locator,
                            adress,
                            metro_locator,
                            metro,
                            phone_locator,
                            phone)
        OrderPage.push_button(self, locator_button_next)
        OrderPage.second_fill(self,
                             date_locator,
                             date_calendar,
                             rent_locator,
                             rent_duration,
                             radio_button,
                             commentary_locator,
                             commentary)
        OrderPage.push_button(self, button_order)
        OrderPage.push_button(self, button_confirmed)
        return OrderPage.get_text_from_element(self, order_text)

    def push_button(self, locator):
        method_q, locator_q = locator
        self.click_on_element((method_q, locator_q))

    def first_fill(self,
                  name_locator,
                  name,
                  second_name_locator,
                  second_name,
                  adress_locator,
                  adress,
                  metro_locator,
                  metro_station_locator,
                  phone_locator,
                  phone):
        method_q, locator_q = name_locator
        self.set_text_to_element((method_q, locator_q), name)

        method_q, locator_q = second_name_locator
        self.set_text_to_element((method_q, locator_q), second_name)

        method_q, locator_q = adress_locator
        self.set_text_to_element((method_q, locator_q), adress)

        method_q, locator_q = metro_locator
        self.click_on_element((method_q, locator_q))

        method_q, locator_q = metro_station_locator
        self.click_on_element((method_q, locator_q))

        method_q, locator_q = phone_locator
        self.set_text_to_element((method_q, locator_q), phone)

    def second_fill(self,
                   date_locator,
                   date_calendar,
                   rent_locator,
                   rent_duration,
                   radio_button,
                   commentary_locator,
                   commentary):
        method_q, locator_q = date_locator
        self.click_on_element((method_q, locator_q))

        method_q, locator_q = date_calendar
        self.click_on_element((method_q, locator_q))

        method_q, locator_q = rent_locator
        self.click_on_element((method_q, locator_q))

        method_q, locator_q = rent_duration
        self.click_on_element((method_q, locator_q))

        method_q, locator_q = radio_button
        self.click_on_element((method_q, locator_q))

        method_q, locator_q = commentary_locator
        self.set_text_to_element((method_q, locator_q), commentary)

    def check(result, expected):
        if expected in result:
            return True
        else:
            return False

    def order_page(self,
                   locator_button_order_top,
                   locator_scooter):
        OrderPage.push_button(self, locator_button_order_top)
        OrderPage.push_button(self, locator_scooter)
        return self.driver.current_url