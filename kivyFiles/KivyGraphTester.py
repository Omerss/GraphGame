import kivy

kivy.require('1.9.1')

from SupplementaryFiles import Utils
from SupplementaryFiles.GraphObj import get_serial
from SupplementaryFiles.Point import Point
from SupplementaryFiles.LineEquation import LineEquation
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from GraphButton import MultiButton
from SupplementaryFiles.GraphObj import GraphObject
from SupplementaryFiles.NodeObject import NodeObject
from GraphLayout import GraphLayout
from SupplementaryFiles.Enums import Colours
from GameLayout import GameLayout

from kivy.uix.floatlayout import FloatLayout

MYColours = [{'R': 1, 'G': 0, 'B': 0, 'name': "red"}, {'R': 0, 'G': 1, 'B': 0, 'name': "green"},
           {'R': 0, 'G': 0, 'B': 1, 'name': "blue"}, {'R': 1, 'G': 0, 'B': 1, 'name': "purple"},
           {'R': 1, 'G': 1, 'B': 0, 'name': "yellow"}, {'R': 0, 'G': 1, 'B': 1, 'name': "light blue"},
           {'R': 1, 'G': 1, 'B': 1, 'name': "white"}]


class MyGameLayout(FloatLayout):

    def __init__(self, graph, signal, button_lst, button_width=0.3, zoom_rate=0.7, edge_size=2, **kwargs):
        super(MyGameLayout, self).__init__(rows=1, cols=2, **kwargs)
        self.button_width = kivy.core.window.Window.size[0] * button_width
        self.dim = {"min_x":0, "min_y": 0}
        self.dim["max_x"] = kivy.core.window.Window.size[0]
        self.dim["max_y"] = kivy.core.window.Window.size[1]
        print self.dim
        self.buttons = []
        self.original_graph = graph
        self.dim["max_x"] -= self.button_width
        self.kivy_graph_in = GraphLayout(self.original_graph, self.dim, 1, edge_size)
        self.kivy_graph_out = GraphLayout(self.original_graph, self.dim, zoom_rate, edge_size)
        self.kivy_graph_in.pos = (self.width - button_width, 0)
        self.kivy_graph_out.pos = (self.button_width, 0)
        self.add_widget(self.kivy_graph_in)
        self.is_zoomed_out = False
        self.set_button_functions()
        self.button_layout = self.get_buttons(signal, button_lst)
        self.add_widget(self.button_layout)
        self.button_layout.pos=(0,0)

    def set_button_functions(self):
        self.button1_func = [self.zoom_out, self.zoom_in]
        self.button2_func = [self.centralize_most_connected]
        self.button3_func = [self.centralize_closest_same_color]
        self.button4_func = [self.centralize_closest_neighbor_diff_color]
        self.button5_func = [self.get_info_from_screen]

    def get_buttons(self, signal, button_lst):
        """
        creates a GridLayout that would hold the buttons (GraphButtons) needed for the game. each button should be
        initialized using a string representing an image to be displayed on the button and a function that will be
        responsible for the button's functionality
        """
        layout = GridLayout(cols=1, col_default_width=self.button_width, col_force_default=True)
        button1 = MultiButton('{}\\button1.jpg'.format(Utils.image_folder), self.button1_func, signal, button_lst, 1,
                              self.button_width)
        button2 = MultiButton('{}\\button2.jpg'.format(Utils.image_folder), self.button2_func, signal, button_lst, 2,
                              self.button_width)
        button3 = MultiButton('{}\\button3.jpg'.format(Utils.image_folder), self.button3_func, signal, button_lst, 3,
                              self.button_width)
        button4 = MultiButton('{}\\button4.jpg'.format(Utils.image_folder), self.button4_func, signal, button_lst, 4,
                              self.button_width)
        button5 = MultiButton('{}\\button4.jpg'.format(Utils.image_folder), self.button5_func, signal, button_lst, 5,
                              self.button_width)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        layout.add_widget(button5)
        self.buttons.append(button1)
        self.buttons.append(button2)
        self.buttons.append(button3)
        self.buttons.append(button4)
        self.buttons.append(button5)
        return layout

    def zoom_out(self):
        center_node = self.kivy_graph_out.kivy_graph.get_by_serial(self.kivy_graph_in.kivy_graph.center_node.serial)
        self.kivy_graph_out.kivy_graph.move_node_to_center(center_node, False)
        self.remove_widget(self.kivy_graph_in)
        self.add_widget(self.kivy_graph_out)
        self.is_zoomed_out = True
        self.remove_widget(self.button_layout)
        self.add_widget(self.button_layout)

    def zoom_in(self):
        center_node = self.kivy_graph_in.kivy_graph.get_by_serial(self.kivy_graph_out.kivy_graph.center_node.serial)
        self.kivy_graph_in.kivy_graph.move_node_to_center(center_node, False)
        self.remove_widget(self.kivy_graph_out)
        self.add_widget(self.kivy_graph_in)
        self.is_zoomed_out = False
        self.remove_widget(self.button_layout)
        self.add_widget(self.button_layout)

    def centralize_most_connected(self):
        if self.is_zoomed_out:
            self.kivy_graph_out.kivy_graph.centralize_most_connected()
        else:
            self.kivy_graph_in.kivy_graph.centralize_most_connected()

    def centralize_closest_same_color(self):
        if self.is_zoomed_out:
            self.kivy_graph_out.kivy_graph.centralize_closest_same_color()
        else:
            self.kivy_graph_in.kivy_graph.centralize_closest_same_color()

    def centralize_closest_neighbor_diff_color(self):
        if self.is_zoomed_out:
            self.kivy_graph_out.kivy_graph.centralize_closest_neighbor_diff_color()
        else:
            self.kivy_graph_in.kivy_graph.centralize_closest_neighbor_diff_color()

    def set_button_status(self, status):
        print "setting button status to", status
        for item in self.buttons:
            item.active = status

    def test_button_status(self):
        for item in self.buttons:
            print "button", item.num, "status is", item.active
        self.set_button_status(False)
        for item in self.buttons:
            print "button", item.num, "status is", item.active
        self.set_button_status(True)

    @staticmethod
    def get_graph_obj():
        graph = GraphObject(None, 800, 400, 6, 4, 5)
        node1 = NodeObject(188, {'x': 369, 'y': 168}, 50, MYColours[0])
        node2 = NodeObject(-55, {'x': 480, 'y': 275}, 50, MYColours[1])
        node3 = NodeObject(640, {'x': 628, 'y': 169}, 50, MYColours[2])
        node4 = NodeObject(206, {'x': 636, 'y': 306}, 50, MYColours[3])
        node5 = NodeObject(-67, {'x': 250, 'y': 289}, 50, MYColours[4])
        node6 = NodeObject(186, {'x': 184, 'y': 71}, 50, MYColours[5])
        graph.node_list.append(node1)
        graph.node_list.append(node2)
        graph.node_list.append(node3)
        graph.node_list.append(node4)
        graph.node_list.append(node5)
        graph.node_list.append(node6)
        graph.connections = [(640, 188), (-55, 206), (-55, 186), (-67, 640),
                             (-67, 206), (640, 206), (-67, 186), (640, 186)]
        graph.center_node = 188
        return graph

    @staticmethod
    def get_graph_obj1():
        graph = GraphObject(None, 5000, 5000, 24, 3, 10)
        node2 = NodeObject("ce5", {'x': -2465, 'y': 2732}, 50, Colours['yellow'])
        node1 = NodeObject("a26", {'x': 614, 'y': 600}, 50, Colours['yellow'])
        node3 = NodeObject("4ec", {'x': -3229, 'y': 3455}, 50, Colours['red'])
        node4 = NodeObject("5e7", {'x': -1184, 'y': 3385}, 50, Colours['blue'])
        node5 = NodeObject("5ea", {'x': 303, 'y': 1050}, 50, Colours['red'])
        node6 = NodeObject("a97", {'x': -1128, 'y': 1884}, 50, Colours['blue'])
        node7 = NodeObject("5f3", {'x': -2910, 'y': 271}, 50, Colours['red'])
        node8 = NodeObject("68f", {'x': -1105, 'y': 1409}, 50, Colours['blue'])
        node9 = NodeObject("a0f", {'x': -1598, 'y': 4054}, 50, Colours['yellow'])
        node10 = NodeObject("b3b", {'x': 1047, 'y': 61}, 50, Colours['red'])
        node11 = NodeObject("379", {'x': -1034, 'y': 2046}, 50, Colours['red'])
        node12 = NodeObject("c5c", {'x': 1543, 'y': 4466}, 50, Colours['red'])
        node13 = NodeObject("97b", {'x': -2551, 'y': 1694}, 50, Colours['yellow'])
        node14 = NodeObject("ac2", {'x': 821, 'y': 4534}, 50, Colours['blue'])
        node15 = NodeObject("788", {'x': -2790, 'y': 2330}, 50, Colours['yellow'])
        node16 = NodeObject("01d", {'x': 450, 'y': 300}, 50, Colours['blue'])
        node17 = NodeObject("e29", {'x': -272, 'y': 910}, 50, Colours['yellow'])
        node18 = NodeObject("d21", {'x': -2329, 'y': 2245}, 50, Colours['blue'])
        node19 = NodeObject("7ac", {'x': 693, 'y': 3124}, 50, Colours['blue'])
        node20 = NodeObject("189", {'x': -2748, 'y': 3403}, 50, Colours['blue'])

        graph.node_list.append(node1)
        graph.node_list.append(node2)
        graph.node_list.append(node3)
        graph.node_list.append(node4)
        graph.node_list.append(node5)
        graph.node_list.append(node6)
        graph.node_list.append(node7)
        graph.node_list.append(node8)
        graph.node_list.append(node9)
        graph.node_list.append(node10)
        graph.node_list.append(node11)
        graph.node_list.append(node12)
        graph.node_list.append(node13)
        graph.node_list.append(node14)
        graph.node_list.append(node15)
        graph.node_list.append(node16)
        graph.node_list.append(node17)
        graph.node_list.append(node18)
        graph.node_list.append(node19)
        graph.node_list.append(node20)

        graph.connections = [('01d', 'e29'), ('01d', 'a97'), ('ac2', 'ce5'), ('379', 'ce5'), ('4ec', 'c5c'),
                             ('5e7', '68f'), ('5e7', '5ea'), ('5ea', '788'), ('a0f', 'a97'), ('5f3', 'b3b'),
                             ('68f', '7ac'), ('a0f', 'd21'), ('a26', 'b3b'), ('189', '379'), ('97b', 'c5c'),
                             ('97b', 'e29'), ('a26', 'ac2'), ('788', '7ac'), ('189', 'd21')]
        graph.center_node = "ce5"

        in_bl = NodeObject(-1, {'x': -1509.0, 'y': 3110.0}, 50, MYColours[6])
        in_tr = NodeObject(-1, {'x': -859.0, 'y': 3660.0}, 50, MYColours[6])
        out_bl = NodeObject(-1, {'x': -1659.0, 'y': 2981.43}, 50, MYColours[6])
        out_tr = NodeObject(-1, {'x': -709.0, 'y': 3788.43}, 50, MYColours[6])

        # graph.node_list.append(in_bl)
        # graph.node_list.append(in_tr)
        # graph.node_list.append(out_bl)
        # graph.node_list.append(out_tr)

        return graph

    def get_info_from_screen(self):
        """
        Function returns the nodes and edges that are at least partially displayed onscreen
        :return: returns a dictionary containing two objects:
        'nodes': A list containing the nodes that are at least partially displayed onscreen.
        'edges': A list representing the edges that are at least partially displayed onscreen. Each edge is represented
                 by a tuple containing of the edge's nodes. If one of the nodes is not onscreen, a new NodeObject is
                 created where the x,y coordinates represent the intersection between the edge and the screen and the
                 serial and size are set to None.
        """
        if self.is_zoomed_out:
            graph_nodes = self.kivy_graph_out.kivy_graph.nodes
            graph_edges = self.kivy_graph_out.kivy_graph.edges
            graph_corners = self.kivy_graph_out.kivy_graph.corners
        else:
            graph_nodes = self.kivy_graph_in.kivy_graph.nodes
            graph_edges = self.kivy_graph_in.kivy_graph.edges
            graph_corners = self.kivy_graph_in.kivy_graph.corners

        nodes = self.get_onscreen_nodes(graph_nodes, graph_corners)
        edges = self.get_onscreen_edges(graph_edges, graph_corners)

        print graph_corners
        print "on screen: "
        for node in nodes:
            print node
        for edge in edges:
            print edge
        # print graph_corners['bottom_left'].get_x() + 25, ", 'y':", graph_corners['bottom_left'].get_y() + 25
        # print graph_corners['top_right'].get_x() - 25, ", 'y':", graph_corners['top_right'].get_y() - 25

        return {'nodes': nodes, 'edges': edges}

    def get_onscreen_nodes(self, graph_nodes, graph_corners):
        """
        Function goes over the list of nodes in the graph and checks which ones are displayed onscreen
        :return: A list containing the nodes that are at least partially displayed onscreen.
        """
        bottom_left = graph_corners["bottom_left"]
        top_right = graph_corners["top_right"]
        displayed_nodes = []
        for node in graph_nodes:
            if node.serial != -1:
                real_node = self.original_graph.get_node_by_serial(node.serial)
                node_x = real_node.x
                node_y = real_node.y
                node_r = real_node.size/2.0 - 1
                if (node_x + node_r) > bottom_left.get_x() and (node_x - node_r) < top_right.get_x() and \
                        (node_y + node_r) > bottom_left.get_y() and (node_y - node_r) < top_right.get_y():
                    displayed_nodes.append(real_node)
        return displayed_nodes

    def get_onscreen_edges(self, graph_edges, graph_corners):
        """
        Function goes over the list of edges in the graph and checks which ones are displayed onscreen
        :return: A list representing the edges that are at least partially displayed onscreen. Each edge is represented
                 by a tuple containing the edge's nodes and the edge's original slope. If one of the nodes is not
                 onscreen, a new NodeObject is created where the x,y coordinates represent the intersection between
                  the edge and the screen.
        """

        top_left = Point(graph_corners["top_left"].get_x(), graph_corners["top_left"].get_y())
        top_right = Point(graph_corners["top_right"].get_x() + 0.001, graph_corners["top_right"].get_y())
        bottom_left = Point(graph_corners["bottom_left"].get_x() + 0.001, graph_corners["bottom_left"].get_y())
        bottom_right = Point(graph_corners["bottom_right"].get_x(), graph_corners["bottom_right"].get_y())
        top = LineEquation.create_equation(top_left, top_right)
        bottom = LineEquation.create_equation(bottom_left, bottom_right)
        left = LineEquation.create_equation(bottom_left, top_left)
        right = LineEquation.create_equation(bottom_right, top_right)

        displayed_edges = []

        for edge in graph_edges:
            if self.is_node_onscreen(edge.node1, graph_corners):
                if self.is_node_onscreen(edge.node2, graph_corners):
                    first_node = self.original_graph.get_node_by_serial(edge.node1.serial)
                    second_node = self.original_graph.get_node_by_serial(edge.node2.serial)
                    if edge.node1.get_x() < edge.node2.get_x():
                        curr_edge = (first_node, second_node, edge.slope)
                    else:
                        curr_edge = (second_node, first_node, edge.slope)
                else:
                    curr_edge = self.get_partly_visible_edge(edge, top, bottom, left, right, edge.node1)
            elif self.is_node_onscreen(edge.node2, graph_corners):
                curr_edge = self.get_partly_visible_edge(edge, top, bottom, left, right, edge.node2)
            else:
                curr_edge = self.get_partly_visible_edge(edge, top, bottom, left, right, None)

            if curr_edge is not None:
                displayed_edges.append(curr_edge)

        return displayed_edges

    def is_node_onscreen(self, node, screen_edges):
        real_node = self.original_graph.get_node_by_serial(node.serial)
        node_x = real_node.x
        node_y = real_node.y
        return screen_edges["bottom_left"].get_x() < node_x < screen_edges["top_right"].get_x() and \
                    screen_edges["bottom_left"].get_y() < node_y < screen_edges["top_right"].get_y()

    def get_partly_visible_edge(self, edge, top, bottom, left, right, node):
        """

        :param edge: an edge that can be seen onscreen but where at least one node is not visible
        :param top: equation representing the top border of the screen
        :param bottom: equation representing the bottom border of the screen
        :param left: equation representing the left border of the screen
        :param right: equation representing the right border of the screen
        :param node: the visible node connected to the edge, or None if no node is visible
        :return: A tuple of two NodeObjects, each representing a one of the edge's nodes. If one of the nodes is not
        onscreen, the x,y coordinates represent the intersection between the edge and the screen and the serial and
        size are set to None.
        """
        real_node1 = self.original_graph.get_node_by_serial(edge.node1.serial)
        real_node2 = self.original_graph.get_node_by_serial(edge.node2.serial)
        point1 = Point(real_node1.x, real_node1.y)
        point2 = Point(real_node2.x, real_node2.y)
        edge_equation = LineEquation.create_equation(point1, point2)
        first_node = None
        second_node = None

        if node:
            first_node = self.original_graph.get_node_by_serial(node.serial)

        # check if edge collides with top border
        if LineEquation.check_collision_point(edge_equation, top):
            col_point = LineEquation.get_equation_collision_point(edge_equation, top)
            location = {'x': round(col_point[0], 2), 'y': round(col_point[1], 2)}
            if first_node is not None:
                second_node = NodeObject(serial=get_serial(), location=location, size=0)
                second_node.real = False
            else:
                first_node = NodeObject(serial=get_serial(), location=location, size=0)
                first_node.real = False

        # check if edge collides with bottom border
        if LineEquation.check_collision_point(edge_equation, bottom):
            col_point = LineEquation.get_equation_collision_point(edge_equation, bottom)
            location = {'x': round(col_point[0], 2), 'y': round(col_point[1], 2)}
            if first_node is not None:
                second_node = NodeObject(serial=get_serial(), location=location, size=0)
                second_node.real = False
            else:
                first_node = NodeObject(serial=get_serial(), location=location, size=0)
                first_node.real = False

        # check if edge collides with left border
        if LineEquation.check_collision_point(edge_equation, left):
            col_point = LineEquation.get_equation_collision_point(edge_equation, left)
            location = {'x': round(col_point[0], 2), 'y': round(col_point[1], 2)}
            if first_node is not None:
                second_node = NodeObject(serial=get_serial(), location=location, size=0)
                second_node.real = False

            else:
                first_node = NodeObject(serial=get_serial(), location=location, size=0)
                first_node.real = False

        # check if edge collides with right border
        if LineEquation.check_collision_point(edge_equation, right):
            col_point = LineEquation.get_equation_collision_point(edge_equation, right)
            location = {'x': round(col_point[0], 2), 'y': round(col_point[1], 2)}
            if first_node is not None:
                second_node = NodeObject(serial=get_serial(), location=location, size=0)
                second_node.real = False
            else:
                first_node = NodeObject(serial=get_serial(), location=location, size=0)
                first_node.real = False

        if second_node is None:
            if first_node is None:
                return None
            else:
                raise Exception("Only One viable node for onscreen edge!")

        min_dist = edge.node1.get_radius() / 2
        if first_node.distance(second_node) < min_dist:
            return None

        if first_node.x < second_node.x:
            curr_edge = (first_node, second_node, edge.slope)
        else:
            curr_edge = (second_node, first_node, edge.slope)

        return curr_edge


class TestScreen():
    graph_config = None
    max_turns = 5

    def __init__(self, graph, button_presses, button_ratio, **kwargs):
        self.graph = graph
        self.button_presses = button_presses
        self.button_ratio = button_ratio

    def end_graph(self):
        App.get_running_app().stop()


class GraphGameApp(App):
    def __init__(self, button_presses, **kwargs):
        super(GraphGameApp, self).__init__(**kwargs)
        self.button_presses = button_presses

    def build(self):
        # dim={"max_x": 400, "max_y": 200}
        # kivy.core.window.Window.size = (dim['max_x'], dim['max_y'])
        # layout = GameLayout(MyGameLayout.get_graph_obj(), None, self.button_presses, 100, dim)
        layout = MyGameLayout(MyGameLayout.get_graph_obj(), None, self.button_presses)
        layout.kivy_graph_in.kivy_graph.print_graph_nodes()
        print layout.original_graph.connections
        return layout
