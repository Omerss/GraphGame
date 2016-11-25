import math


class NodeObject:
    serial_num = -1
    colour = ""
    shape = ""
    location = {'x': 0, 'y': 0}
    size = 0
    neighbors = []

    def __init__(self, serial, location, size, colour=Colours.Black, shape=Shape.Circle):
        self.serial_num = serial
        self.location = location
        self.size = size
        self.colour = colour
        self.shape = shape

    def get_num_neighbors(self):
        return len(self.neighbors)

    def distance_from_node(self, other_node):
        if other_node is None:
            return -1
        x = math.fabs(other_node.location['x'] - self.location['x'])
        y = math.fabs(other_node.location['y'] - self.location['y'])
        dist = math.sqrt(x ^ 2 + y ^ 2)
        return dist

    def connect_to_node(self, other_node):
        self.neighbors.append(other_node.serial)

    def distance_from_line(self, node_1, node_2):
        """
        If for some reason we davide by zero we return -1
        :param node_1: NodeObject
        :param node_2: NodeObject
        :return: distance between self and the line between the two points
        """
        # See https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
        y_part = node_2.location['y'] - node_1.location['y']
        x_part = node_2.location['x'] - node_1.location['x']

        dist_part1 = y_part * self.location['x']
        dist_part2 = x_part * self.location['y']
        distance = math.abs(dist_part1
                            - dist_part2
                            + node_1.location['y'] * node_2.location['x']
                            - node_2.location['y'] * node_1.location['x'])
        if math.sqrt(y_part**2 + x_part**2) == 0:
            raise Exception ("Point-1 and Point-2 are the same!")
        distance /= math.sqrt(y_part**2 + x_part**2)
        return distance

    def __init__(self):
        pass

class Colours:
    Black, Red, Green, Blue = range(4)


class Shape:
    Circle = range(1)
