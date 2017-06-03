from CheckBoxObj import CheckBox
from getNumberObj import getNumber
from kivy.uix.button import Button


class QuestionDisplay():
    questions = []
    usersAnswers = {}
    questionsArray = []

    def __init__ (self, questions):
        btn1 = Button(text='submit')
        btn1.bind(on_press=self.callback)
        self.questions = questions
        i = 0
        for question in questions:
            if (question.isOpenQuestion()):
                openQuestion = buildOpenQuestion(question)
                self.questionsArray[i] = openQuestion
            else:
                checkBox = buildCheckBox(question)
                self.questionsArray[i] = checkBox

    def callback(self,instance):
        gotoAnswers = True
        i=0
        for question in self.questionsArray:
            if (question.getAnswer == -1):
                gotoAnswers = False
            else:
                self.usersAnswers[i] = question.getAnswer
            i = i+1
        if (gotoAnswers):
            pass




if __name__ == '__main__':
    from random import uniform
    from kivy.base import runTouchApp
    from kivy.uix.gridlayout import GridLayout
    x = GridLayout
    QuestionDisplay(x)


def buildSubmissionButton ():
    btn1 = Button(text='submit')
    btn1.bind(on_press=callback)

def callback(instance):
    print('The button <%s> is being pressed' % instance.text)

def buildCheckBox(question):
    checkBox = CheckBox (question)
    return checkBox

def buildOpenQuestion(question):
    openQuestion = getNumber(question)
    return openQuestion




