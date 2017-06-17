import unittest

from SupplementaryFiles.Enums import Colours
from SupplementaryFiles.GraphObj import GraphObject
from SupplementaryFiles.SaveGraph import save_graph


class TestSaveGraph(unittest.TestCase):
    # Arrange
    max_neighbors = 5
    extra_distance = 1
    # Act
    new_graph = GraphObject(max_x=1000, max_y=1000, node_count=20, max_neighbors=max_neighbors,
                            extra_distance=extra_distance)
    new_graph.add_node(x_coor, y_coor, node_colour=size)
    new_graph.add_node(x_coor, y_coor, node_colour=size)
    new_graph.add_node(x_coor, y_coor, node_colour=size)
    new_graph.add_node(x_coor, y_coor, node_colour=size)
    new_graph.add_node(x_coor, y_coor, node_colour=size)









