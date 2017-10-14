#!/usr/bin/kivy
# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import Screen
from KivyFiles.Questions.ResultDisplay import ResultDisplay
from SupplementaryFiles.GLogger import *
LANGUAGE = 'Hebrew'  # 'Hebrew'


class ResultScreen(Screen):
    real_user = True
    game_number = -1
    main_app = None

    result_app = None

    def setup(self, main_app, number=-1, real_user=True):
        """
        :param real_user: Bool. False if machine player
        :param number: The game number
        :param main_app: The main app that runs the program. We use it to pass the question list into the page and get
        the answers out of the page.
        """
        # Init
        self.size = (200, 100)
        self.game_number = number
        self.main_app = main_app
        self.real_user = real_user

        self.result_app = ResultDisplay(self)

    def on_enter(self, *args):
        log_str = 'start,'
        GLogger.log(action=LogAction.data, obj='game_results_' + str(self.game_number), comment=log_str)

        self.result_app.load()

    def end_results(self):
        self.result_app.the_end = True
        self.next_game()

    def next_game(self):
        log_str = 'end game'
        GLogger.log(action=LogAction.data, obj='game_results_' + str(self.game_number), comment=log_str)

        try:
            self.main_app.sm.current = 'game_graph_' + str(self.game_number + 1)

        except Exception as e:
            GLogger.log(action=LogAction.data, obj='game_results_', comment='the_end - {}'.format(e), sync=True)
            self.end_subject()

    def end_subject(self):
        self.main_app.stop()
