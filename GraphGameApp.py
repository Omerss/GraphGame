#!/usr/bin/kivy
# -*- coding: utf-8 -*-
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty, ObjectProperty
from kivy.core.audio import SoundLoader
from kivy.uix.floatlayout import FloatLayout
from functools import partial
from kivy.uix.label import Label
from kivy.clock import Clock

from kivy_communication import *
LANGUAGE = 'Hebrew'  # 'Hebrew'
from kivy.uix.screenmanager import Screen
from kivyFiles.GraphTabletGame import GraphTabletGame


class GameScreen(Screen):
    graph_game = None
    real_user = True

    game_number = -1
    the_app = None
    game_type = None
    graph = None
    current_step_count = 0

    config = None
    current_graph = None
    current_data_handler = None
    display = None
    max_turns = 0
    current_turn = 0
    score = 0
    discovered_graph = None

    def start(self, number=-1, the_app=None, the_type=None, max_turns=None, graph=None):
        self.size = (200, 100)
        self.game_number = number
        self.the_app = the_app
        self.game_type = the_type
        self.graph = graph
        self.max_turns = max_turns

        self.current_graph = None
        self.current_data_handler = None
        self.display = None

        self.current_step_count = 0

        self.current_turn = 0
        self.score = 0

        self.graph_game = GraphTabletGame(self)
        self.graph_game.number_of_turns = self.max_turns

        if self.game_number == 0:
            self.graph_game.set_tutorial()

    def on_enter(self, *args):
        log_str = 'start,'
        log_str += 'duration=' + str(self.graph_game.game_duration) + ','
        log_str += 'questions=' + str(self.graph_game.game_questions)
        KL.log.insert(action=LogAction.data, obj='game_'+str(self.game_number), comment=log_str)

        self.graph_game.load(network=self.game_network,
                             questions=self.game_questions,
                             edges=self.game_edges)
        Clock.schedule_once(self.explanation_screen, 0.5)

    def explanation_screen(self, dt):
        self.curiosity_game.start()
        self.curiosity_game.tell_story(self.game_introduction[0], self.game_introduction[1])
        Clock.schedule_once(self.end_game, self.curiosity_game.game_duration)

    def end_game(self, dt):
        self.graph_game.the_end = True
        if not self.graph_game.is_playing:
            self.next_game()

    def next_game(self):
        # log_str = 'end,q_type='
        # for q in self.curiosity_game.game_q_type:
        #     log_str += str(q) + ';'
        # KL.log.insert(action=LogAction.data, obj='game_' + str(self.game_number), comment=log_str)
        #
        # # delete network
        # self.curiosity_game.discovered_network = set()
        # for c_name, c in self.curiosity_game.network.concepts.items():
        #     c['visible'] = c['level'] == 1
        #
        # try:
        #     self.the_app.sm.current = 'game_' + str(self.game_number+1)
        # except:
        #     KL.log.insert(action=LogAction.data, obj='game', comment='the_end', sync=True)
        #     self.curiosity_game.is_playing = True
        #     sl = SoundLoader.load('items/sounds/the_end_Q_World.wav')
        #     sl.bind(on_stop=self.end_subject)
        #     sl.play()
        pass

    def end_subject(self, *args):
        self.the_app.stop()
            # self.the_app.sm.current = 'zero_screen'






