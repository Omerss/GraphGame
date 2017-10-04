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
    main_app = None

    questionnaire = None

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
        self.main_app.question_list = self.create_questions()
        self.main_app.user_answers = []

        self.questionnaire = QuestionDisplay(self)

    def on_enter(self, *args):
        log_str = 'start,'
        KL.log.insert(action=LogAction.data, obj='game_' + str(self.game_number), comment=log_str)

        self.questionnaire.load()

    def end_questionnaire(self):
        self.next_game()

    def next_game(self):
        log_str = 'end game'
        KL.log.insert(action=LogAction.data, obj='game_questionnaire_' + str(self.game_number), comment=log_str)

        try:
            self.main_app.sm.current = 'game_results_' + str(self.game_number)

        except Exception as e:
            KL.log.insert(action=LogAction.data, obj='game_questionnaire_', comment='the_end - {}'.format(e), sync=True)
            self.questionnaire.is_playing = True

    def end_subject(self):
        self.the_app.stop()

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
