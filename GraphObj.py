from random import random

import Utils
from NodeObject import NodeObject


class GraphObject:
    node_list = []
    size = {}

    def __init__(self, size):
        self.config = Utils.config
        for i in range (self.config['GeneralParams']['NodeCount']):
            self.node_list[i] = i
        size = size

    def create_graph(self):

        random.seed()
        location = (random.randint(0,self.size["x"]),random.randint(0,self.size["y"]))
        location2 = (random.randint(0, self.size["x"]), random.randint(0, self.size["y"]))
        node = NodeObject(location,1)
        node2 = NodeObject(location2, 1)

        for i in range(self.config["GeneralParams"]["NodeCount"]):
            self.nodeList.append(NodeObject())

