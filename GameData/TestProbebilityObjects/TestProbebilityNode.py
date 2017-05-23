import unittest
from GameData.ProbabilityObjects import ProbabilityNode

MIN_VALUE = 0.0001
MAX_VALUE = 1


class TestNode(unittest.TestCase):

    def test_distance_between_nodes(self):

        node1 = ProbabilityNode(100, 100)
        node1.extrapulate_equation_from_points(50, 50)
        print node1.location_equation

