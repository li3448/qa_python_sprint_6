import pytest
import allure
from test_page_object.pages.main_page import MainPage
from test_page_object.data import Answers
from conftest import driver


class TestMainPage:
    @allure.title('Проверка текста ответов в разделе "Вопросы о важном"')
    @pytest.mark.parametrize('num, answer', [
        (0, Answers.ANSWER_0),
        (1, Answers.ANSWER_1),
        (2, Answers.ANSWER_2),
        (3, Answers.ANSWER_3),
        (4, Answers.ANSWER_4),
        (5, Answers.ANSWER_5),
        (6, Answers.ANSWER_6),
        (7, Answers.ANSWER_7)
        ],
        ids=['вопрос 0',
             'вопрос 1',
             'вопрос 2',
             'вопрос 3',
             'вопрос 4',
             'вопрос 5',
             'вопрос 6',
             'вопрос 7'])
    def test_questions(self, driver, num, answer):
        main_page = MainPage(driver)
        main_page.cookies_acceptation()
        assert main_page.get_answer_text(num) == answer

