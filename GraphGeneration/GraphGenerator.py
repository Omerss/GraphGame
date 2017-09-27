import itertools
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
        F = open("saved_steps.txt", 'w')
        #steps = ""
        for i in range(0,4096):
            buttons = iter.next()
            answer = run_buttons_on_graph(graph,buttons)
            #sucsess_marker = sucsess_marker + answer
            F.write("stpes"+str(buttons)+"nodes"+str(answer)+"\n")
            if sucsess_marker > 1:
                #steps = ""
                sucsess_marker = 0
                break
            #if answer ==1:
                #steps = buttons
        #if sucsess_marker== 1:
        sucsess_marker =1
        F.close()




def run_buttons_on_graph(graph, buttons):
    game = GraphTabletGame(graph, None, None)
    data_handler = GameDataHandler(CONFIG_FILE_PATH)
    data_handler.add_view_to_db(game.get_info_from_screen())
    for i in range(0,6):
        #print ("\n"+str(i)+"meow \n")
        game.press_button(int(buttons[i]))
        data_handler.add_view_to_db(game.get_info_from_screen())
  #  if data_handler.get_number_of_known_nodes== len(graph.node_list):
   #     return 1
 #   else:
#        return 0
    print ("known nodes-"+str(data_handler.get_number_of_known_nodes())+"\n")
    return data_handler.get_number_of_known_nodes()

if __name__ == "__main__":
    main()