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

    # Variables that allow passing information between screens
    current_graph = None  # The graph the user is currently playing
    discovered_graph = None  # The graph discovered by the user in the current pipethrough
    user_answers = []
    question_list = []
    button_presses = []

    real_user = True

    def build(self):
        self.config = Utils.read_config_file(CONFIG_FILE_PATH)
        self.init_communication(self.config['Cloud']['server_ip'])
        Utils.image_folder = path.join(getcwd(), self.config['Default']['image_folder'])
        graph_config_path = self.config['Default']['graph_config_path']
        self.sm = ScreenManager()

        screen = ZeroScreen()
        screen.start()
        screen.ids['subject_id'].bind(text=screen.ids['subject_id'].on_text_change)
        self.sm.add_widget(screen)

        graph_list = self.load_graphs_from_folder()
        self.config = Utils.read_config_file(CONFIG_FILE_PATH, True)
        Utils.image_folder = path.join(getcwd(), self.config['Default']['image_folder'])

        self.current_graph = None
        self.discovered_graph = None
        self.user_answers = []
        self.question_list = []
        self.button_presses = []

        graph_list = [load_graph_from_file( path.join(getcwd(), self.config['Default']['graphs_folder'], "draft_graph2.xml"))]

        for i_net, graph_data in enumerate(graph_list):
            # Step 1 - Graph Game
            self.question_list = graph_data.question_object_list
            self.game_screen.append(GraphGameScreen(name='game_graph_' + str(i_net)))
            self.game_screen[-1].setup(number=i_net,
                                       main_app=self,
                                       max_turns=int(self.config['Default']['max_turns']),
                                       real_user=True,
                                       graph=graph_data,
                                       graph_config=graph_config_path,
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

    def init_communication(self, server_ip):
        KC.start(the_ip=server_ip, the_parents=[self])
        KL.start(mode=[DataMode.file], pathname=self.user_data_dir)

    @staticmethod
    def on_connection():
        KL.log.insert(action=LogAction.data, obj='GraphGameApp', comment='start')

    def press_start(self):
        self.sm.current = 'game_graph_0'

    def load_graphs_from_folder(self):
        graph_list = []
        graph_folder = path.join(getcwd(), self.config['Default']['graphs_folder'])
        for graph_name in [item for item in listdir(graph_folder) if item.endswith(".xml")]:
            graph_file_path = path.join(".", graph_folder, str(graph_name))
            current_graph = load_graph_from_file(graph_file_path)
            graph_list.append(current_graph)
        return graph_list


if __name__ == '__main__':
    GraphGameMainApp().run()

