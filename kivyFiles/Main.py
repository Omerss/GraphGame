import os
import kivy
kivy.require('1.9.1')

from SupplementaryFiles.CreateRandGraph import create_rand_graph
from GraphTabletGame import GraphTabletGame
from KivyGraphTester import *
from random import randint


def create_draft_graph2():
    # Arrange
    max_neighbors = 5
    extra_distance = 1

    draft_graph = GraphObject(max_x=2000, max_y=2000, node_count=10 , max_neighbors=max_neighbors,
                              extra_distance=extra_distance)
    draft_graph.add_node(x_loc=50, y_loc=1750, node_colour=Colours['blue'], serial="n1")
    draft_graph.add_node(x_loc=200, y_loc=1700, node_colour=Colours['yellow'], serial="n2")
    draft_graph.add_node(x_loc=500, y_loc=1640, node_colour=Colours['yellow'], serial="n3")
    draft_graph.add_node(x_loc=700, y_loc=1850, node_colour=Colours['yellow'], serial="n4")
    draft_graph.add_node(x_loc=750, y_loc=1350, node_colour=Colours['red'], serial="n5")
    # draft_graph.add_node(x_loc=20, y_loc=1750, node_colour=Colours['yellow'], serial="n6")
    # draft_graph.add_node(x_loc=20, y_loc=1750, node_colour=Colours['yellow'], serial="n7")
    # draft_graph.add_node(x_loc=20, y_loc=1750, node_colour=Colours['red'], serial="n8")
    # draft_graph.add_node(x_loc=20, y_loc=1750, node_colour=Colours['red'], serial="n9")
    # draft_graph.add_node(x_loc=20, y_loc=1750, node_colour=Colours['blue'], serial="n10")
    # draft_graph.add_node(x_loc=20, y_loc=1750, node_colour=Colours['blue'], serial="n11")
    # draft_graph.add_node(x_loc=20, y_loc=1750, node_colour=Colours['yellow'], serial="n12")

    draft_graph.center_node = "n2"

    for node in draft_graph.node_list:
        draft_graph.get_possible_connections(node.serial_num)

    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n2"), draft_graph.get_node_by_serial("n3"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n4"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n5"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))

    # save_graph(draft_graph, "the_draft_graph.xml")
    return draft_graph

if __name__ == "__main__":

    button_presses = []
    # kivy.core.window.Window.size = (800, 600)
    # game = GraphTabletGame(create_rand_graph("{}\..\GraphsData\config.ini".format(os.getcwd())), None, None)
    # game = GraphTabletGame(TestScreen(MyGameLayout.get_graph_obj1(), button_presses, 0.25))
    game = GraphGameApp(TestScreen(create_draft_graph2(), button_presses, 0.25))
    # game = GraphTabletGame(TestScreen(MyGameLayout.get_graph_obj1(), button_presses, 0.25, False))
    #
    # for button in button_presses:
    #     game.press_button(button)
    #
    game.run()
    print button_presses

    # game = DisplayApp(create_rand_graph("{}\..\GraphsData\config.ini".format(os.getcwd())))
    # game.run()
