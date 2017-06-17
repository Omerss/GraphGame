import xml.sax
from NodeObject import NodeObject
from Enums import Colours, Shapes
from GraphObj import GraphObject
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import xml.etree.cElementTree as E


def save_graph(graph, file_name):
    root = E.Element("root")
    graph_xml = E.SubElement(root, "graph_xml")
    node_list = E.SubElement(graph_xml, "node_list")
    E.SubElement(graph_xml,"size",name="size").text = str(graph.size)
    E.SubElement(graph_xml,"extra_distance",name="extra_distance").text=str(graph.extra_distance)
    E.SubElement(graph_xml, "max_neighbors", name="max_neighbors").text=str(graph.max_neighbors)
    E.SubElement(graph_xml, "node_count", name="node_count").text = str(graph.node_count)
    E.SubElement(graph_xml, "line_colour", name="line_colour").text = graph.line_colour['name']
    E.SubElement(graph_xml,"connections",name="connections").text=str(graph.connections)

    for i in range(0, len(graph.node_list)):
        E.SubElement(node_list,"node_serial_num_{}".format(i), name="node_serial_num_{}".format(i)).text = "{}".format(graph.node_list[i].serial_num)
        E.SubElement(node_list, "node_colour_{}".format(i), name="node_colour_{}".format(i)).text =graph.node_list[i].colour
        E.SubElement(node_list, "node_shape_{}".format(i), name="node_shape_{}".format(i)).text = graph.node_list[i].shape['name']
        E.SubElement(node_list, "node_location_{}".format(i), name="node_location_{}".format(i)).text = \
            str({'x': graph.node_list[i].x, 'y': graph.node_list[i].x})
        E.SubElement(node_list, "node_size_{}".format(i), name="node_size_{}".format(i)).text = "{}".format(graph.node_list[i].size)
        E.SubElement(node_list, "node_neighbors_{}".format(i), name="node_neighbors_{}".format(i)).text = repr(graph.node_list[i].neighbors)
        E.SubElement(node_list, "possible_neighbors_{}".format(i), name="possible_neighbors_{}".format(i)).text = repr(graph.node_list[i].possible_neighbors)

        tree = E.ElementTree(root)
        tree.write(file_name)

