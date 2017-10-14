#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import path, getcwd, listdir

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from LoginScreen import LoginScreen
from QuestionnaireScreen import QuestionnaireScreen
from ResultsScreen import ResultScreen
from GraphGameScreen import GraphGameScreen
from SupplementaryFiles.LoadGraph import load_graph_from_json
from SupplementaryFiles.Utils import Utils
from SupplementaryFiles.GLogger import *
CONFIG_FILE_PATH = "game_config.txt"
GRAPH_CONFIG_PATH = "graph_config.txt"


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
    user_id = None
    logger = None
    def build(self):
        self.config = Utils.read_game_config_file(CONFIG_FILE_PATH)
        Utils.read_graph_config_file(GRAPH_CONFIG_PATH)
        self.logger = GLogger(self.config['Default']['logger_output_type'], self.config['Default']['logger_writing_location'],self.config['Default']['log_level'], self.user_data_dir)
        #self.init_communication(self.config['Cloud']['server_ip'])
        graph_config_path = self.config['Default']['graph_config_path']
        self.sm = ScreenManager()

        # Setting up the login screen separately
        login_screen = LoginScreen(name='LoginScreen')
        login_screen.setup(main_app=self)
        login_screen.add_widget(login_screen.display.layout)
        self.sm.add_widget(login_screen)

        graph_list = self.load_graphs_from_folder()

        self.current_graph = None
        self.discovered_graph = None
        self.user_answers = []
        self.question_list = []
        self.button_presses = []
        # Enumerate over all the graphs in the folder
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

        self.sm.current = 'LoginScreen'
        return self.sm

    def init_communication(self, server_ip):
        """
        Initiolize the communication protocol to the server.
        """
        # KC.start(the_ip=server_ip, the_parents=[self])
        # KL.start(mode=[DataMode.file], pathname=self.user_data_dir)
        pass

    @staticmethod
    def on_connection():
        GLogger.log(logging.INFO,"", action=LogAction.data, obj='GraphGameApp', comment='start')
        pass

    def press_start(self):
        self.sm.current = 'game_graph_0'

    def load_graphs_from_folder(self):
        graph_list = []
        graph_folder = path.join(getcwd(), self.config['Default']['graphs_folder'])
        for graph_name in [item for item in listdir(graph_folder) if item.endswith(".json")]:
            graph_file_path = path.join(".", graph_folder, str(graph_name))
            current_graph = load_graph_from_json(graph_file_path)
            graph_list.append(current_graph)
        return graph_list


if __name__ == '__main__':
    GraphGameMainApp().run()

