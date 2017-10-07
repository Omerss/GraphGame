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