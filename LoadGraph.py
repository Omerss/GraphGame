import xml.sax
from NodeObject import NodeObject
from Enums import Colours, Shapes
from GraphObj import GraphObject
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import xml.etree.cElementTree as E


def load_graph(file_name):

    tree = E.parse(file_name)
    root = tree.getroot()
    graph_xml = root.find("graph_xml")
    node_list = graph_xml.find("node_list")
    new_graph = GraphObject()
    new_graph.size= graph_xml.find("size").text
    new_graph.extra_distance = graph_xml.find("extra_distance").text
    new_graph.max_neighbors = graph_xml.find("max_neighbors").text

    # get the node list from the tree
    graph_node_list = []
    i=0
    #while we find more nodes in the tree we continue to store them in the list
    while (node_list.find("node_serial_num_{}".format(i))!= None):
        node_serial_num=node_list.find("node_serial_num_{}".format(i))
        node_colour=node_list.find("node_colour_{}".format(i))
        node_shape=node_list.find("node_shape_{}".format(i))
        node_location=node_list.find("node_location_{}".format(i))
        node_size=node_list.find("node_size_{}".format(i))
        node_neighbors=node_list.find("node_neighbors_{}".format(i))
        possible_neighbors=node_list.find("possible_neighbors_{}".format(i))
        new_node=NodeObject(node_serial_num, node_location, node_size, node_colour, node_shape)
        new_node.neighbors=node_neighbors
        new_node.possible_neighbors=possible_neighbors
        new_graph.node_list[i]=new_node
        i=i+1

    return new_graph