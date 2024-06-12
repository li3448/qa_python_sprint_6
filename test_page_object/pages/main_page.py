
from test_page_object.pages.base_page import BasePage
from test_page_object.locators.main_page_locators import MainPageLocators
class MainPage(BasePage):


    def cookies_acceptation(self):
        self.click_on_element(MainPageLocators.COOKIES_BUTTON)

    def click_to_get_answer(self, locator_quest, locator_ans, q_num):
        method_q ,locator_q = locator_quest
        method_a, locator_a = locator_ans

        locator_q = locator_q.format(q_num)
        locator_a = locator_a.format(q_num)

        self.click_on_element((method_q, locator_q))
        return self.get_text_from_element((method_a, locator_a))

    def check_answer(result, expected):
        return result == expected
