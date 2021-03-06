#!/usr/bin/kivy
# -*- coding: utf-8 -*-
from kivy.uix.screenmanager import Screen
from KivyFiles.GraphTabletDisplay import GraphTabletDisplay
from SupplementaryFiles.GLogger import *
from KivyCommunication import *
from kivy.clock import *
from kivy.core.audio import SoundLoader
from SupplementaryFiles.GraphSaveLoad import save_graph_json
import json

LANGUAGE = 'Hebrew'  # 'Hebrew'
FIRST_GAME_DURATION = 60


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
    event = None

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

        self.graph_game = GraphTabletDisplay(self)

    def on_enter(self, *args):
        log_str = 'start,'
        log_str += 'turns=' + str(self.graph_game.max_turns) + ','
        GLogger.log(logging.INFO,"", action=LogAction.data, obj='game_graph_' + str(self.game_number), comment=log_str)
        self.main_app.current_graph = self.graph
        self.button_presses = []

        self.graph_game.load()
        self.explanation()
        if self.game_number == 0:   # first game is also on timer
            self.event = Clock.schedule_once(self.next_game, FIRST_GAME_DURATION)

    def explanation(self):
        if self.game_number == 1:
            SoundLoader.load('Sounds/6.wav').play()

        if self.game_number > 8:
            pass
            #Goren - add explantion to the last graph
            #SoundLoader.load('Sounds/6.wav').play()

    def end_graph(self):
        KL.log.insert(action=LogAction.data, comment='end graph')
        self.graph_game.the_end = True
        if not self.graph_game.is_playing:
            self.main_app.discovered_graph = self.graph_game.current_data_handler.cleaned_graph()
            self.main_app.current_graph = self.graph
            self.log_graphs()
            self.next_game()

    def log_graphs(self):
        graph_number = self.main_app.sm.screen_names.index(self.main_app.sm.current)
        game_number = self.main_app.sm.screens[graph_number].game_number

        graph_data = save_graph_json(self.main_app.discovered_graph)
        KL.log.insert(action=LogAction.data,
                      obj="game_%d_graph_%d_discovered" % (game_number, graph_number),
                      comment=json.dumps(graph_data), sync=True)

        graph_data = save_graph_json(self.main_app.current_graph)
        KL.log.insert(action=LogAction.data,
                      obj="game_%d_graph_%d_current" % (game_number, graph_number),
                      comment=json.dumps(graph_data), sync=True)

    def next_game(self, *args):
        if self.game_number == 0:
            self.event.cancel()

        log_str = 'end game'
        GLogger.log(logging.INFO,"", action=LogAction.data, obj='game_graph_' + str(self.game_number), comment=log_str)

        try:
            self.main_app.sm.current = 'game_questionnaire_' + str(self.game_number)
        except Exception as e:
            print ("except Exception as e\n")
            GLogger.log(logging.INFO,"", action=LogAction.data, obj='game_graph_', comment='the_end - {}'.format(e), sync=True)
            self.graph_game.is_playing = True
            self.end_subject()

    def end_subject(self):
        #Goren
        #added exiting here, the shutting down is problematic - should we do something like exit(1)?
        KL.log.insert(action=LogAction.data, comment='end game')
        self.main_app.stop()
