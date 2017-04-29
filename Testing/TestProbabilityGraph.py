import random
import unittest

import math

from GameData.ProbabilityGraph import ProbabilityGraph
from GameData.ProbabilityObjects import ProbabilityNode


class TestNode(unittest.TestCase):

    def test_create_graph(self):
        # Arrange
        node_count = 5

        # Act
        new_graph = ProbabilityGraph(node_count)

        # Assert
        assert (new_graph.node_list == [])

    def test_adding_nodes(self):
        # Arrange
        node_count = 5
        new_graph = ProbabilityGraph(node_count)
        node_list = []

        # Act
        for i in range(node_count):
            new_graph.add_node(i * i * 10, i * i * 10, 1 - i * 0.1)
            tmp_node = new_graph.node_list[len(new_graph.node_list) - 1]
            node_list.append(tmp_node)

        # Assert
        for item in node_list:
            assert item in new_graph.node_list

    def test_add_vectors(self):
        # Arrange
        node_count = 5
        new_graph = ProbabilityGraph(node_count)
        node_list = []

        # Act
        for i in range(node_count):
            new_graph.add_vector(i * i * 10, i * i * 10, math.pi * random.randrange(2))
            tmp_node = new_graph.vector_list[len(new_graph.vector_list) - 1]
            node_list.append(tmp_node)

        # Assert
        for item in node_list:
            assert item in new_graph.vector_list