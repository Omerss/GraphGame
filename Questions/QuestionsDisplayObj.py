
__all__ = ('QuestionDisplay')

import QuestionObj
from CheckBoxObj import CheckBox
from getNumberObj import getNumber
from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty, StringProperty, ListProperty
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.button import Button
from kivy.uix.button import ButtonBehavior
from kivy.uix.button import Label

class QuestionDisplay():
    questions = []
    usersAnswers = {}
    questionsArray = []

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
            #do stuff

    def __init__ (self, questions):
        btn1 = Button(text='submit')
        btn1.bind(on_press=callback)
        self.questions= questions
        i =0
        for question in questions:
            if (question.is_the_question_open):
                openQuestion = buildOpenQuestion(question)
                self.questionsArray[i] =openQuestion
            else:
                checkBox= buildCheckBox(question)
                self.questionsArray[i] = checkBox



if __name__ == '__main__':
    from random import uniform
    from kivy.base import runTouchApp
    from kivy.uix.gridlayout import GridLayout

    runTouchApp(x)




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




