import ast
import xml.etree.cElementTree as E

import Enums
from GraphObj import GraphObject
from NodeObject import NodeObject


def load_graph_from_file(file_name):
    tree = E.parse(file_name)
    root = tree.getroot()
    graph_xml = root.find("graph_xml")
    node_list = graph_xml.find("node_list")
    new_graph = GraphObject()
    new_graph.size = ast.literal_eval(graph_xml.find("size").text)
    new_graph.extra_distance = int(graph_xml.find("extra_distance").text)
    new_graph.max_neighbors = int(graph_xml.find("max_neighbors").text)
    new_graph.line_colour = from_name_to_color(graph_xml.find("line_colour").text)
    new_graph.node_count = int(graph_xml.find("node_count").text)
    new_graph.connections = ast.literal_eval(graph_xml.find("connections").text)



    # get the node list from the tree
    graph_node_list = []
    i=0
    #while we find more nodes in the tree we continue to store them in the list
    while (node_list.find("node_serial_num_{}".format(i))!= None):
        node_serial_num=node_list.find("node_serial_num_{}".format(i)).text
        node_colour=from_name_to_color(node_list.find("node_colour_{}".format(i)).text)
        node_shape=from_name_to_shape(node_list.find("node_shape_{}".format(i)).text)
        node_location={'x' :int(node_list.find("node_x_{}".format(i)).text), 'y':int(node_list.find("node_y_{}".format(i)).text)}
        node_size=int(node_list.find("node_size_{}".format(i)).text)
        node_neighbors=set (eval(node_list.find("node_neighbors_{}".format(i)).text))
        possible_neighbors=set (eval(node_list.find("possible_neighbors_{}".format(i)).text))
        new_node=NodeObject(node_serial_num, node_location, node_size, node_colour, node_shape)
        new_node.neighbors=node_neighbors
        new_node.possible_neighbors=possible_neighbors
        new_graph.node_list.append(new_node)
        i=i+1

    return new_graph


def from_name_to_color(name):

    if name == "red":
        return Enums.Colours['red']
    if name == "yellow":
        return Enums.Colours['yellow']
    if name == "blue":
        return Enums.Colours['blue']


def from_name_to_shape(name):
    if name == "Circle":
        return Enums.Shapes.circle

