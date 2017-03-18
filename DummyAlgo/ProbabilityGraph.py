from ConnectionMatrix import ConnectionMatrix
from ProbabilityObjects import ProbabilityNode, ProbabilityVector


class ProbabilityGraph:
    """
    Holds the data for the AI of how the graph looks like. All actions for manipulating the graph will be done
    thorough this interface
    """
    max_serial = 1
    node_list = []
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
        # if self.node_count > len(self.node_list):
        #     lowest_node = self.node_list[0]
        #     for node in self.node_list:
        #         if node.probability < lowest_node.probability:
        #             lowest_node = node
        #     self.node_list.remove(lowest_node)

    def add_vector(self, x_coor, y_coor, rads):
        vector = ProbabilityVector(x_coor, y_coor, rads)
        self.vector_list.append(vector)


