import QuestionObject
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
    user_seen_graph_answers = None
    full_graph_answers = None
    success_rate = 0

    def __init__ (self, answer_list, graph_user, graph_true):
        super(AnswersDisplay, self).__init__()

        self.layout = GridLayout(rows = 6)
        self.usersAnswers = usersAnswers
        self.questionsArray = questionsArray
        self.user_seen_graph_answers = user_seen_graph_answers
        self.full_graph_answers = full_graph_answers

        self.display_answers(user_seen_graph_answers, full_graph_answers)
        self.display_graphs()
        self.display_success_rates()

        success_rate_label = Label(text="success rate" + str(self.success_rate))
        self.layout.add_widget(success_rate_label)

        submit_button = Button(text='exit')
        submit_button.bind(on_press=self.callback)
        self.layout.add_widget(submit_button)

    def callback(self,instance):
            pass

    def display_answers (self, user_seen_graph_answers, full_graph_answers):
         counter = 0
         for question in self.questionsArray:
             question_label = Label(text=question.getQuestionString())
             self.layout.add_widget(question_label)
             user_answer_label = Label(text = "your answer" + str(self.usersAnswers[counter].get_question_result()))
             self.layout.add_widget(user_answer_label)
             user_seen_graph_answer_label = Label (text = "the answer by the graph you discovered" + str(
                 user_seen_graph_answers[counter].get_question_result()))
             self.layout.add_widget(user_seen_graph_answer_label)
             full_graph_answer_label = Label(text="the answer by the full graph" + str(
                 full_graph_answers[counter].get_question_result()))
             self.layout.add_widget(full_graph_answer_label)
             counter = counter + 1


    def display_graphs (self):
        #ask for tal's help
        pass


    def build(self):
        return self.layout

#pass to game manager
        user_seen_graph_answers = self.set_answer_objects(userSeenGraph)
        full_graph_answers = self.set_answer_objects(fullGraph)
    #pass to game manager
    def set_answer_objects(self, graph):
        answer_objects = []
        for question in self.questionsArray:
            question_number = question.get_question_number()
            question_arguments = question.get_question_arguments()
            answer_object = AnswerObj(graph, question_number, question_arguments)
            answer_objects.append(answer_object)
        return answer_objects


