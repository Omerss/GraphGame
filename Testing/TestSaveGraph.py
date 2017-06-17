import unittest

from SupplementaryFiles.Enums import Colours
from SupplementaryFiles.GraphObj import GraphObject
from SupplementaryFiles.SaveGraph import save_graph


class TestSaveGraph(unittest.TestCase):
    # Arrange
    max_neighbors = 5
    extra_distance = 1

    new_graph = GraphObject(max_x=1000, max_y=1000, node_count=10 , max_neighbors=max_neighbors,
                            extra_distance=extra_distance)
    new_graph.add_node(150, 100, node_colour=Colours.yellow)
    new_graph.add_node(100, 800, node_colour=Colours.red)
    new_graph.add_node(150, 500, node_colour=Colours.blue)
    new_graph.add_node(150, 300, node_colour=Colours.blue)
    new_graph.add_node(550, 100, node_colour=Colours.red)
    new_graph.add_node(450, 500, node_colour=Colours.yellow)
    new_graph.add_node(350, 600, node_colour=Colours.yellow)
    new_graph.add_node(250, 700, node_colour=Colours.red)
    new_graph.add_node(150, 800, node_colour=Colours.blue)
    new_graph.add_node(50, 900, node_colour=Colours.blue)

    for node in new_graph.node_list:
        new_graph.get_possible_connections(node.serial_num)

    new_graph.connect_nodes (new_graph.node_list[0],new_graph.node_list[1])
    new_graph.connect_nodes (new_graph.node_list[2],new_graph.node_list[3])
    new_graph.connect_nodes (new_graph.node_list[4],new_graph.node_list[5])
    new_graph.connect_nodes (new_graph.node_list[6],new_graph.node_list[7])
    new_graph.connect_nodes (new_graph.node_list[8],new_graph.node_list[9])
    new_graph.connect_nodes (new_graph.node_list[9],new_graph.node_list[0])
    new_graph.connect_nodes (new_graph.node_list[0],new_graph.node_list[3])
    new_graph.connect_nodes (new_graph.node_list[4],new_graph.node_list[8])
    new_graph.connect_nodes (new_graph.node_list[2],new_graph.node_list[5])
    new_graph.connect_nodes (new_graph.node_list[7],new_graph.node_list[3])
    new_graph.connect_nodes (new_graph.node_list[3],new_graph.node_list[1])
    # Act
    save_graph(new_graph, "testSavingGraph.xml")








