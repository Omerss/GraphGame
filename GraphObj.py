import Utils
from NodeObject import NodeObject

class GraphObject:

    nodeList = []

    def __init__(self, size):
        self.config = Utils.config

    def create_graph(self):
        for i in range(self.config["GeneralParams"]["NodeCount"]):
            self.nodeList.append(NodeObject())
