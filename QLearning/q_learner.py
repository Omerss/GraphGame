import logging
from random import random, randrange, randint

from numpy import mean

from SupplementaryFiles import Utils
from SupplementaryFiles.GameDataHandler import GameDataHandler
from SupplementaryFiles.LoadGraph import load_graph_from_file
from SupplementaryFiles.Utils import read_config_file
from kivyFiles.GraphTabletGame import GraphTabletGame

EPSILON = 0.1
GAMMA = 0.8
ALPHA = 0.1

MAIN_CONFIG_FILE_PATH = "../config.ini"
GRAPH_CONFIG_FILE = "../GraphsData/graph_config.ini"


class QMatrix:
    moves_arr = []
    reword_arr = []

    action_space = 4
    first_step = 0  # The first step taken by the QMatrix
    prev_step = 0  # The previous step taken by the matrix
    num_old_nodes = 0
    nodes_in_graph = 10

    def __init__(self, action_space, step_count, nodes_in_graph):
        """

        :param action_space:
        """
        self.action_space = action_space
        self.prev_step = 0
        self.num_old_nodes = 0
        self.nodes_in_graph = nodes_in_graph
        self.reword_arr = []
        self.moves_arr = []
        for i in range(4):
            self.moves_arr.append([])
            self.reword_arr.append([])
            for _ in range(4):
                self.moves_arr[i].append(0.1)
                self.reword_arr[i].append(0)

    def init_q_array(self):
        pass

    def init_reqord_array(self):
        pass

    def max_args(self):
        """
        looks at the matrix. chooses option with highest percentage
        """
        return self.moves_arr[self.prev_step].index(max(self.moves_arr[self.prev_step]))

    def choose_action_epsilon_greedy(self, force_random=False):
        if force_random or random() < EPSILON:
            return randint(1, self.action_space) - 1
        else:
            return self.max_args()
        # Maybe not use greedy??

    def update_matrix(self, num_nodes, current_step):
        #improvement_score = float(num_nodes)/float(self.num_old_nodes)
        improvement_score = float(num_nodes)/float(self.nodes_in_graph)
        rsa = self.reword_arr[self.prev_step][current_step]
        qsa = self.moves_arr[self.prev_step][current_step]
        # = qsa + ALPHA * (rsa + GAMMA * max(self.moves_arr[current_step][:]) - qsa)
        new_q = qsa + ALPHA * (improvement_score + GAMMA * max(self.moves_arr[current_step][:]) - qsa)
        self.moves_arr[self.prev_step][current_step] = new_q
        # self.reword_arr[self.prev_step][current_step] = mean(self.reword_arr[self.prev_step][current_step],
        #                                                      improvement_score)
        self.prev_step = current_step


class QPlayer:

    def __init__(self):
        pass

    def main(self):
        read_config_file(MAIN_CONFIG_FILE_PATH, True)
        log = logging.getLogger()
        log.setLevel(Utils.config['Default']['log_level'])
        session_length = 1000
        graph_path = "../GraphsData/Graph_1.xml"
        graph = load_graph_from_file(graph_path)
        q_matrix = QMatrix(action_space=4, step_count=int(Utils.config['Default']['max_turns']), nodes_in_graph=len(graph.node_list))
        for i in range(session_length):
            dummy_screen = DummyScreen(graph)
            game = GraphTabletGame(dummy_screen)
            data_handler = GameDataHandler(GRAPH_CONFIG_FILE, graph.size)
            data_handler.add_view_to_db(game.get_info_from_screen())
            log.info("Q session {}:{}".format(i, session_length))
            for i in range(1, int(Utils.config['Default']['max_turns'])):
                log.debug("doing a step {}/{}".format(i, Utils.config['Default']['max_turns']))
                btn = q_matrix.choose_action_epsilon_greedy(True)
                game.press_button(btn + 1)
                data_handler.add_view_to_db(game.get_info_from_screen())
                q_matrix.update_matrix(num_nodes=len(data_handler.get_real_nodes()), current_step=btn)
        print(q_matrix)


class DummyScreen:
    graph = None
    graph_config = GRAPH_CONFIG_FILE
    max_turns = 0
    button_presses = []
    button_ratio = 0.2

    def __init__(self, graph):
        self.graph = graph
        self.real_user = False
        self.max_turns = int(Utils.config['Default']['max_turns'])

    def end_graph(self):
        self.graph_game.the_end = True
        if not self.graph_game.is_playing:
            pass

    def end_game(self):
        print ("end game \n")


player = QPlayer()
player.main()