import itertools
from SupplementaryFiles.CreateRandGraph import create_rand_graph
from kivyFiles.GraphTabletGame import GraphTabletGame
from SupplementaryFiles.SaveGraph import save_graph
#create each permutation of buttons and save them in an array

#create and save one random graph
#run the button permutaion
# get the full graph that seen
# get the number of node seen
# put 0 if the #of node seen < #nodes in the graph
CONFIG_FILE_PATH = "./config.ini"

def main ():
    iter = itertools.product('1234', repeat=10)
    sucsess_marker = 0
    while not sucsess_marker:
        graph = create_rand_graph(CONFIG_FILE_PATH)
        steps = ""
        for i in range(0,1048576):
            buttons = iter.next()
            answer = run_buttons_on_graph(graph,buttons)
            sucsess_marker = sucsess_marker + answer
            if sucsess_marker > 1:
                steps = ""
                sucsess_marker = 0
                break
            if answer ==1:
                steps = buttons
        if sucsess_marker== 1:
            sucsess_marker =0
            save_graph(graph, "saved_rand_graph.xml")
            F =open("saved_steps.txt",'w')
            F.write(str(steps))
            F.close()
def run_buttons_on_graph(graph, buttons):
    GraphTabletGame()
    #press buttons
    #get user graph
    seen_graph =None
    #ask Tal and Omer about ghost nodes
    if len(seen_graph.node_list) == len(graph.node_list):
        return 1
    else:
        return 0
