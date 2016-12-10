
import unittest
from NodeObject import NodeObject
from GraphObj import GraphObject
import math
from random import random

class TestNode(unittest.TestCase):


    def test_create_graph(self):
        # Arrange , # Act
        newGraph = GraphObject()
        # Assert
        assert (newGraph.node_list == [])
        assert (newGraph.extra_distance == 1)
        assert (newGraph.max_neighbors == 4)

    def test_add_node(self):
        # Arrange
        newGraph = GraphObject()

        # Act
        newGraph.add_node(1, 10)

        # Assert
        assert (newGraph.node_list[0].location('x') == 1)
        assert (newGraph.node_list[0].location('y') == 10)
        assert (newGraph.node_list[0].size == 1)
        location = {'x': 1, 'y': 10}
        assert (newGraph.node_list[0].serial == newGraph.get_serial(location))


    def test_get_possible_connections(self):
        # Arrange
        newGraph = GraphObject()

        # Act
        newGraph.add_node(1, 10)
        newGraph.add_node(1, 100)
        newGraph.add_node(1, 200)
        serial = newGraph.node_list[0].serial
        serial2 = newGraph.node_list[1].serial
        serial3 = newGraph.node_list[2].serial
        list = newGraph.get_possible_connections(serial)

        # Assert
        assert (list.__contains__(serial3))
        assert (not (list.__contains__(serial2)))



    def test_get_best_connection(self):
        # Arrange
        newGraph = GraphObject()
        newGraph.add_node(1, 10)
        newGraph.add_node(1, 100)
        newGraph.add_node(1, 200)
        serial = newGraph.node_list[0].serial
        serial3 = newGraph.node_list[2].serial

        # Act
        list = newGraph.get_possible_connections(serial)
        id = newGraph.get_best_connection(list)

        # Assert
        assert (id == serial3)


    def test_get_node_by_serial(self):
        # Arrange
        newGraph = GraphObject()
        newGraph.add_node(1, 10)
        newGraph.add_node(1, 100)
        newGraph.add_node(1, 200)

        # Act
        serial = newGraph.node_list[0].serial
        serial2 = newGraph.node_list[1].serial
        serial3 = newGraph.node_list[2].serial

        # Assert
        assert ((newGraph.get_node_by_serial(serial).location('y')) == 10)
        assert ((newGraph.get_node_by_serial(serial2).location('y')) == 100)
        assert ((newGraph.get_node_by_serial(serial3).location('y')) == 200)


    def test_is_node_far_enough(self):
        # Arrange
        newGraph = GraphObject()
        newGraph.add_node(1, 10)
        newGraph.add_node(1, 100)
        newGraph.add_node(1, 200)
        serial = newGraph.node_list[0].serial
        serial2 = newGraph.node_list[1].serial
        serial3 = newGraph.node_list[2].serial

        # Act

        # Assert
        assert (not(newGraph.is_node_far_enough(newGraph.node_list [1],newGraph.node_list[0],newGraph.node_list[2])))
        assert (newGraph.is_node_far_enough(newGraph.node_list[0], newGraph.node_list [1],newGraph.node_list [2]))


    def test_get_serial(self):
        # Arrange
        newGraph = GraphObject()
        newGraph.add_node(1, 10)
        newGraph.add_node(1, 200)
        serial = newGraph.node_list[0].serial
        serial2 = newGraph.node_list[1].serial

        # Act
        checkSerial = newGraph.get_serial(newGraph.node_list[0])
        checkSerial2 = newGraph.get_serial(newGraph.node_list[1])

        # Assert
        assert (checkSerial == serial)
        assert  (checkSerial2 == serial2)


if __name__ == '__main__':
    unittest.main()










