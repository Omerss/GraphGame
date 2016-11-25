import unittest
from NodeObject import NodeObject


class test_node(unittest.TestCase):
    def test_distance_between_nodes(self):
        node1 = NodeObject(serial=1, location={'x': 1, 'y': 3}, size=1)
        node2 = NodeObject(serial=2, location={'x': 5, 'y': 8}, size=1)
        actual_distance = 0


if __name__ == '__main__':
    unittest.main()