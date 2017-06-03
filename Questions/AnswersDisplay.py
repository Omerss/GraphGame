import QuestionObj
import AnswerObject

from kivy.uix.gridlayout import GridLayout
from random import uniform
from kivy.base import runTouchApp
from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty, StringProperty, ListProperty
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.button import Button
from kivy.uix.button import ButtonBehavior
from kivy.uix.button import Label
from kivy.app import App

class AnswersDisplay(App):
    usersAnswers = None
    questionsArray = None
    userSeenGraph = None
    fullGraph = None
    def __init__ (self, usersAnswers, questionsArray, userSeenGraph, fullGraph,**kwargs):
        super(AnswersDisplay, self).__init__(**kwargs)

        self.layout = GridLayout(rows = 6)
        self.usersAnswers = usersAnswers
        self.questionsArray = questionsArray
        self.userSeenGraph= userSeenGraph
        self.fullGraph = fullGraph

        userSeenGraphAnswers = set_answer_objects (questionsArray, userSeenGraph)
        fullGraphAnswers = set_answer_objects (questionsArray, fullGraph)
        submit_button = Button(text='exit')
        submit_button.bind(on_press=self.callback)
        self.layout.add_widget(submit_button)

    def callback(self,instance):
            pass


    def set_answer_objects(questionsArray, graph):
        for question in questionsArray:


    def build(self):
        return self.layout








