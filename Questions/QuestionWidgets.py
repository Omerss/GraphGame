# import Kivy
import re

from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button


class IntInput(TextInput):
    def __init__(self, question_number):
        super(IntInput, self).__init__(text='', multiline=False)
        self.question_number = question_number

    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        s = re.sub(self.pat, '', substring)
        return super(IntInput, self).insert_text(s, from_undo=from_undo)

    def get_answer(self):
        return None if len(self.text) == 0 or int(self.text) < 0 else int(self.text)


class UntoggbleToggle(ToggleButtonBehavior, Button):
    def __init__(self, **kwargs):
        super(UntoggbleToggle, self).__init__(allow_no_selection=False, **kwargs)


class MultipleAnswersObj(GridLayout):
    """
    See https://kivy.org/docs/api-kivy.uix.dropdown.html
    """
    def __init__(self, question, question_number):
        super(MultipleAnswersObj, self).__init__(rows=1, cols=len(question.list_of_possible_answers))
        for answer in question.list_of_possible_answers:
            btn_answer = UntoggbleToggle(text=answer, group='question_{}'.format(question_number))
            self.add_widget(btn_answer)

        self.question_number = question_number

    def get_answer(self):
        for child in self.children:
            if type(child) == UntoggbleToggle:
                if child.state == 'down':
                    return child.text
        return None


class BooleanQuestion(GridLayout):

    def __init__(self, question_number):
        super(BooleanQuestion, self).__init__(rows=1, cols=2)
        btn_yes = UntoggbleToggle(text='yes', group='question_{}'.format(question_number))
        btn_no = UntoggbleToggle(text='no', group='question_{}'.format(question_number))
        self.add_widget(btn_yes)
        self.add_widget(btn_no)

        self.question_number = question_number

    def get_answer(self):
        for child in self.children:
            if type(child) == UntoggbleToggle:
                if child.state == 'down':
                    return child.text
        return None
