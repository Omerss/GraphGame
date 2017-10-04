import itertools

from structlog import get_logger

from SupplementaryFiles.CreateRandGraph import create_rand_graph
from kivyFiles.GraphTabletGame import GraphTabletGame
from SupplementaryFiles.SaveGraph import save_graph
from GameData.GameDataHandler import GameDataHandler
#create each permutation of buttons and save them in an array

#create and save one random graph
#run the button permutaion
# get the full graph that seen
# get the number of node seen
# put 0 if the #of node seen < #nodes in the graph
CONFIG_FILE_PATH = "./config.ini"


def main ():
    iter = itertools.product('1234', repeat=6)
    sucsess_marker = 0

    while not sucsess_marker:
        graph = create_rand_graph(CONFIG_FILE_PATH)
        save_graph(graph, "saved_rand_graph.xml")
        with open("saved_steps.txt", 'w') as f:
            #steps = ""
            for i in range(0,4096):
                buttons = iter.next()
                answer = run_buttons_on_graph(graph,buttons)
                #sucsess_marker = sucsess_marker + answer
                f.write("stpes"+str(buttons)+"nodes"+str(answer)+"\n")
                if sucsess_marker > 1:
                    #steps = ""
                    sucsess_marker = 0
                    break
                #if answer ==1:
                    #steps = buttons
            #if sucsess_marker== 1:
            sucsess_marker =1

class DummyScreen:
    graph = None
    graph_config = CONFIG_FILE_PATH
    max_turns = 6
    button_presses = []
    button_ratio = 0.2

    def __init__(self, graph):
        self.graph = graph

    def end_graph(self):
        self.graph_game.the_end = True
        if not self.graph_game.is_playing:
            pass

    def end_game(self):
        print ("end game \n")


def run_buttons_on_graph(graph, buttons):
    log = get_logger()
    dummy_screen = DummyScreen(graph)
    game = GraphTabletGame(dummy_screen)
    data_handler = GameDataHandler(CONFIG_FILE_PATH)
    data_handler.add_view_to_db(game.get_info_from_screen())
    max_steps = 6
    for i in range(0, max_steps):
        log.info("doing a step {}/{}".format(i, max_steps))
        game.press_button(int(buttons[i]))
        data_handler.add_view_to_db(game.get_info_from_screen())

    print ("known nodes-"+str(data_handler.get_number_of_known_nodes())+"\n")
    return data_handler.get_number_of_known_nodes()


def view_graph(graph_xml_path):
    from GameHandler import GameHandler
    game = GameHandler()
    new_score = game.run_single_game(graph_xml_path, None)



if __name__ == "__main__":
    main()