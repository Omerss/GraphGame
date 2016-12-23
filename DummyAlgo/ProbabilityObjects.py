import ConnectionMatrix
from NodeObject import NodeObject
from Enums import Colours, Shapes
import math

MIN_VALUE = 0.0001
MAX_VALUE = 1


class ProbabilityNode(NodeObject):

    def __init__(self, temp_x, temp_y):
        self.serial_num = -1
        self.colour_probability_list = []
        self.shape = Shapes.circle
        self.location_list = []
        self.location_equasion = {'temp_x': temp_x, 'temp_y': temp_y, 'slope': float("infinity"), 'const': 0,
                                  'rads': math.pi}
        self.size_list = []
        self.neighbors = set()
        self.num_neighbors = 0
        self.update_location(temp_x, temp_y, 0.001)

    def update_location(self, x_coor, y_coor, new_probability):

        if len(self.location_list) == 0:
            self.location_list.append(LocationProbability(location={'x': x_coor, 'y': y_coor},
                                                          set_probability=new_probability))
        else:
            for location in self.location_list:
                if location['x'] == x_coor and location['y'] == y_coor:
                    location.update_probability(new_probability)
                else:
                    self.location_list.append(LocationProbability(location={'x': x_coor, 'y': y_coor},
                                                                  set_probability=new_probability))

    def get_best_location(self):
        return max(self.location_list)

    def extrapulate_equasion_from_points(self, other_x, other_y):
        if other_x == self.location_equasion['temp_x']:
            self.location_equasion['slope'] = float("infinity")
            self.location_equasion['rads'] = math.pi/2 if other_x > self.location_equasion['temp_x'] else math.pi*3/2
        else:
            # y = m*x + b
            slope = (other_y - self.location_equasion['temp_y'])/(other_x - self.location_equasion['temp_x'])
            self.location_equasion['slope'] = slope
            self.location_equasion['const'] = self.location_equasion['temp_y'] - slope*self.location_equasion['temp_x']
            self.location_equasion['rads'] = math.atan(slope) if other_x < self.location_equasion['temp_x']\
                else 2*math.pi - math.atan(slope)

class ProbabilityObject:
    def __init__(self):
        self.probability = 0

    def update_probability(self, new_probability):
        self.probability = new_probability


class LocationProbability(ProbabilityObject):
    location = {'x': 0, 'y': 0}
    probability = 0

    def __init__(self, location={'x': -1, 'y': -1}, set_probability=0):
        assert ('x' in location.keys() and 'y' in location.keys() and len(location.keys()) == 2,
                "Error! Location was not in correct format - {}".format(location))
        assert (ConnectionMatrix.MAX_VALUE >= set_probability >= ConnectionMatrix.MIN_VALUE,
                "Error! new probability has impossible value: {}"
                .format(set_probability))
        self.location = location
        self.probability = set_probability

    def __cmp__(self, other):
        return self.probability > other.probability


class SizeProbability(ProbabilityObject):
    size = 1
    probability = 0

    def __init__(self, size=1, set_probability=0):
        assert (size > 0, "Error! size of node cannot be negative!")
        assert (ConnectionMatrix.MAX_VALUE >= set_probability >= ConnectionMatrix.MIN_VALUE,
                "Error! new probability has impossible value: {}"
                .format(set_probability))
        self.size = size
        self.probability = set_probability


class ColourProbability(ProbabilityObject):
    colour = Colours.black
    probability = 0

    def __init__(self, colour=Colours.black, set_probability=0):
        assert (ConnectionMatrix.MAX_VALUE >= set_probability >= ConnectionMatrix.MIN_VALUE,
                "Error! new probability has impossible value: {}"
                .format(set_probability))
        self.colour = colour
        self.probability = set_probability



