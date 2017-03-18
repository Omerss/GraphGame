import ConnectionMatrix
from NodeObject import NodeObject
from Enums import Colours, Shapes
import math

MIN_VALUE = 0.0001
MAX_VALUE = 1


class ProbabilityNode(NodeObject):
    """

    """
    probability = MIN_VALUE
    x_coor = None
    y_coor = None

    def __init__(self, temp_x, temp_y, probability):
        self.serial_num = -1
        self.colour_probability_list = []
        self.shape = Shapes.circle
        self.location_equation = {'temp_x': temp_x, 'temp_y': temp_y, 'slope': float("infinity"), 'const': 0,
                                  'rads': math.pi}
        self.neighbors = set()
        self.num_neighbors = 0
        self.probability = probability

    # def update_location(self, x_coor, y_coor, new_probability):
    #     if len(self.location_list) == 0:
    #         self.location_list.append(LocationProbability(location={'x': x_coor, 'y': y_coor},
    #                                                       set_probability=new_probability))
    #     else:
    #         for location in self.location_list:
    #             if location.location['x'] == x_coor and location.location['y'] == y_coor:
    #                 location.update_probability(new_probability)
    #             else:
    #                 self.location_list.append(LocationProbability(location={'x': x_coor, 'y': y_coor},
    #                                                               set_probability=new_probability))

    def get_best_location(self):
        return max(self.location_list)

    def extrapolate_equation_from_points(self, other_x, other_y):
        """
        Get the data for the linear equation. Uses another point for a reference to get data.
        Gets slope from 0 to inf.
        Rads from 0 to 2*pi
        Const for the equation
        :param other_x: The x value of the other node
        :param other_y: The y value of the other node
        :return:
        """
        if other_x == self.location_equation['temp_x']:
            self.location_equation['slope'] = float("infinity")
            self.location_equation['rads'] = math.pi/2 if other_x > self.location_equation['temp_x'] else math.pi*3/2
        else:
            # y = m*x + b
            slope = (other_y - self.location_equation['temp_y'])/(other_x - self.location_equation['temp_x'])
            self.location_equation['slope'] = slope
            self.location_equation['const'] = self.location_equation['temp_y'] - slope*self.location_equation['temp_x']
            self.location_equation['rads'] = math.atan(slope) if other_x < self.location_equation['temp_x']\
                else 2*math.pi - math.atan(slope)


class ProbabilityVector:
    point = ()
    rads = math.pi

    def __init__(self, self_x, self_y, rads):
        self.point = (self_x, self_y)
        self.rads = rads


class ProbabilityObject:
    def __init__(self):
        self.probability = 0

    def update_probability(self, new_probability):
        self.probability = new_probability


class LocationProbability(ProbabilityObject):
    location = {'x': 0, 'y': 0}
    probability = 0

    def __init__(self, location={'x': -1, 'y': -1}, set_probability=0):
        assert 'x' in location.keys() and 'y' in location.keys() and len(location.keys()) == 2,\
            "Error! Location was not in correct format - {}".format(location)
        assert ConnectionMatrix.MAX_VALUE >= set_probability >= ConnectionMatrix.MIN_VALUE,\
            "Error! new probability has impossible value: {}".format(set_probability)
        self.location = location
        self.probability = set_probability

    def __cmp__(self, other):
        return self.probability > other.probability


class SizeProbability(ProbabilityObject):
    size = 1
    probability = 0

    def __init__(self, size=1, set_probability=0):
        assert size > 0, "Error! size of node cannot be negative!"
        assert ConnectionMatrix.MAX_VALUE >= set_probability >= ConnectionMatrix.MIN_VALUE,\
            "Error! new probability has impossible value: {}".format(set_probability)
        self.size = size
        self.probability = set_probability


class ColourProbability(ProbabilityObject):
    colour = Colours.black
    probability = 0

    def __init__(self, colour=Colours.black, set_probability=0):
        assert ConnectionMatrix.MAX_VALUE >= set_probability >= ConnectionMatrix.MIN_VALUE,\
                "Error! new probability has impossible value: {}".format(set_probability)
        self.colour = colour
        self.probability = set_probability
