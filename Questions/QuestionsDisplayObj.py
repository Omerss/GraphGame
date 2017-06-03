from CheckBoxObj import CheckBox
from getNumberObj import getNumber
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App


class QuestionDisplay(App):
    questions = None
    usersAnswers = None
    questionsArray = None

    def __init__(self, questions, **kwargs):
        super(QuestionDisplay, self).__init__(**kwargs)

        num_of_rows = len(questions) + 1
        self.layout = GridLayout(rows=num_of_rows)
        self.questions = questions
        self.questionsArray = []
        self.usersAnswers = []
        self.set_questions(questions)
        submit_button = Button(text='submit')
        submit_button.bind(on_press=self.submit_button)
        self.layout.add_widget(submit_button)

    def submit_button(self):
        go_to_answers = True

        for question in self.questionsArray:
            if question.getAnswer == -1:
                go_to_answers = False
            else:
                self.usersAnswers.append(question.getAnswer)

        if go_to_answers:
            pass

    def set_questions(self, questions):
        for question in questions:
            if question.isOpenQuestion():
                new_question = getNumber(question)
            else:
                new_question = CheckBox(question)
            self.questionsArray.append(new_question)
            self.layout.add_widget(new_question)

    def build(self):
        return self.layout



