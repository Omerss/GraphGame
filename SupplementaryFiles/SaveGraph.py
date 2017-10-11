import xml.sax

from os import path, makedirs

from NodeObject import NodeObject
from Enums import Colours, Shapes
from GraphObj import GraphObject
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import xml.etree.cElementTree as E
SAVED_GRAPH_PATH = "../TestingGraphs"


def save_graph(graph, file_name):
    file_path = path.join(SAVED_GRAPH_PATH, file_name)

    root = E.Element("root")
    graph_xml = E.SubElement(root, "graph_xml")
    node_list = E.SubElement(graph_xml, "node_list")
    E.SubElement(graph_xml,"center_node",name="center_node").text = graph.center_node
    E.SubElement(graph_xml, "size", name="size").text = str(graph.size)
    E.SubElement(graph_xml,"extra_distance",name="extra_distance").text=str(graph.extra_distance)
    E.SubElement(graph_xml, "max_neighbors", name="max_neighbors").text=str(graph.max_neighbors)
    E.SubElement(graph_xml, "node_count", name="node_count").text = str(graph.node_count)
    E.SubElement(graph_xml, "line_colour", name="line_colour").text = graph.line_colour['name']
    E.SubElement(graph_xml,"connections",name="connections").text=str(graph.connections)
    E.SubElement(graph_xml,"question_object_list",name="question_object_list").text=str(graph.question_object_list)


    if not path.exists(path.dirname(file_path)):
        try:
            makedirs(path.dirname(file_path))
        except:
            pass
    with open(file_path, 'w+') as f:
        pass
    for i in range(0, len(graph.node_list)):
        E.SubElement(node_list,"node_serial_num_{}".format(i), name="node_serial_num_{}".format(i)).text = graph.node_list[i].serial_num
        E.SubElement(node_list, "node_colour_{}".format(i), name="node_colour_{}".format(i)).text =graph.node_list[i].colour['name']
        E.SubElement(node_list, "node_shape_{}".format(i), name="node_shape_{}".format(i)).text = graph.node_list[i].shape['name']
        E.SubElement(node_list, "node_x_{}".format(i), name="node_x_{}".format(i)).text = str(graph.node_list[i].x)
        E.SubElement(node_list, "node_y_{}".format(i), name="node_y_{}".format(i)).text = str(graph.node_list[i].y)
        E.SubElement(node_list, "node_size_{}".format(i), name="node_size_{}".format(i)).text = "{}".format(graph.node_list[i].size)
        E.SubElement(node_list, "node_neighbors_{}".format(i), name="node_neighbors_{}".format(i)).text = repr(graph.node_list[i].neighbors)
        E.SubElement(node_list, "possible_neighbors_{}".format(i), name="possible_neighbors_{}".format(i)).text = repr(graph.node_list[i].possible_neighbors)
        E.SubElement(node_list, "node_real_{}".format(i), name="node_real_{}".format(i)).text = str(graph.node_list[i].real)

        tree = E.ElementTree(root)
        tree.write(file_path)

