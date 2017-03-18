from ConnectionMatrix import ConnectionMatrix
from ProbabilityObjects import ProbabilityNode, ProbabilityVector


class ProbabilityGraph:
    """
    Holds the data for the AI of how the graph looks like. All actions for manipulating the graph will be done
    thorough this interface
    Probability graph holds 2 main lists:
    Node_list = holds actual nodes that have been viewed by us
    Vector_list = holds a list of all the edges we've seen in the graph
    """
    max_serial = 1
    node_list = []
    vector_list = []
    node_count = 0

    def __init__(self, node_count):
        self.node_count = node_count
        self.node_list = []
        self.vector_list = []

    def add_node(self, x_coor, y_coor, probability):
        tmp_node = ProbabilityNode(x_coor, y_coor, probability)
        tmp_node.serial_num = self.max_serial
        self.max_serial += 1
        self.node_list.append(tmp_node)

    def add_vector(self, x_coor, y_coor, rads):
        vector = ProbabilityVector(x_coor, y_coor, rads)
        self.vector_list.append(vector)

    def find_collisions(self):
        """
        Goes through all vectors available and searches for possible interactions between them
        :return: A list of all possible connections
        """
        collisions = []
        for vector in self.vector_list:
            pass
        return collisions
