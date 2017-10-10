import itertools
import logging

from SupplementaryFiles.GameDataHandler import GameDataHandler
from SupplementaryFiles.LoadGraph import load_graph_from_file
from kivyFiles.GraphTabletGame import GraphTabletGame

# get the full graph that seen
# get the number of node seen
# put 0 if the #of node seen < #nodes in the graph
CONFIG_FILE_PATH = "./graph_config.ini"
SAVED_GRAPH_PATH = "../../Saved_Graphs"
LOG_LEVEL = logging.DEBUG


def main ():
    iter = itertools.product('1234', repeat=6)
    number_of_successful_runs = 0
    sucsess_marker = 0
    while not sucsess_marker:
        #graph = MyGameLayout.get_graph_obj1()
        #graph = create_rand_graph(CONFIG_FILE_PATH)
        #save_graph(graph, path.join(SAVED_GRAPH_PATH, "saved_graph_{}.xml".format(datetime.utcnow().strftime("%H%M%S"))))
        graph = load_graph_from_file("the_draft_graph2.xml")
        with open("saved_steps.txt", 'w') as f:
            #steps = ""
            for i in range(0,4096):
                buttons = iter.next()
                answer, number_of_nodes_seen = run_buttons_on_graph(graph,buttons)
                number_of_successful_runs= number_of_successful_runs+answer
                #sucsess_marker = sucsess_marker + answer
                f.write("stpes"+str(buttons)+"- #seen nodes"+str(number_of_nodes_seen)+"\n")
                #if sucsess_marker > 1:
                    #steps = ""
#                    sucsess_marker = 0
                 #   break
                #if answer ==1:
                    #steps = buttons
            #if sucsess_marker== 1:
            f.write ("number of succesful runs = {0}\n".format(number_of_successful_runs))
            sucsess_marker =1

class DummyScreen:
    graph = None
    graph_config = CONFIG_FILE_PATH
    max_turns = 6
    button_presses = []
    button_ratio = 0.2

    def __init__(self, graph):
        self.graph = graph
        self.real_user = False

    def end_graph(self):
        self.graph_game.the_end = True
        if not self.graph_game.is_playing:
            pass

    def end_game(self):
        print ("end game \n")


def run_buttons_on_graph(graph, buttons):
    log = logging.getLogger()
    log.setLevel(LOG_LEVEL)
    dummy_screen = DummyScreen(graph)
    game = GraphTabletGame(dummy_screen)
    #game.run()
    data_handler = GameDataHandler(CONFIG_FILE_PATH, graph.size)
    data_handler.add_view_to_db(game.get_info_from_screen())
    max_steps = 6
    for i in range(0, max_steps):
        log.debug("doing a step {}/{}".format(i, max_steps))
        game.press_button(int(buttons[i]))
        data_handler.add_view_to_db(game.get_info_from_screen())

    #print ("known nodes-"+str(data_handler.get_number_of_known_nodes())+"\n")
    answer = (data_handler.get_number_of_known_nodes() == len(graph.node_list))
    return answer,data_handler.get_number_of_known_nodes()


def view_graph(graph_xml_path):
    from Old.GameHandler import GameHandler
    game = GameHandler()
    new_score = game.run_single_game(graph_xml_path, None)


if __name__ == "__main__":
    main()
