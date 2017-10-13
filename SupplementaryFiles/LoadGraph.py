from GraphObj import GraphObject
from KivyFiles.Questions.QuestionObject import QuestionObject
from NodeObject import NodeObject
from SupplementaryFiles.Enums import Colours, QuestionTypes
from SupplementaryFiles.GraphObj import GraphObject


def load_py_graph (graph_name):

    if (graph_name== 'graph_1'):
        return create_graph_1()
    if (graph_name == 'graph_2'):
        return create_graph_2()
    if (graph_name == 'graph_3'):
        return create_graph_3()
    if (graph_name == 'graph_4'):
        return create_graph_4()
    if (graph_name == 'graph_5'):
        return create_graph_5()
    if (graph_name == 'graph_6'):
        return create_graph_6()
    if (graph_name == 'graph_7'):
        return create_graph_7()
    if (graph_name == 'graph_8'):
        return create_graph_8()
    if (graph_name == 'graph_9'):
        return create_graph_9()
    if (graph_name == 'graph_10'):
        return create_graph_10()


def create_graph_1():
    # Arrange
    max_neighbors = 5
    extra_distance = 1

    draft_graph = GraphObject(max_x=1050, max_y=1800, node_count=15 , max_neighbors=max_neighbors,
                              extra_distance=extra_distance)
    draft_graph.add_node(x_loc=60, y_loc=1250, node_colour=Colours['blue'], serial="n1")
    draft_graph.add_node(x_loc=211, y_loc=1400, node_colour=Colours['yellow'], serial="n2")
    draft_graph.add_node(x_loc=510, y_loc=1140, node_colour=Colours['blue'], serial="n3")
    draft_graph.add_node(x_loc=710, y_loc=1350, node_colour=Colours['blue'], serial="n4")
    draft_graph.add_node(x_loc=760, y_loc=850, node_colour=Colours['red'], serial="n5")
    draft_graph.add_node(x_loc=860, y_loc=600, node_colour=Colours['red'], serial="n6")
    draft_graph.add_node(x_loc=560, y_loc=500, node_colour=Colours['red'], serial="n7")
    draft_graph.add_node(x_loc=610, y_loc=350, node_colour=Colours['blue'], serial="n8")
    draft_graph.add_node(x_loc=511, y_loc=100, node_colour=Colours['red'], serial="n14")
    draft_graph.add_node(x_loc=990, y_loc=350, node_colour=Colours['yellow'], serial="n9")
    draft_graph.add_node(x_loc=311, y_loc=550, node_colour=Colours['blue'], serial="n10")
    draft_graph.add_node(x_loc=150, y_loc=852, node_colour=Colours['red'], serial="n11")
    draft_graph.add_node(x_loc=25, y_loc=910, node_colour=Colours['yellow'], serial="n12")
    draft_graph.add_node(x_loc=212, y_loc=940, node_colour=Colours['blue'], serial="n13")
    draft_graph.add_node(x_loc=82, y_loc=1720, node_colour=Colours['blue'], serial="n15")
    draft_graph.center_node = "n2"

    for node in draft_graph.node_list:
        draft_graph.get_possible_connections(node.serial_num)

    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n2"), draft_graph.get_node_by_serial("n3"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n5"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n6"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n10"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n11"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n11"), draft_graph.get_node_by_serial("n12"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n11"), draft_graph.get_node_by_serial("n13"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n14"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n7"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n2"), draft_graph.get_node_by_serial("n15"))

    question_one = QuestionObject("how many red nodes are there?",
                                  QuestionTypes['NUMBER'], 1, Colours['red'])
    question_two = QuestionObject("how many blue nodes do not have links to yellow nodes",
                                  QuestionTypes['NUMBER'], 5, Colours['blue'], Colours['yellow'])
    question_three = QuestionObject("which color has the largest number of nodes?",
                                    QuestionTypes['MULTIPLE_CHOICE'], 16)
    question_four = QuestionObject("is there a blue node that has at least 2 links to another blue node?",
                                   QuestionTypes['BOOLEAN'], 11, Colours['blue'], 2)
    question_five = QuestionObject("What is the color of the node with the largest number of links?",
                                   QuestionTypes['MULTIPLE_CHOICE'], 3)
    question_six = QuestionObject("is every blue node linked to a red node?",
                                  QuestionTypes['BOOLEAN'], 9, Colours['blue'], Colours['red'])
    question_seven = QuestionObject("is there an even number of yellow nodes?",
                                    QuestionTypes['BOOLEAN'], 15, Colours['yellow'], 0)
    draft_graph.question_object_list = [question_one, question_two, question_three, question_four, question_five,
                                        question_six, question_seven]

    return draft_graph


def create_graph_2():
    pass

def create_graph_3():
    pass

def create_graph_4():
    pass

def create_graph_5():
    pass

def create_graph_6():
    pass

def create_graph_7():
    pass

def create_graph_8():
    pass

def create_graph_9():
    pass

def create_graph_10():
    pass


def load_graph_from_file(file_name):
    import ast
    import xml.etree.cElementTree as E
    from os import path

    import Enums
    if not path.exists(file_name):
        raise IOError("File not found", path=file_name)

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
