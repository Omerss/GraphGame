import kivy

from SupplementaryFiles import Utils
from SupplementaryFiles.GraphObj import get_serial
from SupplementaryFiles.Point import Point
from SupplementaryFiles.LineEquation import LineEquation

kivy.require('1.9.1')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from GraphButton import MultiButton
from KivyGraph import KivyGraph
from KivyEdge import KivyEdge
from kivy.graphics import Color
from KivyNode import KivyNode
from SupplementaryFiles.GraphObj import GraphObject
from SupplementaryFiles.NodeObject import NodeObject

Colours = [{'R':1,'G':0,'B':0,'name':"red"},{'R':0,'G':1,'B':0,'name':"green"},{'R':0,'G':0,'B':1,'name':"blue"},{'R':1,'G':0,'B':1,'name':"purple"},{'R':1,'G':1,'B':0,'name':"yellow"},{'R':0,'G':1,'B':1,'name':"light blue"}]

class GameLayout(FloatLayout):
    button_width = 100
    dim = {"min_x": button_width, "min_y": 0 ,"max_x": 400, "max_y": 200}
    original_graph = None
    kivy_graph = None
    center_screen = (0,0)


    def __init__(self, **kwargs):
        super(GameLayout, self).__init__(**kwargs)
        kivy.core.window.Window.size = (self.dim['max_x'], self.dim['max_y'])
        self.original_graph = self.get_GraphObj()
        #self.original_graph = create_rand_graph("{}\..\GraphsData\config.ini".format(os.getcwd()))
        self.center_screen = self.get_center_coor()
        self.kivy_graph = KivyGraph(self.center_screen, self.original_graph.size, self.dim)
        self.get_nodes()
        self.get_edges()
        self.button1_func = [self.kivy_graph.zoom_out, self.kivy_graph.zoom_in]
        self.button2_func = [self.kivy_graph.centralize_most_connected]
        self.button3_func = [self.kivy_graph.centralize_closest_same_color]
        self.button4_func = [self.kivy_graph.centralize_closest_neighbor_diff_color]
        self.button5_func = [self.get_info_from_screen]
        self.get_buttons()

        self.kivy_graph.print_graph_nodes()
        #self.kivy_graph.centralize_random_node(False)
        self.kivy_graph.move_node_to_center(self.kivy_graph.nodes[0],False)

    def get_center_coor(self):
        """
        :return: the coordinations of the center of the screen (not including the button area)
        """
        x = (self.dim['max_x'] - self.dim['min_x'])/2 + self.button_width
        y = (self.dim['max_y'] - self.dim['min_y']) / 2
        return (x,y)

    def get_nodes(self):
        """
        for each NodeObject from the original graph (of type GraphObj) this function creates
        an equivalent KivyNode and adds it to the kivy graph (of type KivyGraph)
        """
        graph_nodes = self.original_graph.node_list
        with self.canvas:
            for node in graph_nodes:
                colour = node.colour
                Color(colour['R'],colour['G'],colour['B'])
                new_node = KivyNode(node.x,node.y,node.serial_num,colour['name'])
                self.kivy_graph.add_node(new_node)

    def get_edges(self):
        """
        function creates a KivyEdge that represents the neighbors in the original graph (GraphObj), adds created edge to the
        kivy graph (KivyGraph), and adds the nodes (KivyNodes) connected to the edge to each other's list of neighbors
        """
        edges = self.original_graph.get_connections()
        with self.canvas:
            Color(1, 1, 1)
            for edge in edges:
                node1 = self.kivy_graph.get_by_serial(edge[0])
                node2 = self.kivy_graph.get_by_serial(edge[1])
                new_edge = KivyEdge(node1,node2)
                self.kivy_graph.add_edge(new_edge)
                node1.add_neighbor(node2)
                node2.add_neighbor(node1)

    def get_buttons(self):
        """
        creates a GridLayout that would hold the buttons (GraphButtons) needed for the game. each button should be
        initialized using a string representing an image to be displayed on the button and a function that will be
        responsible for the button's functionality
        """
        layout = GridLayout(cols=1, col_default_width=self.button_width, col_force_default=True)
        button1 = MultiButton('{}\\button1.jpg'.format(Utils.image_folder), self.button1_func, None, [], 1)
        button2 = MultiButton('{}\\button2.jpg'.format(Utils.image_folder), self.button2_func, None, [], 2)
        button3 = MultiButton('{}\\button3.jpg'.format(Utils.image_folder), self.button3_func, None, [], 3)
        button4 = MultiButton('{}\\button4.jpg'.format(Utils.image_folder), self.button4_func, None, [], 4)
        button5 = MultiButton('{}\\button4.jpg'.format(Utils.image_folder), self.button5_func, None, [], 5)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        layout.add_widget(button5)
        self.add_widget(layout)

    def get_GraphObj(self):
        graph = GraphObject(None,800,400,6,4,5)
        node1 = NodeObject(188, {'x': 369, 'y': 168}, 50, Colours[0])
        node2 = NodeObject(-55, {'x': 480, 'y': 275}, 50, Colours[1])
        #node3 = NodeObject(640, {'x': 628, 'y': 169}, 50, Colours[2])
        #node4 = NodeObject(206, {'x': 636, 'y': 306}, 50, Colours[3])
        #node5 = NodeObject(-67, {'x': 250, 'y': 289}, 50, Colours[4])
        #node6 = NodeObject(186, {'x': 184, 'y': 71}, 50, Colours[5])
        #center red:
        node3 = NodeObject(640, {'x': 494, 'y': 93}, 50, Colours[2])
        node4 = NodeObject(206, {'x': 557, 'y': 285}, 50, Colours[3])
        node5 = NodeObject(-67, {'x': 244, 'y': 243}, 50, Colours[4])
        node6 = NodeObject(186, {'x': 179, 'y': 50}, 50, Colours[5])
        #no center:
        #node1 = NodeObject(188, {'x': 375, 'y': 175}, 50, Colours[0])
        #node3 = NodeObject(640, {'x': 545, 'y': 25}, 50, Colours[2])
        #node5 = NodeObject(-67, {'x': 167, 'y': 260}, 50, Colours[4])
        #node6 = NodeObject(186, {'x': 125, 'y': 25}, 50, Colours[5])
        graph.node_list.append(node1)
        graph.node_list.append(node2)
        graph.node_list.append(node3)
        graph.node_list.append(node4)
        graph.node_list.append(node5)
        graph.node_list.append(node6)
        graph.connections = [(640, 188), (-55, 206), (-55, 186), (-67, 640),
                             (-67, 206), (640, 206), (-67, 186), (640, 186)]
        return graph

    def get_info_from_screen(self):
        '''
        Function returns the nodes and edges that are at least partially displayed onscreen
        :return: returns a dictionary containing two objects:
        'nodes': A list containing the nodes that are at least partially displayed onscreen.
        'edges': A list representing the edges that are at least partially displayed onscreen. Each edge is represented
                 by a tuple containing of the edge's nodes. If one of the nodes is not onscreen, a new NodeObject is
                 created where the x,y coordinates represent the intersection between the edge and the screen and the
                 serial and size are set to None.
        '''


        nodes = self.get_onscreen_nodes()
        edges = self.get_onscreen_edges(nodes)

        print self.kivy_graph.corners
        print "on screen: "
        for node in nodes:
            print node
        for edge in edges:
            print edge
        print "kivy nodes:"
        self.kivy_graph.print_graph_nodes()

        return {'nodes': nodes, 'edges': edges}

    def get_onscreen_nodes(self):
        '''
        Function goes over the list of nodes in the graph and checks which ones are displayed onscreen
        :return: A list containing the nodes that are at least partially displayed onscreen.
        '''
        bottom_left = self.kivy_graph.corners["bottom_left"]
        top_right = self.kivy_graph.corners["top_right"]
        displayed_nodes = []
        for node in self.kivy_graph.nodes:
            real_node = self.original_graph.get_node_by_serial(node.serial)
            node_x = real_node.x
            node_y = real_node.y
            node_r = node.get_radius()
            if (node_x + node_r) > bottom_left.get_x() and (node_x - node_r) < top_right.get_x() and \
                            (node_y + node_r) > bottom_left.get_y() and (node_y - node_r) < top_right.get_y():
                displayed_nodes.append(real_node)
        return displayed_nodes

    def get_onscreen_edges(self, displayed_nodes):
        '''
        Function goes over the list of edges in the graph and checks which ones are displayed onscreen
        :param displayed_nodes: a list of the nodes displayed onscreen
        :return: A list representing the edges that are at least partially displayed onscreen. Each edge is represented
                 by a tuple containing the edge's nodes and the edge's original slope. If one of the nodes is not onscreen, a new NodeObject is
                 created where the x,y coordinates represent the intersection between the edge and the screen.
        '''

        screen_edges = self.kivy_graph.corners
        top_left = Point(screen_edges["top_left"].get_x(), screen_edges["top_left"].get_y())
        top_right = Point(screen_edges["top_right"].get_x() + 0.001, screen_edges["top_right"].get_y())
        bottom_left = Point(screen_edges["bottom_left"].get_x() + 0.001, screen_edges["bottom_left"].get_y())
        bottom_right = Point(screen_edges["bottom_right"].get_x(), screen_edges["bottom_right"].get_y())
        top = LineEquation.create_equation(top_left, top_right)
        bottom = LineEquation.create_equation(bottom_left, bottom_right)
        left = LineEquation.create_equation(bottom_left, top_left)
        right = LineEquation.create_equation(bottom_right, top_right)

        displayed_edges = []

        for edge in self.kivy_graph.edges:

            if self.is_node_onscreen(edge.node1, screen_edges):
                if self.is_node_onscreen(edge.node2, screen_edges):
                    first_node = self.original_graph.get_node_by_serial(edge.node1.serial)
                    second_node = self.original_graph.get_node_by_serial(edge.node2.serial)
                    if edge.node1.get_x() < edge.node2.get_x():
                        curr_edge = (first_node, second_node, edge.slope)
                    else:
                        curr_edge = (second_node, first_node, edge.slope)
                else:
                    curr_edge = self.get_partly_visible_edge(edge, top, bottom, left, right, edge.node1)
            elif self.is_node_onscreen(edge.node2, screen_edges):
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
        '''

        :param edge: an edge that can be seen onscreen but where at least one node is not visible
        :param top: equation representing the top border of the screen
        :param bottom: equation representing the bottom border of the screen
        :param left: equation representing the left border of the screen
        :param right: equation representing the right border of the screen
        :param node: the visible node connected to the edge, or None if no node is visible
        :return: A tuple of two NodeObjects, each representing a one of the edge's nodes. If one of the nodes is not
        onscreen, the x,y coordinates represent the intersection between the edge and the screen and the serial and
        size are set to None.
        '''
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

    def fit_graph(self):
        self.kivy_graph.resize_graph(800, 400, 50, 2, True)

    def fit_to_screen(self):
        self.kivy_graph.resize_graph(400, 200, 40, 1.8, True)

    def zoom_out(self):
        self.kivy_graph.resize_graph(self.kivy_graph.min_size['max_x'], self.kivy_graph.min_size['max_y'], 35, 1.4,False)

    def zoom_in(self):
        self.kivy_graph.resize_graph(self.kivy_graph.max_size['max_x'], self.kivy_graph.max_size['max_y'], 50, 2, False)

class GraphGameApp(App):
    def build(self):
        layout = GameLayout()
        #layout.kivy_graph.print_graph_nodes()
        print layout.original_graph.connections
        return layout


