import logging
from random import random, randrange, randint

from SupplementaryFiles import Utils
from SupplementaryFiles.GameDataHandler import GameDataHandler
from SupplementaryFiles.LoadGraph import load_graph_from_file
from SupplementaryFiles.Utils import read_config_file
from kivyFiles.GraphTabletGame import GraphTabletGame

# https://gist.github.com/kastnerkyle/d127197dcfdd8fb888c2


EPSILON = 0.1
GAMMA = 0.8
ALPHA = 0.1

MAIN_CONFIG_FILE_PATH = "../config.ini"
GRAPH_CONFIG_FILE = "../GraphsData/graph_config.ini"

log = logging.getLogger()


class QMatrix:
    moves_matrix = []

    action_space = 4
    first_step = 0  # The first step taken by the QMatrix, press button 1
    prev_step = 0  # The previous step taken by the matrix
    num_old_nodes = 0
    nodes_in_graph = 10
    max_steps = 0

    def __init__(self, action_space, step_count, nodes_in_graph):
        self.action_space = action_space
        self.prev_step = 0
        self.num_old_nodes = 0
        self.max_steps = step_count
        self.nodes_in_graph = nodes_in_graph
        self.moves_matrix = []
        for i in range(4):
            self.moves_matrix.append([])
            for _ in range(4):
                self.moves_matrix[i].append(0)

    def init_q_array(self):
        pass

    def init_record_array(self):
        pass

    def max_args(self):
        """
        looks at the matrix. chooses option with highest percentage
        """
        return self.moves_matrix[self.prev_step].index(max(self.moves_matrix[self.prev_step]))

    def choose_action_epsilon_greedy(self):
        if random() < EPSILON:
            return randint(1, self.action_space) - 1
        else:
            return self.max_args()
        # Maybe not use greedy??

    def update_matrix(self, num_nodes, current_step):
        """

        :param num_nodes:
        :param current_step:
        :return:
        """

        improvement_score = float(num_nodes)/float(self.nodes_in_graph)
        qsa = self.moves_matrix[self.prev_step][current_step]
        # = qsa + ALPHA * (rsa + GAMMA * max(self.moves_arr[current_step][:]) - qsa)
        new_q = qsa + ALPHA * (improvement_score + GAMMA * max(self.moves_matrix[current_step][:]) - qsa)
        self.moves_matrix[self.prev_step][current_step] = new_q

        # Normalize
        # place = []
        # line_sum = 0
        # for i in range(len(self.moves_arr[self.prev_step])):
        #     if self.moves_arr[self.prev_step][i] > 0:
        #         place.append(i)
        #         line_sum += self.moves_arr[self.prev_step][i]
        # for item in place:
        #     self.moves_arr[self.prev_step][item] =  self.moves_arr[self.prev_step][item]/line_sum

        # self.reword_arr[self.prev_step][current_step] = mean(self.reword_arr[self.prev_step][current_step],
        #                                                      improvement_score)
        self.prev_step = current_step
        return improvement_score


class QPlayer:
    auto_first_press = 0  # the first button press is predetermined

    def __init__(self):
        pass

    def run_q_player(self):
        read_config_file(MAIN_CONFIG_FILE_PATH, True)
        log.setLevel(Utils.config['Default']['log_level'])
        session_length = 200
        graph_path = "../GraphsData/draft_graph2.xml"
        graph = load_graph_from_file(graph_path)
        q_matrix = QMatrix(action_space=4, step_count=int(Utils.config['Default']['max_turns']), nodes_in_graph=len(graph.node_list))
        for i in range(session_length):
            dummy_screen = DummyScreen(graph)
            game = GraphTabletGame(dummy_screen)
            data_handler = GameDataHandler(GRAPH_CONFIG_FILE, graph.size)
            data_handler.add_view_to_db(game.get_info_from_screen())

            rw = 0
            game.press_button(self.auto_first_press + 1)
            for j in range(1, int(Utils.config['Default']['max_turns'])):
                log.debug("doing a step {}/{}".format(j, Utils.config['Default']['max_turns']))
                btn = q_matrix.choose_action_epsilon_greedy() + 1
                game.press_button(btn)
                data_handler.add_view_to_db(game.get_info_from_screen())
                rw = q_matrix.update_matrix(num_nodes=len(data_handler.get_real_nodes()), current_step=btn)
            log.info("Q session {}:{} - reword:{}".format(i, session_length, rw))
        print(q_matrix.moves_matrix)


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
player.run_q_player()