from ConnectionMatrix import ConnectionMatrix
from ProbabilityObjects import ProbabilityNode


class ProbabilityGraph:
    max_serial = 1

    def __init__(self, node_count):
        self.node_count = node_count
        self.node_list = []

    def add_node(self, x_coor, y_coor, probability):
        tmp_node = ProbabilityNode()
        tmp_node.serial_num = self.max_serial
        self.max_serial += 1
        tmp_node.update_location(x_coor, y_coor, probability)
        self.node_list.append(tmp_node)


a = ProbabilityGraph(15)
a.add_node(500, 700, 0.766)
a.add_node(600, 90, 0.2)
a.add_node(100, 150, 1)


