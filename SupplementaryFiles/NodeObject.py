import math

from Point import Point
from SupplementaryFiles.Enums import Colours, Shapes


class NodeObject(Point):
    serial_num = None
    shape = Shapes.circle
    size = 0
    neighbors = set()
    possible_neighbors = set()
    real = True

    def __init__(self, serial, location, size, colour=Colours.red, shape=Shapes.circle, real=True):
        """

        :param serial:
        :param location: {'x':float, 'y':float}
        :param size:
        :param colour:
        :param shape:
        """
        super(NodeObject, self).__init__(location['x'], location['y'])
        self.serial_num = serial
        self.size = size
        self.colour = colour
        self.shape = shape
        self.neighbors = set()
        self.possible_neighbors = set()
        self.real = real

    def get_num_neighbors(self):
        return len(self.neighbors)

    def distance_from_line(self, node_1, node_2):
        """
        If for some reason we davide by zero we return -1
        :param node_1: NodeObject
        :param node_2: NodeObject
        :return: distance between self and the line between the two points
        """
        # See https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
        y_part = math.fabs(node_2.y - node_1.y)
        x_part = math.fabs(node_2.x - node_1.x)

        dist_part1 = y_part * self.x
        dist_part2 = x_part * self.y
        distance = math.fabs(dist_part1
                             - dist_part2
                             + node_1.y * node_2.x
                             - node_2.y * node_1.x)
        if math.sqrt(y_part ** 2 + x_part ** 2) == 0:
            raise Exception("Point-1 and Point-2 are the same!")
        distance /= math.sqrt(y_part**2 + x_part**2)
        return distance

    def is_real(self):
        return self.real
