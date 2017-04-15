import unittest

import time
from mock import MagicMock, Mock, patch

from CreateRandGraph import create_rand_graph
from GraphObj import GraphObject
from NodeObject import NodeObject
from DummyAlgo.GameDataHandler import GameDataHandler, read_data_from_window

MIN_VALUE = 0.0001
MAX_VALUE = 1


class TestGameDataHandling(unittest.TestCase):

    def test_get_furthest_nodes(self):
        # Assemble
        node_1 = NodeObject(serial=1, location={'x': 1, 'y': 1}, size=1, real=True)
        node_2 = NodeObject(serial=2, location={'x': 2, 'y': 2}, size=1, real=True)
        node_3 = NodeObject(serial=3, location={'x': 3, 'y': 3}, size=1, real=True)
        node_4 = NodeObject(serial=4, location={'x': 4, 'y': 4}, size=1, real=True)

        # Act
        res = GameDataHandler.get_furthest_nodes(node_1, node_2, node_3, node_4)

        # Assert
        self.assertIn(node_1.serial_num, res, "node with serial number {0} was not returned by function."
                                              " Got {1}".format(node_1.serial_num, res))
        self.assertIn(node_4.serial_num, res, "node with serial number {0} was not returned by function."
                                              " Got {1}".format(node_4.serial_num, res))

    @patch('DummyAlgo.GameDataHandler.GraphObject.connect_nodes')
    @patch('DummyAlgo.GameDataHandler.GraphObject.get_node_by_serial')
    def test_connect_nodes(self, mock_get_node_by_serial, mock_connect_nodes):
        # Assemble
        node_1 = NodeObject(serial=1, location={'x': 1, 'y': 1}, size=1, real=True)
        node_2 = NodeObject(serial=2, location={'x': 2, 'y': 2}, size=1, real=True)

        mock_get_node_by_serial.side_effect = [node_1, node_2]
        mock_connect_nodes.return_value = None
        data_handler = GameDataHandler(None)

        # Act
        data_handler.connect_nodes(node_1, node_1)

        # Assert
        self.assertIn((node_1, node_2), data_handler.extra_edges)

    def test_two_edges_are_one(self):
        # Assemble
        node_1 = NodeObject(serial=1, location={'x': 100, 'y': 100}, size=1, real=True)
        node_2 = NodeObject(serial=2, location={'x': 200, 'y': 200}, size=1, real=True)
        node_3 = NodeObject(serial=3, location={'x': 300, 'y': 300}, size=1, real=True)
        node_4 = NodeObject(serial=4, location={'x': 400, 'y': 400}, size=1, real=True)
        node_5 = NodeObject(serial=4, location={'x': 100, 'y': 400}, size=1, real=True)

        # Act
        res_miss = GameDataHandler.two_edges_are_one((node_3, node_5), (node_2, node_4))
        res_not_sure = GameDataHandler.two_edges_are_one((node_1, node_2), (node_3, node_4))
        res_hit = GameDataHandler.two_edges_are_one((node_1, node_3), (node_2, node_4))
        res_hit_same_point = GameDataHandler.two_edges_are_one((node_1, node_2), (node_1, node_3))
        res_same_edge = GameDataHandler.two_edges_are_one((node_1, node_2), (node_1, node_2))

        # Assert
        self.assertFalse(res_not_sure)
        self.assertFalse(res_miss)
        self.assertTrue(res_hit)
        self.assertTrue(res_hit_same_point)
        self.assertTrue(res_same_edge)

    @patch('DummyAlgo.GameDataHandler.read_data_from_window')
    def test_data_collection(self, mock_reader):
        # WIP
        return
        # Assemble
        new_graph = create_rand_graph("../config.ini")
        gamer = GameDataHandler("../config.ini")

        nodes_list = []
        edges = []

        def add_empty_edge(self, graph, nodes_list, edges_list):
            for node in graph.node_list:
                if node not in nodes_list:
                    for friend in node.neighbors:
                        if friend in [item.serial_num for item in nodes_list]:
                            tmp_node = graph.get_node_by_serial(friend)
                            fake_node_1 = NodeObject(serial=None, location={'x': node.x, 'y': node.y},
                                                   size=node.size, real=False)
                            fake_node_2 = NodeObject(serial=None, location={'x': tmp_node.x, 'y': tmp_node.y},
                                                   size=tmp_node.size, real=False)
                            edges_list.append((fake_node_1, fake_node_2))
                            return

        for i in range(3):
            nodes_list.append(new_graph.node_list[i])
        # Add an extra node that is connected to one of the existing ones

        for node in nodes_list[0].neighbors:
            if node not in nodes_list:
                nodes_list.append(new_graph.get_node_by_serial(node))
                break
        for node in nodes_list:
            for friend in node.neighbors:
                if friend in [item.serial_num for item in nodes_list]:
                    edges.append((node, new_graph.get_node_by_serial(friend)))
                else:
                    origin_node = new_graph.get_node_by_serial(friend)
                    fake_node = NodeObject(serial=None, location={'x':origin_node.x,'y':origin_node.y}, size=origin_node.size, real=False)
                    edges.append((node, fake_node))

        # clean nodes
        for node in nodes_list:
            node.neighbors = set()
            node.possible_neighbors = set()

        # Add a few empty edges
        add_empty_edge(new_graph, nodes_list, edges)
        add_empty_edge(new_graph, nodes_list, edges)
        add_empty_edge(new_graph, nodes_list, edges)

        mock_reader.return_value = {'nodes': nodes_list, 'edges': edges}

        # act
        gamer.do_move()
        time.sleep(1)

