import ast
import xml.etree.cElementTree as E

import Enums
from GraphObj import GraphObject
from NodeObject import NodeObject
from Questions.QuestionObject import QuestionObject


def load_graph_from_file(file_name):
    tree = E.parse(file_name)
    root = tree.getroot()
    graph_xml = root.find("graph_xml")
    node_list = graph_xml.find("node_list")
    new_graph = GraphObject()
    new_graph.size = ast.literal_eval(graph_xml.find("size").text)
    new_graph.extra_distance = int(graph_xml.find("extra_distance").text)
    new_graph.center_node = graph_xml.find("center_node").text
    new_graph.max_neighbors = int(graph_xml.find("max_neighbors").text)
    new_graph.line_colour = from_name_to_color(graph_xml.find("line_colour").text)
    new_graph.node_count = int(graph_xml.find("node_count").text)
    new_graph.connections = ast.literal_eval(graph_xml.find("connections").text)
    question_object_list = graph_xml.find("question_object_list")

    # get the node list from the tree
    i = 0
    # while we find more nodes in the tree we continue to store them in the list
    while node_list.find("node_serial_num_{}".format(i)) is not None:
        node_serial_num = node_list.find("node_serial_num_{}".format(i)).text
        node_colour = from_name_to_color(node_list.find("node_colour_{}".format(i)).text)
        node_shape = from_name_to_shape(node_list.find("node_shape_{}".format(i)).text)
        node_location = {'x': int(node_list.find("node_x_{}".format(i)).text),
                         'y': int(node_list.find("node_y_{}".format(i)).text)}
        node_size = int(node_list.find("node_size_{}".format(i)).text)
        node_neighbors = set(eval(node_list.find("node_neighbors_{}".format(i)).text))
        possible_neighbors = set(eval(node_list.find("possible_neighbors_{}".format(i)).text))
        new_node = NodeObject(node_serial_num, node_location, node_size, node_colour, node_shape)
        new_node.neighbors = node_neighbors
        new_node.possible_neighbors = possible_neighbors
        new_graph.node_list.append(new_node)
        i = i + 1

    # question_string, question_type_number, question_id, *args
    i = 0
    while question_object_list.find("question_id_{}".format(i)) is not None:
        question_type_number = int(question_object_list.find("question_type_number_{}".format(i)).text)
        question_string = question_object_list.find("question_string_{}".format(i)).text
        question_id = int(question_object_list.find("question_id_{}".format(i)).text)
        graph_args = question_object_list.find("args_{}".format(i))
        function_args = []
        if graph_args is not None:
            graph_args = eval(graph_args.text).split(',')
            for item in graph_args:
                tmp = from_name_to_color(item)
                if tmp == -1:
                    function_args.append(int(item))
                else:
                    function_args.append(tmp)

        question_object = QuestionObject(question_string, question_type_number, question_id, *function_args)
        new_graph.question_object_list.append(question_object)
        i = i + 1
    return new_graph


def from_name_to_color(name):
    if name == "red":
        return Enums.Colours['red']
    if name == "yellow":
        return Enums.Colours['yellow']
    if name == "blue":
        return Enums.Colours['blue']
    return -1


def from_name_to_shape(name):
    if name == "Circle":
        return Enums.Shapes.circle
