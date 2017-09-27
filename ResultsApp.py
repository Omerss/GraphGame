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


class GameScreen(Screen):
    real_user = True
    game_number = -1
    parent_app = None
    score = 0

    questions = []
    user_answers = []
    questionnaire = None

    def setup(self, parent_app, number=-1, real_user=True):
        """
        Does a single run of a game - 3 stages:
        Graph learning - the main game section.
        Questionnaire - A list of questions about the graph
        Results - The result screen and summary of the data.
        :param graph_config:
        :param real_user: Bool. False if machine player
        :param number: The game number
        :param parent_app: The parent who called this screen
        :param max_turns: Number of steps for the game
        :param graph: The graph used in this specific game
        """
        # Init
        self.size = (200, 100)
        self.game_number = number
        self.parent_app = parent_app
        self.real_user = real_user
        self.questions = self.create_questions()
        self.user_answers = []

        self.questionnaire = QuestionDisplay(self)

    def on_enter(self, *args):
        log_str = 'start,'
        log_str += 'turns=' + str(self.graph_game.number_of_turns) + ','
        KL.log.insert(action=LogAction.data, obj='game_' + str(self.game_number), comment=log_str)

        self.graph_game.load(network=self.game_network,
                             questions=self.game_questions,
                             edges=self.game_edges)
        Clock.schedule_once(self.explanation_screen, 0.5)

    def explanation_screen(self):
        self.graph_game.start()
        self.graph_game.tell_story(self.game_introduction[0], self.game_introduction[1])
        Clock.schedule_once(self.end_game, self.graph_game.game_duration)

    def end_graph(self):
        # Stage 2 - Questionnaire
        self.questions = self.create_questions()
        self.user_answers = []
        self.questionnaire = QuestionDisplay(self)

    def end_questionnaire(self):
        self.full_answers = []
        for item in self.user_answers:
            print("question #{} - {}".format(item.question_number, item.get_answer()))

        for item in self.user_answers:
            self.full_answers.append(AnswerObject(question_object=item,
                                                  user_seen_graph=self.current_data_handler.graph,
                                                  real_graph=self.current_graph))
        self.result_screen = ResultDisplay(self)

    def end_results(self):
        self.graph_game.the_end = True
        if not self.graph_game.is_playing:
            self.next_game()

    def next_game(self):
        log_str = 'end game'
        KL.log.insert(action=LogAction.data, obj='game_' + str(self.game_number), comment=log_str)

        # delete network
        self.graph_game.discovered_network = set()
        for c_name, c in self.graph_game.network.concepts.items():
            c['visible'] = c['level'] == 1

        try:
            self.the_app.sm.current = 'game_' + str(self.game_number + 1)

        except Exception as e:
            KL.log.insert(action=LogAction.data, obj='game', comment='the_end - {}'.format(e), sync=True)
            self.curiosity_game.is_playing = True

    def end_subject(self, *args):
        self.the_app.stop()
        # self.the_app.sm.current = 'zero_screen'

    @staticmethod
    def create_questions():
        """
        Creates a list of QuestionObject
        """
        questionOne = QuestionObject("how many {} nodes there are?", QuestionTypes.NUMBER, 1, Colours['red'])
        questionThree = QuestionObject("how many {} nodes there are?", QuestionTypes.NUMBER, 1, Colours['red'])
        questionFive = QuestionObject("how many {} nodes there are?", QuestionTypes.NUMBER, 1, Colours['red'])
        questionNine = QuestionObject("how many {} nodes there are?", QuestionTypes.NUMBER, 1, Colours['red'])
        questionTen = QuestionObject("how many {} nodes there are?", QuestionTypes.NUMBER, 1, Colours['red'])

        question_list = [questionOne, questionThree, questionFive, questionNine, questionTen]

        return question_list
