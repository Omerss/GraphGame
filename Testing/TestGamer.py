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
        new_graph = create_rand_graph("../config.ini")
        gamer = BasicGamer("../config.ini")

        nodes = []
        edges = []
        for i in range(3):
            nodes.append(new_graph.node_list[i])
            for friend in new_graph.node_list[i].neighbors:
                edges.append((new_graph.node_list[i], new_graph.get_node_by_serial(friend)))
        mock_reader.return_value = {'nodes': nodes, 'edges': edges}
        for turn in range(10):
            gamer.do_move()
            time.sleep(1)



