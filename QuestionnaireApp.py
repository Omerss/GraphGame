#!/usr/bin/kivy
# -*- coding: utf-8 -*-
from kivy.clock import Clock
from kivy_communication import *
from kivy.uix.screenmanager import Screen

from Questions.QuestionObject import QuestionObject
from Questions.QuestionsDisplay import QuestionDisplay
from SupplementaryFiles.Enums import QuestionTypes, Colours

LANGUAGE = 'Hebrew'  # 'Hebrew'


class QuestionnaireScreen(Screen):
    real_user = True
    game_number = -1
    parent_app = None
    score = 0

    question_list = []
    user_answers = []
    questionnaire = None

    def setup(self, parent_app, number=-1, real_user=True):
        """
        :param real_user: Bool. False if machine player
        :param number: The game number
        :param parent_app: The parent who called this screen
        """
        # Init
        self.size = (200, 100)
        self.game_number = number
        self.parent_app = parent_app
        self.real_user = real_user
        self.question_list = self.create_questions()
        parent_app.user_answers = []

        self.questionnaire = QuestionDisplay(self)

    def on_enter(self, *args):
        log_str = 'start,'
        KL.log.insert(action=LogAction.data, obj='game_' + str(self.game_number), comment=log_str)

        self.questionnaire.load()

    def end_questionnaire(self):
        self.questionnaire.the_end = True
        if not self.questionnaire.is_playing:
            self.next_game()

    def next_game(self):
        log_str = 'end game'
        KL.log.insert(action=LogAction.data, obj='game_' + str(self.game_number), comment=log_str)

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
