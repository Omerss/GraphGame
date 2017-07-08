from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton

from Questions.QuestionWidgets import MultipleAnswersObj, IntInput, BooleanQuestion
from SupplementaryFiles.Enums import QuestionTypes


class ResultDisplay(App):
    questions = None
    usersAnswers = None
    questionsArray = None

    def __init__(self, question_list):
        super(ResultDisplay, self).__init__()
        self.layout = GridLayout(rows=1, cols=2)

        self.layout.add_widget(self.get_question_result_grid(question_list=question_list))

        map_grid = GridLayout(rows=2, cols=1)
        self.layout.add_widget(map_grid)

    @staticmethod
    def get_question_result_grid(question_list):
        question_result_grid = GridLayout(rows=len(question_list), cols=1)

        for item in question_list:
            new_question = GridLayout(rows=3, cols=1)
            new_question.add_widget(Label(text=item.question_string))

            keys = GridLayout(rows=1, cols=3)
            keys.add_widget("User Answer")
            keys.add_widget("User Graph Answer")
            keys.add_widget("True Answer")
            new_question.add_widget(keys)

            answers = GridLayout(rows=1, cols=3)
            answers.add_widget(item.get_user_answer())
            answers.add_widget(item.get_user_graph_answer())
            answers.add_widget(item.get_true_answer())
            new_question.add_widget(answers)

            question_result_grid.add_widget(new_question)

        return question_result_grid


def calculatePrecentage(list):
    for answer in list:
        answers_list = answer.get_question_results()
        


    return