import ConnectionMatrix
from NodeObject import NodeObject
from Enums import Colours, Shapes


class ProbabilityNode(NodeObject):
    colour_probability = [ColourProbability]
    shape = Shapes.circle
    location = [LocationProbability]
    size = [SizeProbability]
    neighbors = ()

    def __init__(self):
        pass


class LocationProbability:
    location = {'x': 0, 'y': 0}
    probability = 0

    def __init__(self, location={'x': 0, 'y': 0}, set_probability=0):
        assert ('x' in location.keys() and 'y' in location.keys() and location.keys().count() == 2,
                "Error! Location was not in correct format - {}".format(location))
        assert (ConnectionMatrix.MAX_VALUE > set_probability > ConnectionMatrix.MIN_VALUE,
                "Error! new probability has impossible value: {}"
                .format(set_probability))
        self.location = location
        self.probability = set_probability

    def update_probability(self, new_probability):
        self.probability = new_probability


class SizeProbability:
    size = 1
    probability = 0

    def __init__(self, size = 1, set_probability = 0):
        assert (size > 0, "Error! size of node cannot be negative!")
        assert (ConnectionMatrix.MAX_VALUE > set_probability > ConnectionMatrix.MIN_VALUE,
                "Error! new probability has impossible value: {}"
                .format(set_probability))
        self.size = size
        self.probability = set_probability

    def update_probability(self, new_probability):
        self.probability = new_probability


class ColourProbability:
    colour = Colours.black
    probability = 0

    def __init__(self, colour = Colours.black, set_probability = 0):
        assert (ConnectionMatrix.MAX_VALUE > set_probability > ConnectionMatrix.MIN_VALUE,
                "Error! new probability has impossible value: {}"
                .format(set_probability))
        self.colour = colour
        self.probability = set_probability

    def update_probability(self, new_probability):
        self.probability = new_probability


