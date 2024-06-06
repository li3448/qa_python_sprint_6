import pytest
import allure
from test_page_object.pages.main_page import MainPage
from ..data import *
from test_page_object.locators.main_page_locators import *


class TestMainPage:

    @allure.title("Проверка вопросов о важном") #декораторы
    @allure.description("Поиск текста, клик, проверка выпадающего текста")#декоратор для Allure
    @allure.link(MAIN_URL)
    @pytest.mark.parametrize(
    "q_num, expected_result",
    [
        (0, Answers.ANSWER_0),
        (1, Answers.ANSWER_1),
        (2, Answers.ANSWER_2),
        (3, Answers.ANSWER_3),
        (4, Answers.ANSWER_4),
        (5, Answers.ANSWER_5),
        (6, Answers.ANSWER_6),
        (7, Answers.ANSWER_7)
    ]
    )
    def test_questions(self, driver, q_num, expected_result):
        main_page = MainPage(driver)
        result = main_page.click_to_get_answer(MainPageLocators.QUESTION_LOCATOR,
                                                       MainPageLocators.ANSWER_LOCATOR,
                                                       q_num)

        assert MainPage.check_answer(result, expected_result)