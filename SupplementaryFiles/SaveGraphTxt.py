import xml.sax

from os import path, makedirs

from NodeObject import NodeObject
from Enums import Colours, Shapes
from GraphObj import GraphObject
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import xml.etree.cElementTree as E
SAVED_GRAPH_PATH = "../TestingGraphs"


def save_graph(graph, file_name):
    file_path = path.join(SAVED_GRAPH_PATH, file_name,'.txt')
    with open (file_path, 'w') as output:
        output.write("graph.center_node={0}\n".format(graph.center_node))
        output.write("graph.size={0}\n".format(graph.size))
        output.write("graph.extra_distance={0}\n".format(graph.extra_distance))
        output.write("graph.max_neighbors={0}\n".format(graph.max_neighbors))
        output.write("graph.node_count={0}\n".format(graph.node_count))
        output.write("graph.line_colour={0}\n".format(graph.line_colour))
        output.write("graph.connections={0}\n".format(graph.connections))

        #question_object_list
        for i in range(len((graph.question_object_list))):
            output.write("question{0}.question_string={1}\n".format(i,graph.question_object_list[i].question_string))
            output.write("question{0}.question_type_number={1}\n".format(i,graph.question_object_list[i].question_type_number))
            output.write("question{0}.question_id={1}\n".format(i,graph.question_object_list[i].question_id))
            output.write("question{0}.args={1}\n".format(i,graph.question_object_list[i].args))

        #node list
        for i in range(len(graph.node_list)):
            output.write("node{0}.serial={1}\n".format(i,graph.node_list[i].serial))
            output.write("node{0}.node_x={1}\n".format(i,graph.node_list[i].x))
            output.write("node{0}.node_y={1}\n".format(i,graph.node_list[i].y))
            output.write("node{0}.node_size={1}\n".format(i,graph.node_list[i].size))
            output.write("node{0}.colour={1}\n".format(i,graph.node_list[i].colour))
            output.write("node{0}.shape={1}\n".format(i,graph.node_list[i].shape))
            output.write("node{0}.real={1}\n".format(i,graph.node_list[i].real))
            output.write("node{0}.dummy_num={1}\n".format(i,graph.node_list[i].dummy_num))
