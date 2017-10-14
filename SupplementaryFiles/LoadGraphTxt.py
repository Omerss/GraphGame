
from GraphObj import GraphObject
from KivyFiles.Questions.QuestionObject import QuestionObject
from NodeObject import NodeObject
from SupplementaryFiles.Enums import Colours, Shapes
from SupplementaryFiles.GraphObj import GraphObject
import ast
from os import path

def parse_line(line):
    point_index = line.find(".")
    equal_index = line.find("=")
    new_dict = {}
    new_dict[line[:point_index]] = {}
    new_dict[line[:point_index]][line[point_index + 1:equal_index]] = line[equal_index + 1:]
    return new_dict

def read_file(config_path):
    config_dict = {}
    with open(config_path, 'r') as f:
        for line in f:
            new_line = parse_line(line)
            key = new_line.keys()
            if not key[0] in config_dict:
                config_dict[key[0]] = {}
            inner_key = new_line[key[0]].keys()
            config_dict[key[0]][inner_key[0]] = new_line[key[0]][inner_key[0]].rstrip()
    return config_dict


def load_graph_from_file(file_name):


    import Enums
    if not path.exists(file_name):
        raise IOError("File not found", path=file_name)
    new_graph = GraphObject()

    graph_dict = read_file(file_name)
    new_graph.size = ast.literal_eval(graph_dict['graph']['size'])
    new_graph.extra_distance = int(graph_dict['graph']['extra_distance'])
    new_graph.center_node = graph_dict['graph']['center_node']
    new_graph.max_neighbors = int(graph_dict['graph']['max_neighbors'])
    new_graph.line_colour = from_name_to_color(graph_dict['graph']['line_colour'])
    new_graph.node_count = int(graph_dict['graph']['node_count'])
    new_graph.connections = ast.literal_eval(graph_dict['graph']['connections'])
    i=0
    question = ''
    while True:
        if ('question{0}'.format(i) in graph_dict):
            question_string = graph_dict['question{0}'.format(i)]["question_string"]
            question_type_number = int(graph_dict['question{0}'.format(i)]["question_type_number"])
            question_id = int(graph_dict['question{0}'.format(i)]["question_id"])
            args = graph_dict['question{0}'.format(i)]["args"]
            # function_args = []
            # if args is not None:
            #     graph_args = eval(args.text).split(',')
            #     for item in args:
            #         tmp = from_name_to_color(item)
            #         if tmp == -1:
            #             function_args.append(int(item))
            #         else:
            #             function_args.append(tmp)
            # question = QuestionObject(question_string, question_type_number, question_id, *function_args)
            question = QuestionObject(question_string, question_type_number, question_id, args)
            new_graph.question_object_list.append(question)
            i = i+1
        else:
            i = 0
            break


    # get the node list from the tree
# serial, location, size, colour=Colours['red'], shape=Shapes['circle'], real=True, dummy_num=None
    while True:
        if ('node{0}'.format(i) in graph_dict):
            serial_num = graph_dict['node{0}'.format(i)]["serial_num"]
            location =  {'x': int(graph_dict['node{0}'.format(i)]["node_x"]),
                         'y': int(graph_dict['node{0}'.format(i)]["node_y"])}
            node_size = int(graph_dict['node{0}'.format(i)]["node_size"])
            colour = from_name_to_color(graph_dict['node{0}'.format(i)]["colour"])
            shape = from_name_to_shape(graph_dict['node{0}'.format(i)]["shape"])
            real = bool(graph_dict['node{0}'.format(i)]["real"])
            dummy_num = int(graph_dict['node{0}'.format(i)]["dummy_num"])
            neighbors = set(eval(graph_dict['node{0}'.format(i)]["neighbors"]))
            possible_neighbors = set(eval(graph_dict['node{0}'.format(i)]["possible_neighbors"]))
            node = NodeObject(serial_num, location, node_size, colour, shape, real, dummy_num)
            node.neighbors = neighbors
            node.possible_neighbors= possible_neighbors
            new_graph.node_list.append(node)
            i = i+1
        else:
            break
    return new_graph

def from_name_to_color(name):
    from SupplementaryFiles import Enums

    if name == "red":
        return Enums.Colours['red']
    if name == "yellow":
        return Enums.Colours['yellow']
    if name == "blue":
        return Enums.Colours['blue']
    return -1


def from_name_to_shape(name):
    from SupplementaryFiles import Enums

    if name == "Circle":
        return Enums.Shapes['circle']
