
import unittest
from NodeObject import NodeObject
from GraphObj import GraphObject
import math
from random import random
from SaveGraph import save_graph
from LoadGraph import load_graph
from Enums import Colours, Shapes
from NodeObject import NodeObject

class TestNode(unittest.TestCase):

    def test_create_graph(self):
        # Arrange
        new_graph = GraphObject()
        new_graph.add_node(300,300)
        new_graph.add_node(500,500)
        #Act

        save_graph(new_graph,"mew2.xml")
        new_graph = load_graph ("mew2.xml")

        #Assert
        assert (len(new_graph.node_list) == 2)
        assert (new_graph.line_colour ==Colours.white)
        assert (new_graph.extra_distance == 25)
        assert (new_graph.max_neighbors == 5)


if __name__ == '__main__':
    unittest.main()










