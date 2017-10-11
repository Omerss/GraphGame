import itertools
import logging

from SupplementaryFiles import Utils
from SupplementaryFiles.GameDataHandler import GameDataHandler
from SupplementaryFiles.LoadGraph import load_graph_from_file
from SupplementaryFiles.Utils import read_config_file
from KivyFiles.GraphTabletDisplay import GraphTabletDisplay
from os import path, listdir

# get the full graph that seen
# get the number of node seen
# put 0 if the #of node seen < #nodes in the graph
MAIN_CONFIG_FILE_PATH = "../config.ini"
GRAPH_CONFIG_FILE = "./config.ini"
SAVED_GRAPH_PATH = "../TestingGraphs"
graphs_names = ["draft_graph_1.xml"]


def main():
    read_config_file(MAIN_CONFIG_FILE_PATH, True)
    max_turns = int(Utils.config['Default']['max_turns'])
    # iter = itertools.product('1234', repeat=int(Utils.config['Default']['MaxTurns']))
    iter = itertools.product('1234', repeat=max_turns)
    number_of_successful_runs = 0
    # for current_graph in [item for item in listdir(SAVED_GRAPH_PATH) if item.endswith(".xml")]:
    for current_graph in graphs_names:
        curr_path = path.join(SAVED_GRAPH_PATH, current_graph)
        graph = load_graph_from_file(curr_path)
        with open("{}_saved_steps.txt".format(curr_path[:-4]), 'w') as f:
            num_of_graph_nodes = len(graph.node_list)
            f.write("The graph contains {} nodes\n".format(str(num_of_graph_nodes)))
            while True:
                try:
                    buttons = iter.next()
                except StopIteration:
                    break
                answer, number_of_nodes_seen = run_buttons_on_graph(graph,buttons)
                number_of_successful_runs = number_of_successful_runs+answer
                f.write("steps: {} seen nodes: {} \n".format(str(buttons), str(number_of_nodes_seen)))

            f.write("number of successful runs = {0}\n".format(number_of_successful_runs))


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


def run_buttons_on_graph(graph, buttons):
    log = logging.getLogger()
    log.setLevel(Utils.config['Default']['log_level'])
    dummy_screen = DummyScreen(graph)
    game = GraphTabletDisplay(dummy_screen)
    #game.run()
    data_handler = GameDataHandler(GRAPH_CONFIG_FILE, graph.size)
    data_handler.add_view_to_db(game.get_info_from_screen())
    for i in range(int(Utils.config['Default']['max_turns'])):
        log.debug("doing a step {}/{}".format(i, Utils.config['Default']['max_turns']))
        game.press_button(int(buttons[i]))
        data_handler.add_view_to_db(game.get_info_from_screen())

    #print ("known nodes-"+str(data_handler.get_number_of_known_nodes())+"\n")
    answer = (data_handler.get_number_of_known_nodes() == len(graph.node_list))
    return answer, data_handler.get_number_of_known_nodes()


def view_graph(graph_xml_path):
    from Old.GameHandler import GameHandler
    game = GameHandler()
    new_score = game.run_single_game(graph_xml_path, None)


if __name__ == "__main__":
    main()
