from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton

from Questions.QuestionWidgets import MultipleAnswersObj, IntInput, BooleanQuestion
from SupplementaryFiles.Enums import QuestionTypes


class QuestionDisplay(App):
    questions = None
    usersAnswers = None
    questionsArray = None

    def __init__(self, questions, queue, **kwargs):
        super(QuestionDisplay, self).__init__(**kwargs)

        num_of_rows = 2*len(questions) + 1
        self.layout = GridLayout(rows=num_of_rows, cols=1)
        self.questions = questions
        self.questionsArray = []
        self.usersAnswers = []
        self.set_questions(questions)
        self.submit_button = Button(text='submit')
        self.submit_button.bind(on_press=self.submit_action)
        self.layout.add_widget(self.submit_button)

    def submit_action(self, instance):
        go_to_answers = True

        for question in self.questionsArray:
            if question.getAnswer == -1:
                go_to_answers = False
            else:
                self.usersAnswers.append(question.getAnswer)

        if go_to_answers:
            pass

    def set_questions(self, questions):
        for i in range(len(questions)):
            new_question_label = Label(text=questions[i].question_string)
            if questions[i].question_type_number == QuestionTypes.NUMBER:
                new_question = IntInput(text='', multiline=False)

            elif questions[i].question_type_number == QuestionTypes.MULTIPLE_CHOICE:
                new_question = MultipleAnswersObj(questions[i], i)

            elif questions[i].question_type_number == QuestionTypes.BOOLEAN:
                new_question = BooleanQuestion(i)

            self.questionsArray.append(new_question)
            self.layout.add_widget(new_question_label)
            self.layout.add_widget(new_question)

    def build(self):
        return self.layout



