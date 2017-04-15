import unittest


from NodeObject import NodeObject
from DummyAlgo.GameDataHandler import GameDataHandler


class TestGameDataHandling(unittest.TestCase):

    def test_get_furthest_nodes(self):
        node_1 = NodeObject(serial=1, location={'x': 1, 'y': 1}, size=1, real=True)
        node_2 = NodeObject(serial=2, location={'x': 2, 'y': 2}, size=1, real=True)
        node_3 = NodeObject(serial=3, location={'x': 3, 'y': 3}, size=1, real=True)
        node_4 = NodeObject(serial=4, location={'x': 4, 'y': 4}, size=1, real=True)
        res = GameDataHandler.get_furthest_nodes(node_1, node_2, node_3, node_4)

        self.assertIn(node_1.serial_num, res, "node with serial number {0} was not returned by function. Got {1}".format(node_1.serial_num, res))
        self.assertIn(node_4.serial_num, res, "node with serial number {0} was not returned by function. Got {1}".format(node_4.serial_num, res))

    def test_connect_nodes(self):
