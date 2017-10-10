import unittest
from kivyFiles.GraphTabletGame import GraphTabletGame
from SupplementaryFiles.Enums import Colours
from SupplementaryFiles.GraphObj import GraphObject
from SupplementaryFiles.SaveGraph import save_graph
from SupplementaryFiles.LoadGraph import load_graph_from_file
import threading


def create_draft_graph():
    # Arrange
    max_neighbors = 5
    extra_distance = 1

    draft_graph = GraphObject(max_x=2000, max_y=2000, node_count=10 , max_neighbors=max_neighbors,
                            extra_distance=extra_distance)
    draft_graph.add_node(0, 50, node_colour=Colours['yellow'])
    draft_graph.add_node(100, 100, node_colour=Colours['red'])
    draft_graph.add_node(200, 150, node_colour=Colours['red'])
    draft_graph.add_node(300, 200, node_colour=Colours['blue'])
    draft_graph.add_node(400, 250, node_colour=Colours['blue'])
    draft_graph.add_node(500, 300, node_colour=Colours['yellow'])
    draft_graph.add_node(600, 350, node_colour=Colours['yellow'])
    draft_graph.add_node(700, 400, node_colour=Colours['red'])
    draft_graph.add_node(800, 450, node_colour=Colours['red'])
    draft_graph.add_node(900, 500, node_colour=Colours['blue'])
    draft_graph.add_node(1000, 550, node_colour=Colours['blue'])
    draft_graph.add_node(1100, 600, node_colour=Colours['yellow'])

    for node in draft_graph.node_list:
        draft_graph.get_possible_connections(node.serial_num)

    draft_graph.connect_nodes (draft_graph.node_list[0],draft_graph.node_list[1])
    draft_graph.connect_nodes (draft_graph.node_list[1],draft_graph.node_list[2])
    draft_graph.connect_nodes (draft_graph.node_list[2],draft_graph.node_list[3])
    draft_graph.connect_nodes (draft_graph.node_list[3],draft_graph.node_list[4])
    draft_graph.connect_nodes (draft_graph.node_list[4],draft_graph.node_list[5])
    draft_graph.connect_nodes (draft_graph.node_list[5],draft_graph.node_list[6])
    draft_graph.connect_nodes (draft_graph.node_list[6],draft_graph.node_list[7])
    draft_graph.connect_nodes (draft_graph.node_list[7],draft_graph.node_list[8])
    draft_graph.connect_nodes (draft_graph.node_list[8],draft_graph.node_list[9])
    draft_graph.connect_nodes (draft_graph.node_list[9],draft_graph.node_list[10])
    draft_graph.connect_nodes (draft_graph.node_list[10],draft_graph.node_list[11])

    save_graph(draft_graph, "the_draft_graph.xml")
create_draft_graph()


def create_draft_graph2():
    # Arrange
    max_neighbors = 5
    extra_distance = 1

    draft_graph = GraphObject(max_x=1050, max_y=1800, node_count=10 , max_neighbors=max_neighbors,
                              extra_distance=extra_distance)
    draft_graph.add_node(x_loc=60, y_loc=1250, node_colour=Colours['blue'], serial="n1")
    draft_graph.add_node(x_loc=211, y_loc=1400, node_colour=Colours['yellow'], serial="n2")
    draft_graph.add_node(x_loc=510, y_loc=1140, node_colour=Colours['blue'], serial="n3")
    draft_graph.add_node(x_loc=710, y_loc=1350, node_colour=Colours['blue'], serial="n4")
    draft_graph.add_node(x_loc=760, y_loc=850, node_colour=Colours['red'], serial="n5")
    draft_graph.add_node(x_loc=860, y_loc=600, node_colour=Colours['red'], serial="n6")
    draft_graph.add_node(x_loc=560, y_loc=500, node_colour=Colours['red'], serial="n7")
    draft_graph.add_node(x_loc=610, y_loc=350, node_colour=Colours['blue'], serial="n8")
    draft_graph.add_node(x_loc=511, y_loc=100, node_colour=Colours['red'], serial="n14")
    draft_graph.add_node(x_loc=990, y_loc=350, node_colour=Colours['yellow'], serial="n9")
    draft_graph.add_node(x_loc=311, y_loc=550, node_colour=Colours['blue'], serial="n10")
    draft_graph.add_node(x_loc=150, y_loc=852, node_colour=Colours['red'], serial="n11")
    draft_graph.add_node(x_loc=25, y_loc=910, node_colour=Colours['yellow'], serial="n12")
    draft_graph.add_node(x_loc=212, y_loc=940, node_colour=Colours['blue'], serial="n13")
    draft_graph.add_node(x_loc=82, y_loc=1780, node_colour=Colours['blue'], serial="n15")
    draft_graph.center_node = "n2"

    for node in draft_graph.node_list:
        draft_graph.get_possible_connections(node.serial_num)

    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n2"), draft_graph.get_node_by_serial("n3"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n5"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n6"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n10"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n11"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n11"), draft_graph.get_node_by_serial("n12"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n11"), draft_graph.get_node_by_serial("n13"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n14"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n7"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n2"), draft_graph.get_node_by_serial("n15"))

    # save_graph(draft_graph, "the_draft_graph2.xml")
    return draft_graph

create_draft_graph2()