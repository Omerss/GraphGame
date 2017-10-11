from KivyGraph import KivyGraph
from KivyEdge import KivyEdge
from kivy.graphics import Color
from KivyNode import KivyNode
from kivy.uix.relativelayout import RelativeLayout


class GraphDisplay(RelativeLayout):

    def __init__(self, graph, dim, **kwargs):
        super(GraphDisplay, self).__init__(size_hint_x=None, width=dim[0], **kwargs)
        self.kivy_graph = KivyGraph((0, 0), 1, {"min_x": 0, "min_y": 0, "max_x": dim[0], "max_y": dim[1]})
        ratio = self.get_ratio(graph.size, dim)
        move_nodes = self.get_nodes(graph, ratio)
        self.reset_nodes(ratio, move_nodes)
        self.get_edges(graph)

    def get_ratio(self, graph_size, dim):
        x = dim[0] / float(graph_size['max_x'])
        y = dim[1] / float(graph_size['max_y'])
        return x, y

    def get_nodes(self, original_graph, zoom):
        min_x = 0
        min_y = 0
        with self.canvas:
            for node in original_graph.node_list:
                colour = node.colour
                Color(colour['R'], colour['G'], colour['B'])
                if node.x < min_x:
                    min_x = node.x
                if node.y < min_y:
                    min_y = node.y
                new_node = KivyNode(node.x, node.y, node.serial_num, zoom[0]*node.size, node.size, colour['name'])
                self.kivy_graph.add_node(new_node)

        return min_x, min_y, node.size

    def reset_nodes(self, ratio, move_amount):
        if move_amount[0] < 0:
            self.kivy_graph.move_right(-(move_amount[0]-move_amount[2]))
        if move_amount[1] < 0:
            self.kivy_graph.move_up(-(move_amount[1]-move_amount[2]))
        for node in self.kivy_graph.nodes:
            node.relative_move(ratio[0], ratio[1])



    def get_edges(self, graph):
        edges = graph.get_connections()
        with self.canvas:
            Color(1, 1, 1)
            for edge in edges:
                node1 = self.kivy_graph.get_by_serial(edge[0])
                node2 = self.kivy_graph.get_by_serial(edge[1])
                new_edge = KivyEdge(node1, node2, 1.3)
                self.kivy_graph.add_edge(new_edge)
                node1.add_neighbor(node2)
                node2.add_neighbor(node1)
