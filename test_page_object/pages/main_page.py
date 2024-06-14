import allure
from test_page_object.pages.base_page import BasePage
from test_page_object.locators.main_page_locators import MainPageLocators
from helpers import format_locators


class MainPage(BasePage):

    def cookies_acceptation(self):
        self.click_on_element(MainPageLocators.COOKIES_BUTTON)

    def get_answer_text(self, num):
        answer_locator = format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        question_locator = format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.click_on_element(question_locator)
        return self.get_text_from_element(answer_locator)

    @allure.step('Жмем на кнопку Заказать')
    def make_order(self, button):
        self.click_on_element(button)