from CheckBoxObj import CheckBox
from getNumberObj import getNumber
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App

class QuestionDisplay(App):
    questions = None
    usersAnswers = None
    questionsArray = None

    def __init__ (self, questions, **kwargs):
        super(QuestionDisplay, self).__init__(**kwargs)

        self.layout = GridLayout(rows = 6)
        self.questions = []
        self.questionsArray = []
        self.usersAnswers = []
        self.set_questions(questions)
        submit_button = Button(text='submit')
        submit_button.bind(on_press=self.callback)
        self.layout.add_widget(submit_button)

    def callback(self,instance):
        gotoAnswers = True
        i = 0
        for question in self.questionsArray:
            if (question.getAnswer == -1):
                gotoAnswers = False
            else:
                self.usersAnswers[i] = question.getAnswer
            i = i+1
        if (gotoAnswers):
            pass

    def set_questions(self, questions):
        for question in questions:
            if (question.isOpenQuestion()):
                new_question = getNumber(question)
            else:
                new_question = CheckBox(question)
            self.questionsArray.append(new_question)
            self.layout.add_widget(new_question)

    def build(self):
        return self.layout






