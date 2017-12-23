#!/usr/bin/python
# -*- coding: utf-8 -*-
import kivy
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore

from KivyFiles.GraphDisplay import GraphDisplay


from KivyCommunication import *


class ResultDisplay:
    """
        This object lies between the screen and the widget. It is used as a buffer between the two.
    """
    parent_screen = None

    def __init__(self, parent_screen=None):
        self.parent_screen = parent_screen
        self.the_widget = ResultWidget(self, self.parent_screen.main_app)

    def load(self):
        self.the_widget.on_enter()


class ResultWidget(GridLayout):
    question_list = None
    main_app = None
    parent_app = None
    score_label_height = 50
    submit_button_height = 50
    graph_spacing = 50
    graph_title_size = 30
    res = None

    def __init__(self, parent_app, main_app):
        # The result window is split to 3 parts - information, scoreboard and button
        super(ResultWidget, self).__init__(rows=3, cols=1)

        self.parent_app = parent_app
        self.main_app = main_app

    def on_enter(self):
        col_width = kivy.core.window.Window.size[0] / 2
        height_spacing = self.score_label_height + self.submit_button_height + self.graph_spacing + \
                         (2 * self.graph_title_size)
        height = (kivy.core.window.Window.size[1] - height_spacing) / 2

        # First part of the result screen is split in two - questions and graphs
        layout = GridLayout(rows=len(self.main_app.user_answers) * 2, cols=2)

        layout.add_widget(self.get_question_result_grid(user_answers=self.main_app.user_answers, width=col_width))
        store = JsonStore("Json/answers.json", encoding='utf-8')
        map_grid = GridLayout(rows=4, cols=1)
        map_grid.add_widget(Label(text=store['answers']['graphs_types']['discovered_graph'][::-1],font_name="fonts/the_font.ttf",
            halign='right', size_hint_y=None, height=self.graph_title_size))
        graph_discovered = GraphDisplay(graph=self.main_app.discovered_graph,font_name="fonts/the_font.ttf",
            halign='right', dim=(col_width, height))
        map_grid.add_widget(graph_discovered)
        map_grid.add_widget(Label(text=store['answers']['graphs_types']['real_graph'][::-1],font_name="fonts/the_font.ttf",
            halign='right', size_hint_y=None, height=self.graph_title_size))
        graph_true = GraphDisplay(graph=self.main_app.current_graph,
                                  dim=(col_width, height))
        map_grid.add_widget(graph_true)
        layout.add_widget(map_grid)

        self.add_widget(layout)
        self.res = self.calculate_percentage(self.main_app.user_answers)
        self.add_widget(Label(text=store['answers']['scores']['subject_score'][::-1]+" {0}%;".format(self.res['user_score'])+ store['answers']['scores']['discovered_graph_score'][::-1]+" {1}%;".format(self.res['possible_score'])+ store['answers']['scores']['nodes_discovered'][::-1]+" {2}%"
                              .format(self.game_grade(self.main_app.discovered_graph,
                                                      self.main_app.current_graph)),
                              size_hint_y=None, height=self.score_label_height, font_name="fonts/the_font.ttf", halign='right'))

        self.submit_button = Button(text=store['answers']['next_button'][::-1], size_hint_y=None,font_name="fonts/the_font.ttf", halign='right', height=self.submit_button_height)
        self.submit_button.bind(on_press=self.stop_me)
        self.add_widget(self.submit_button)

    def stop_me(self, instance):
        self.parent_app.parent_screen.end_results()

    @staticmethod
    def get_question_result_grid(user_answers, width):
        """
        Here we create the question grid.
        Each question has the question itself and the three categories of answers:
        The answers the user gave
        The answers the user would have given if they had a perfect memory
        The true answer in the graph.
        """
        user_answers = user_answers
        question_result_grid = GridLayout(rows=len(user_answers))
        store = JsonStore("Json/answers.json", encoding='utf-8')
        for item in user_answers:
            new_question = GridLayout(rows=3, cols=1)
            new_question.add_widget(Label(text=item.question_string, text_size=(width, None)))

            keys = GridLayout(rows=1, cols=3)
            keys.add_widget(Label(text=store['answers']['answer_graph_type']['user_answer'][::-1]), font_name="fonts/the_font.ttf", halign='right')
            keys.add_widget(Label(text=store['answers']['answer_graph_type']['discovered_graph_answer'][::-1]), font_name="fonts/the_font.ttf",halign='right')
            keys.add_widget(Label(text=store['answers']['answer_graph_type']['full_graph_answer'][::-1]), font_name="fonts/the_font.ttf",halign='right')
            new_question.add_widget(keys)

            answers = GridLayout(rows=1, cols=3)
            answers.add_widget(Label(text=str(item.user_answer)))
            answers.add_widget(Label(text=str(item.user_graph_answer)))
            answers.add_widget(Label(text=str(item.real_answer)))
            new_question.add_widget(answers)

            KL.log.insert(action=LogAction.data, comment='results_question_%s_user_%s_discovered_%s_true_%s' % (
                item.question_string, str(item.user_answer), str(item.user_graph_answer), str(item.real_answer)))

            question_result_grid.add_widget(new_question)

        return question_result_grid

    @staticmethod
    def calculate_percentage(user_answers):
        """
        Calculate the score of the user and the user's graph as compared to the truth.
        :param user_answers:
        :return:
        """
        answer_list = user_answers
        user_answers_percentage = 0
        user_graph_answer_percentage = 0
        for answer in answer_list:
            if str(answer.user_answer) == str(answer.user_graph_answer):
                user_answers_percentage = user_answers_percentage + 1
            if str(answer.real_answer) == str(answer.user_graph_answer):
                user_graph_answer_percentage = user_graph_answer_percentage + 1
        num_of_questions = len(answer_list)
        num_of_questions = num_of_questions if num_of_questions != 0 else 1
        user_possible_success = round(user_answers_percentage * 100 / float(num_of_questions), 2)
        user_true_success = round(user_graph_answer_percentage * 100 / float(num_of_questions), 2)
        return {'possible_score': user_true_success, 'user_score': user_possible_success}

    @staticmethod
    def game_grade(user_seen_graph, real_graph):
        """
        Returns the final grade for the graph. Num nodes seen vs num nodes existing.
        """
        user_graph_num_of_nodes = len([item for item in user_seen_graph.node_list if item.is_real()])
        real_graph_num_of_nodes = len([item for item in real_graph.node_list if item.is_real()])
        return round(100 * float(user_graph_num_of_nodes) / float(real_graph_num_of_nodes), 2)

    def build(self):
        return self.meta_layout
