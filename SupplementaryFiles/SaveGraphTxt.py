import json
import xml.sax

from os import path, makedirs

from NodeObject import NodeObject
from Enums import Colours, Shapes
from GraphObj import GraphObject
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import xml.etree.cElementTree as E

# SAVED_GRAPH_PATH = "../TestingGraphs"
SAVED_GRAPH_PATH = "../GraphsData"


def save_graph(graph, file_name):
    file_path = path.join(SAVED_GRAPH_PATH, file_name)
    with open (file_path, 'w') as output:
        output.write("graph.center_node={0}\n".format(graph.center_node))
        output.write("graph.size={0}\n".format(graph.size))
        output.write("graph.extra_distance={0}\n".format(graph.extra_distance))
        output.write("graph.max_neighbors={0}\n".format(graph.max_neighbors))
        output.write("graph.node_count={0}\n".format(graph.node_count))
        output.write("graph.line_colour={0}\n".format(graph.line_colour))
        output.write("graph.connections={0}\n".format(graph.connections))

        #question_object_list
        for i in range(len(graph.question_object_list)):
            output.write("question{0}.question_string={1}\n".format(i,graph.question_object_list[i].question_string))
            output.write("question{0}.question_type_number={1}\n".format(i,graph.question_object_list[i].question_type_number))
            output.write("question{0}.question_id={1}\n".format(i,graph.question_object_list[i].question_id))
            output.write("question{0}.args={1}\n".format(i,graph.question_object_list[i].args))

        #node list
        for i in range(len(graph.node_list)):
            output.write("node{0}.serial_num={1}\n".format(i,graph.node_list[i].serial_num))
            output.write("node{0}.node_x={1}\n".format(i,graph.node_list[i].x))
            output.write("node{0}.node_y={1}\n".format(i,graph.node_list[i].y))
            output.write("node{0}.node_size={1}\n".format(i,graph.node_list[i].size))
            output.write("node{0}.colour={1}\n".format(i,graph.node_list[i].colour['name']))
            output.write("node{0}.shape={1}\n".format(i,graph.node_list[i].shape))
            output.write("node{0}.real={1}\n".format(i,graph.node_list[i].real))
            output.write("node{0}.dummy_num={1}\n".format(i,graph.node_list[i].dummy_num))
            output.write("node{0}.neighbors={1}\n".format(i, graph.node_list[i].neighbors))
            output.write("node{0}.possible_neighbors={1}\n".format(i, graph.node_list[i].possible_neighbors))


def save_graph_json(graph, file_name):
    file_path = path.join(SAVED_GRAPH_PATH, file_name)
    file_data = {"center_node": graph.center_node, "size": graph.size, "extra_distance": graph.extra_distance,
                 "max_neighbors": graph.max_neighbors, "node_count": graph.node_count, "line_colour": graph.line_colour,
                 "connections": graph.connections, "question_object_list": {}, "node_list": {}}

    #question_object_list
    for i in range(len(graph.question_object_list)):
        file_data["question_object_list"][str(i)] = {}
        file_data["question_object_list"][str(i)]["question_string"] = graph.question_object_list[i].question_string
        file_data["question_object_list"][str(i)]["question_type_number"] = graph.question_object_list[i].question_type_number
        file_data["question_object_list"][str(i)]["question_id"] = graph.question_object_list[i].question_id
        file_data["question_object_list"][str(i)]["args"] = json.dumps(graph.question_object_list[i].args)

    #node list
    for i in range(len(graph.node_list)):
        serial = graph.node_list[i].serial_num
        file_data["node_list"][serial] = {}
        file_data["node_list"][serial]["node_x"] = graph.node_list[i].x
        file_data["node_list"][serial]["node_y"] = graph.node_list[i].y
        file_data["node_list"][serial]["node_size"] = graph.node_list[i].size
        file_data["node_list"][serial]["colour"] = str(graph.node_list[i].colour['name'])
        file_data["node_list"][serial]["shape"] = graph.node_list[i].shape
        file_data["node_list"][serial]["real"] = graph.node_list[i].real
        file_data["node_list"][serial]["dummy_num"] = graph.node_list[i].dummy_num
        file_data["node_list"][serial]["neighbors"] = json.dumps(list(graph.node_list[i].neighbors))
        file_data["node_list"][serial]["possible_neighbors"] = json.dumps(list(graph.node_list[i].possible_neighbors))

    with open(file_path, 'w') as output:
        output.write(json.dumps(file_data))

