import QuestionObj
import AnswerObject
from AnswerObject import AnswerObj
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

        user_seen_graph_answers = self.set_answer_objects(userSeenGraph)
        full_graph_answers = self.set_answer_objects(fullGraph)

        self.display_answers(user_seen_graph_answers, full_graph_answers)
        self.display_graphs(userSeenGraph,fullGraph)
        self.display_success_rates()

        submit_button = Button(text='exit')
        submit_button.bind(on_press=self.callback)
        self.layout.add_widget(submit_button)

    def callback(self,instance):
            pass


    def set_answer_objects(self, graph):
        answer_objects = []
        for question in self.questionsArray:
            question_number = question.get_question_number()
            question_arguments = question.question_arguments()
            answer_object = AnswerObj(graph, question_number, question_arguments)
            answer_objects.append(answer_object)
        return answer_objects

    def display_answers (self, user_seen_graph_answers, full_graph_answers):
        counter =0
         for question in self.questionsArray:
             question_label = Label(text=question.getQuestionString)
             user_answer_label = 
             counter = counter + 1

         for answer in user_seen_graph_answers:
             pass

         for answer in full_graph_answers:
             pass

         label = Label(text='Hello world')
         self.layout.add_widget(new_question)

        pass

    def display_graphs (self, userSeenGraph,fullGraph):

        pass

    def display_success_rates (self):

        pass


    def build(self):
        return self.layout








