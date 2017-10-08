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

    draft_graph = GraphObject(max_x=2000, max_y=2000, node_count=10 , max_neighbors=max_neighbors,
                              extra_distance=extra_distance)
    draft_graph.add_node(x_loc=20, y_loc=1750, node_colour=Colours['blue'], serial="n1")
    draft_graph.add_node(x_loc=201, y_loc=1700, node_colour=Colours['yellow'], serial="n2")
    draft_graph.add_node(x_loc=500, y_loc=1640, node_colour=Colours['yellow'], serial="n3")
    draft_graph.add_node(x_loc=700, y_loc=1850, node_colour=Colours['yellow'], serial="n4")
    draft_graph.add_node(x_loc=750, y_loc=1350, node_colour=Colours['red'], serial="n5")
    draft_graph.add_node(x_loc=850, y_loc=1100, node_colour=Colours['red'], serial="n6")
    draft_graph.add_node(x_loc=650, y_loc=1050, node_colour=Colours['red'], serial="n7")
    draft_graph.add_node(x_loc=600, y_loc=750, node_colour=Colours['blue'], serial="n8")
    draft_graph.add_node(x_loc=1050, y_loc=700, node_colour=Colours['yellow'], serial="n9")
    draft_graph.add_node(x_loc=900, y_loc=800, node_colour=Colours['yellow'], serial="n10")
    # draft_graph.add_node(x_loc=20, y_loc=1750, node_colour=Colours['blue'], serial="n11")
    # draft_graph.add_node(x_loc=20, y_loc=1750, node_colour=Colours['yellow'], serial="n12")

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
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n10"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))

    # save_graph(draft_graph, "the_draft_graph.xml")
    return draft_graph
