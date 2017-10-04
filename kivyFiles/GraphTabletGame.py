from SupplementaryFiles.GraphObj import get_serial
from GameLayout import GameLayout
from SupplementaryFiles.Point import Point
from SupplementaryFiles.LineEquation import LineEquation
from SupplementaryFiles.NodeObject import NodeObject
from GameData.GameDataHandler import GameDataHandler


class GraphTabletGame:
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    graph_config = None
    is_playing = True

    def __init__(self, game_screen=None):
        self.game_screen = game_screen
        self.original_graph = self.game_screen.graph
        self.current_data_handler = GameDataHandler(self.game_screen.graph_config)
        self.max_turns = self.game_screen.max_turns
        self.button_presses = self.game_screen.button_presses
        self.layout = GameLayout(self)
        self.send_info_from_screen()

    def load(self):
        pass

    def send_info_from_screen(self):
        self.current_data_handler.add_view_to_db(self.get_info_from_screen())

    def end_game(self):
        self.is_playing = False
        self.game_screen.end_graph()

    def set_button_status(self, status):
        self.layout.set_button_status(status)

    def press_button(self, num):
        if num == 1:
            f = self.counter1 % len(self.layout.button1_func)
            self.layout.button1_func[f]()
            self.counter1 += 1
        elif num == 2:
            f = self.counter2 % len(self.layout.button2_func)
            self.layout.button2_func[f]()
            self.counter2 += 1
        elif num == 3:
            f = self.counter3 % len(self.layout.button3_func)
            self.layout.button3_func[f]()
            self.counter3 += 1
        elif num == 4:
            f = self.counter4 % len(self.layout.button4_func)
            self.layout.button4_func[f]()
            self.counter4 += 1

    def get_info_from_screen(self):
        """
        Function returns the nodes and edges that are at least partially displayed onscreen
        :return: returns a dictionary containing two objects:
        'nodes': A list containing the nodes that are at least partially displayed onscreen.
        'edges': A list representing the edges that are at least partially displayed onscreen. Each edge is represented
                 by a tuple containing the edge's nodes, the edge's original slope and the edge's equation. If one of
                 the nodes is not onscreen, a new NodeObject is created where the x,y coordinates represent the
                 intersection between the edge and the screen and the serial and size are set to None.
        """
        if self.layout.is_zoomed_out:
            graph_nodes = self.layout.kivy_graph_out.kivy_graph.nodes
            graph_edges = self.layout.kivy_graph_out.kivy_graph.edges
            graph_corners = self.layout.kivy_graph_out.kivy_graph.corners
        else:
            graph_nodes = self.layout.kivy_graph_in.kivy_graph.nodes
            graph_edges = self.layout.kivy_graph_in.kivy_graph.edges
            graph_corners = self.layout.kivy_graph_in.kivy_graph.corners

        nodes = self.get_onscreen_nodes(graph_nodes, graph_corners)
        edges = self.get_onscreen_edges(graph_edges, graph_corners)

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
                node_r = node.get_radius() * 0.85
                if (node_x + node_r) > bottom_left.get_x() and (node_x - node_r) < top_right.get_x() and \
                    (node_y + node_r) > bottom_left.get_y() and (node_y - node_r) < top_right.get_y():
                    displayed_nodes.append(real_node)
        return displayed_nodes

    def get_onscreen_edges(self, graph_edges, graph_corners):
        """
        Function goes over the list of edges in the graph and checks which ones are displayed onscreen
        :return: A list representing the edges that are at least partially displayed onscreen. Each edge is represented
                 by a tuple containing the edge's nodes, the edge's original slope and the edge's equation. If one of
                 the nodes is not onscreen, a new NodeObject is created where the x,y coordinates represent the
                 intersection between the edge and the screen.
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
            real_node1 = self.original_graph.get_node_by_serial(edge.node1.serial)
            real_node2 = self.original_graph.get_node_by_serial(edge.node2.serial)
            point1 = Point(real_node1.x, real_node1.y)
            point2 = Point(real_node2.x, real_node2.y)
            edge_equation = LineEquation.create_equation(point1, point2)
            edge.set_slope(edge_equation)

            if self.is_node_onscreen(edge.node1, graph_corners):
                if self.is_node_onscreen(edge.node2, graph_corners):
                    if edge.node1.get_x() < edge.node2.get_x():
                        curr_edge = (real_node1, real_node2, edge.slope, edge_equation)
                    else:
                        curr_edge = (real_node2, real_node1, edge.slope, edge_equation)
                else:
                    curr_edge = self.get_partly_visible_edge(edge, top, bottom, left, right, edge.node1, edge_equation)
            elif self.is_node_onscreen(edge.node2, graph_corners):
                curr_edge = self.get_partly_visible_edge(edge, top, bottom, left, right, edge.node2, edge_equation)
            else:
                curr_edge = self.get_partly_visible_edge(edge, top, bottom, left, right, None, edge_equation)

            if curr_edge is not None:
                displayed_edges.append(curr_edge)

        return displayed_edges

    def is_node_onscreen(self, node, screen_edges):
        real_node = self.original_graph.get_node_by_serial(node.serial)
        node_x = real_node.x
        node_y = real_node.y
        return screen_edges["bottom_left"].get_x() < node_x < screen_edges["top_right"].get_x() and \
                screen_edges["bottom_left"].get_y() < node_y < screen_edges["top_right"].get_y()

    def get_partly_visible_edge(self, edge, top, bottom, left, right, node, edge_equation):
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
        first_node = None
        second_node = None

        if node:
            first_node = self.original_graph.get_node_by_serial(node.serial)

        # check if edge collides with top border
        if LineEquation.check_collision_point(edge_equation, top):
            col_point = LineEquation.get_equation_collision_point(edge_equation, top)
            location = {'x': round(col_point.x, 2), 'y': round(col_point.y, 2)}
            if first_node is not None:
                second_node = NodeObject(serial=get_serial(), location=location, size=0)
                second_node.real = False
            else:
                first_node = NodeObject(serial=get_serial(), location=location, size=0)
                first_node.real = False

        # check if edge collides with bottom border
        if LineEquation.check_collision_point(edge_equation, bottom):
            col_point = LineEquation.get_equation_collision_point(edge_equation, bottom)
            location = {'x': round(col_point.x, 2), 'y': round(col_point.y, 2)}
            if first_node is not None:
                second_node = NodeObject(serial=get_serial(), location=location, size=0)
                second_node.real = False
            else:
                first_node = NodeObject(serial=get_serial(), location=location, size=0)
                first_node.real = False

        # check if edge collides with left border
        if LineEquation.check_collision_point(edge_equation, left):
            col_point = LineEquation.get_equation_collision_point(edge_equation, left)
            location = {'x': round(col_point.x, 2), 'y': round(col_point.y, 2)}
            if first_node is not None:
                second_node = NodeObject(serial=get_serial(), location=location, size=0)
                second_node.real = False

            else:
                first_node = NodeObject(serial=get_serial(), location=location, size=0)
                first_node.real = False

        # check if edge collides with right border
        if LineEquation.check_collision_point(edge_equation, right):
            col_point = LineEquation.get_equation_collision_point(edge_equation, right)
            location = {'x': round(col_point.x, 2), 'y': round(col_point.y, 2)}
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
            curr_edge = (first_node, second_node, edge.slope, edge_equation)
        else:
            curr_edge = (second_node, first_node, edge.slope, edge_equation)

        return curr_edge

    def stop_me(self):
        self.stop()