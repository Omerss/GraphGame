import unittest
import time
from mock import MagicMock, Mock, patch

from CreateRandGraph import create_rand_graph
from DummyAlgo.BasicGamer import BasicGamer, read_data_from_window
from GraphObj import GraphObject
from NodeObject import NodeObject


MIN_VALUE = 0.0001
MAX_VALUE = 1


class TestNode(unittest.TestCase):

    @patch('DummyAlgo.BasicGamer.read_data_from_window')
    def test_data_collection(self, mock_reader):
        # Assemble
        new_graph = create_rand_graph("../config.ini")
        gamer = BasicGamer("../config.ini")

        nodes_list = []
        edges = []

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
        self.add_empty_edge(new_graph, nodes_list, edges)
        self.add_empty_edge(new_graph, nodes_list, edges)
        self.add_empty_edge(new_graph, nodes_list, edges)

        mock_reader.return_value = {'nodes': nodes_list, 'edges': edges}

        # act
        gamer.do_move()
        time.sleep(1)

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




