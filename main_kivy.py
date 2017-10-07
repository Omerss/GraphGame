#!/usr/bin/python
# -*- coding: utf-8 -*-
from kivy.app import App
from os import path, getcwd, listdir
from kivy.uix.screenmanager import ScreenManager, Screen

from QuestionnaireScreen import QuestionnaireScreen
from ResultsScreen import ResultScreen
from SupplementaryFiles import Utils
from kivy_communication import *
from GraphGameScreen import GraphGameScreen
from SupplementaryFiles.LoadGraph import load_graph_from_file
from kivyFiles.KivyGraphTester import MyGameLayout

CONFIG_FILE_PATH = "./config.ini"


class ZeroScreen(Screen):

    def on_enter(self, *args):
        KL.restart()

    def start(self):
        self.ids['subject_id'].bind(text=self.ids['subject_id'].on_text_change)


class GraphGameMainApp(App):
    game_screen = []
    filename = 'network_new.json'

    true_graph = None
    discovered_graph = None
    user_answers = []
    question_list = []
    button_presses = []

    real_user = True

    def build(self):
        self.init_communication()
        self.sm = ScreenManager()

        screen = ZeroScreen()
        screen.start()
        screen.ids['subject_id'].bind(text=screen.ids['subject_id'].on_text_change)
        self.sm.add_widget(screen)

        self.config = Utils.read_config_file(CONFIG_FILE_PATH)
        Utils.image_folder = path.join(getcwd(), self.config['Default']['image_folder'])

        # TODO - Actually get multiple graphs in here
        # graph_list = self.get_graphs()
        graph_list = [MyGameLayout.get_graph_obj()]
        graph_list = [load_graph_from_file(path.join(".","GraphGeneration", "the_draft_graph.xml"))]

        concepts_path = 'items/'
        graph_config = path.join(getcwd(), "GraphsData", "config.ini")

        self.current_graph = None
        self.discovered_graph = None
        self.user_answers = []
        self.question_list = None
        self.button_presses = []

        for i_net, graph_data in enumerate(graph_list):
            # Step 1 - Graph Game
            self.question_list = graph_data.question_object_list
            self.game_screen.append(GraphGameScreen(name='game_graph_' + str(i_net)))
            self.game_screen[-1].setup(number=i_net,
                                       main_app=self,
                                       max_turns=int(self.config['Default']['max_turns']),
                                       real_user=True,
                                       graph=graph_data,
                                       graph_config=graph_config,
                                       button_presses=self.button_presses)
            self.game_screen[-1].add_widget(self.game_screen[-1].graph_game.layout)

            # Step 2 - Questionnaire
            self.game_screen.append(QuestionnaireScreen(name='game_questionnaire_' + str(i_net)))
            self.game_screen[-1].setup(number=i_net,
                                       main_app=self,
                                       real_user=self.real_user)
            self.game_screen[-1].add_widget(self.game_screen[-1].questionnaire.the_widget)

            # Step 3 - Results
            self.game_screen.append(ResultScreen(name='game_results_' + str(i_net)))
            self.game_screen[-1].setup(number=i_net,
                                       main_app=self,
                                       real_user=True)
            self.game_screen[-1].add_widget(self.game_screen[-1].result_app.the_widget)

        for gs in self.game_screen:
            self.sm.add_widget(gs)

        self.sm.current = 'zero_screen'
        return self.sm

    def init_communication(self):
        KC.start(the_ip='192.168.1.254', the_parents=[self])  # 127.0.0.1
        KL.start(mode=[DataMode.file], pathname=self.user_data_dir)

    def on_connection(self):
        KL.log.insert(action=LogAction.data, obj='GraphGameApp', comment='start')

    def press_start(self, pre_post):
        # self.game_screen.curiosity_game.filename = 'items_' + pre_post + '.json'
        self.sm.current = 'game_graph_0'

    def get_graphs(self):
        graphs = []
        graph_folder = path.join(getcwd(), self.config['Default']['graphs'])
        for file in listdir(graph_folder):
            graph_file_path = path.join(graph_folder, str(file))
            current_graph = load_graph_from_file(graph_file_path)
            graphs.append(current_graph)

        return graphs


if __name__ == '__main__':
    GraphGameMainApp().run()

