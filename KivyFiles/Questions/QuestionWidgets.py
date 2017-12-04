import re

from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from KivyCommunication import *

from kivy.uix.button import Button


class IntSpinner(Spinner):
    """
    IntInput only excepts numbers
    """
    def __init__(self, question):
        super(IntSpinner, self).__init__(text='0', values=('0', '1', '2', '3', '4', '5','6', '7', '8', '9'))
        self.question_data = question
        self.question_number = question.question_id


    def get_answer(self):
        return self.text


class UntoggbleToggle(ToggleButtonBehavior, LoggedButton):
    def __init__(self, **kwargs):
        super(UntoggbleToggle, self).__init__(allow_no_selection=False, **kwargs)


class MultipleAnswersObj(GridLayout):
    """
    Allows the user to answer one of many questions
    See https://kivy.org/docs/api-kivy.uix.dropdown.html
    """
    def __init__(self, question):
        super(MultipleAnswersObj, self).__init__(rows=1, cols=len(question.list_of_possible_answers))
        self.question_data = question
        for answer in question.list_of_possible_answers:
            btn_answer = UntoggbleToggle(text=answer, group='question_{}'.format(question.question_id))
            btn_answer.name = 'question_%s_answer_%s' % (format(question.question_id), answer)
            self.add_widget(btn_answer)

        self.question_number = question.question_id

    def get_answer(self):
        for child in self.children:
            if type(child) == UntoggbleToggle:
                if child.state == 'down':
                    return child.text
        return None


class BooleanQuestion(GridLayout):
    """
    A yes\no questionn
    """
    def __init__(self, question):
        super(BooleanQuestion, self).__init__(rows=1, cols=2)
        self.question_data = question
        btn_yes = UntoggbleToggle(text='yes', group='question_{}'.format(question.question_id))
        btn_yes.name = 'question_%s_answer_%s' % (format(question.question_id), 'yes')
        btn_no = UntoggbleToggle(text='no', group='question_{}'.format(question.question_id))
        btn_no.name = 'question_%s_answer_%s' % (format(question.question_id), 'no')
        self.add_widget(btn_yes)
        self.add_widget(btn_no)

        self.question_number = question.question_id

    def get_answer(self):
        for child in self.children:
            if type(child) == UntoggbleToggle:
                if child.state == 'down':
                    return child.text == "yes"
        return None

