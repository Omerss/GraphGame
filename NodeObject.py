import math


class NodeObject():
    serial_num = -1
    colour = ""
    shape = ""
    location = {'x':0, 'y':0}
    size = 0
    neighbors = []

    def __init__(self, serial, location, size, colour = "black", shape = "circle"):
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





