#!/usr/bin/kivy
# -*- coding: utf-8 -*-
from kivy.clock import Clock
from kivy_communication import *
from kivy.uix.screenmanager import Screen

from kivyFiles.GraphTabletGame import GraphTabletGame
from Questions.QuestionObject import QuestionObject
from Questions.QuestionsDisplay import QuestionDisplay
from Questions.AnswerObject import AnswerObject
from Questions.ResultDisplay import ResultDisplay
from SupplementaryFiles.Enums import QuestionTypes, Colours

LANGUAGE = 'Hebrew'  # 'Hebrew'


class GraphGameScreen(Screen):
    real_user = True
    game_number = -1
    main_app = None
    score = 0

    max_turns = -1
    graph = None
    graph_config = None
    button_presses = None

    graph_game = None

    def setup(self, graph, graph_config, main_app, max_turns, button_presses, number=-1, button_ratio=0.2, real_user=True):
        """
        Does a single run of a game - 3 stages:
        Graph learning - the main game section.
        Questionnaire - A list of questions about the graph
        Results - The result screen and summary of the data.
        :param graph_config:
        :param real_user: Bool. False if machine player
        :param number: The game number
        :param main_app: The main who called this screen
        :param max_turns: Number of steps for the game
        :param graph: The graph used in this specific game
        """
        # Init
        self.size = (200, 100)
        self.game_number = number
        self.main_app = main_app
        self.real_user = real_user
        self.score = 0

        self.graph = graph
        self.max_turns = max_turns
        main_app.discovered_graph = None
        self.graph_config = graph_config
        self.button_presses = button_presses
        self.button_ratio = button_ratio

        self.graph_game = GraphTabletGame(self)

    def on_enter(self, *args):
        log_str = 'start,'
        log_str += 'turns=' + str(self.graph_game.max_turns) + ','
        KL.log.insert(action=LogAction.data, obj='game_graph_' + str(self.game_number), comment=log_str)

        self.button_presses = []

        self.graph_game.load()

    def end_graph(self):
        self.graph_game.the_end = True
        if not self.graph_game.is_playing:

            self.main_app.discovered_graph = self.graph_game.current_data_handler.cleaned_graph()
            self.main_app.true_graph = self.graph
            self.next_game()

    def next_game(self):
        log_str = 'end game'
        KL.log.insert(action=LogAction.data, obj='game_graph_' + str(self.game_number), comment=log_str)
        try:
            self.main_app.sm.current = 'game_questionnaire_' + str(self.game_number)
        except Exception as e:
            KL.log.insert(action=LogAction.data, obj='game_graph_', comment='the_end - {}'.format(e), sync=True)
            self.graph_game.is_playing = True
