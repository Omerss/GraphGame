from GraphObj import GraphObject
from KivyFiles.Questions.QuestionObject import QuestionObject
from NodeObject import NodeObject
from SupplementaryFiles.Enums import Colours, QuestionTypes
from SupplementaryFiles.GraphObj import GraphObject


def load_py_graph(graph_name):
    if graph_name == 'graph_1':
        return create_graph_1()
    if graph_name == 'graph_2':
        return create_graph_2()
    if graph_name == 'graph_3':
        return create_graph_3()
    if graph_name == 'graph_4':
        return create_graph_4()
    if graph_name == 'graph_5':
        return create_graph_5()
    if graph_name == 'graph_6':
        return create_graph_6()
    if graph_name == 'graph_7':
        return create_graph_7()
    if graph_name == 'graph_8':
        return create_graph_8()
    if graph_name == 'graph_9':
        return create_graph_9()
    if graph_name == 'graph_10':
        return create_graph_10()


def create_graph_1():
    # Arrange
    max_neighbors = 5
    extra_distance = 1

    draft_graph = GraphObject(max_x=1050, max_y=1800, node_count=15, max_neighbors=max_neighbors,
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

    question_one = QuestionObject("How many red nodes are there?",
                                  QuestionTypes['NUMBER'], 1, Colours['red'])
    question_two = QuestionObject("How many blue nodes do not have links to yellow nodes",
                                  QuestionTypes['NUMBER'], 5, Colours['blue'], Colours['yellow'])
    question_three = QuestionObject("Which color has the largest number of nodes?",
                                    QuestionTypes['MULTIPLE_CHOICE'], 16)
    question_four = QuestionObject("Is there a blue node that has at least 2 links to another blue node?",
                                   QuestionTypes['BOOLEAN'], 11, Colours['blue'], 2)
    question_five = QuestionObject("What is the color of the node with the largest number of links?",
                                   QuestionTypes['MULTIPLE_CHOICE'], 3)
    question_six = QuestionObject("Is every blue node linked to a red node?",
                                  QuestionTypes['BOOLEAN'], 9, Colours['blue'], Colours['red'])
    question_seven = QuestionObject("Is there an even number of yellow nodes?",
                                    QuestionTypes['BOOLEAN'], 15, Colours['yellow'], 0)
    draft_graph.question_object_list = [question_one, question_two, question_three, question_four, question_five,
                                        question_six, question_seven]

    return draft_graph


def create_graph_2():
    draft_graph = GraphObject(max_x=1250, max_y=1800, node_count=15, max_neighbors=5, extra_distance=1)
    draft_graph.add_node(x_loc=904, y_loc=1191, node_colour=Colours['yellow'], serial="n1")
    draft_graph.add_node(x_loc=1021, y_loc=1537, node_colour=Colours['red'], serial="n2")
    draft_graph.add_node(x_loc=523, y_loc=1407, node_colour=Colours['blue'], serial="n3")
    draft_graph.add_node(x_loc=783, y_loc=1052, node_colour=Colours['blue'], serial="n4")
    draft_graph.add_node(x_loc=322, y_loc=1167, node_colour=Colours['red'], serial="n5")
    draft_graph.add_node(x_loc=143, y_loc=802, node_colour=Colours['red'], serial="n6")
    draft_graph.add_node(x_loc=133, y_loc=1107, node_colour=Colours['yellow'], serial="n7")
    draft_graph.add_node(x_loc=376, y_loc=408, node_colour=Colours['blue'], serial="n8")
    draft_graph.add_node(x_loc=144, y_loc=459, node_colour=Colours['red'], serial="n9")
    draft_graph.add_node(x_loc=551, y_loc=843, node_colour=Colours['red'], serial="n10")
    draft_graph.add_node(x_loc=836, y_loc=483, node_colour=Colours['blue'], serial="n11")
    draft_graph.add_node(x_loc=954, y_loc=206, node_colour=Colours['red'], serial="n12")
    draft_graph.add_node(x_loc=631, y_loc=613, node_colour=Colours['yellow'], serial="n13")
    draft_graph.add_node(x_loc=1115, y_loc=596, node_colour=Colours['yellow'], serial="n14")
    draft_graph.add_node(x_loc=312, y_loc=1340, node_colour=Colours['blue'], serial="n15")

    draft_graph.center_node = "n1"

    for node in draft_graph.node_list:
        draft_graph.get_possible_connections(node.serial_num)

    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n3"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n5"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n7"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n10"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n12"), draft_graph.get_node_by_serial("n11"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n6"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n11"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n13"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n14"), draft_graph.get_node_by_serial("n12"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n7"), draft_graph.get_node_by_serial("n15"))

    question_one = QuestionObject("How many red nodes do not have links to yellow nodes?",
                                  QuestionTypes['NUMBER'], 5, Colours['red'], Colours['yellow'])
    question_two = QuestionObject("Is the number of red nodes even?",
                                  QuestionTypes['BOOLEAN'], 15, Colours['red'], 0)
    question_three = QuestionObject("Does all the blue nodes have an odd number of links?",
                                    QuestionTypes['BOOLEAN'], 13, Colours['blue'], 1)
    question_four = QuestionObject("What is the color that contains the smallest total number of links?",
                                   QuestionTypes['MULTIPLE_CHOICE'], 7)
    question_five = QuestionObject("Does every yellow node have a link to a red node?",
                                   QuestionTypes['BOOLEAN'], 9, Colours['yellow'], Colours['red'])
    question_six = QuestionObject("Are there more blue nodes than yellow nodes?",
                                  QuestionTypes['BOOLEAN'], 10, Colours['blue'], Colours['yellow'])
    question_seven = QuestionObject("Is there a red nodes that has a link to another red node?",
                                    QuestionTypes['BOOLEAN'], 8, Colours['red'])
    draft_graph.question_object_list = [question_one, question_two, question_three, question_four, question_five,
                                        question_six, question_seven]
    return draft_graph


def create_graph_3():

    draft_graph = GraphObject(max_x=1250, max_y=1600, node_count=15, max_neighbors=5, extra_distance=1)
    draft_graph.add_node(x_loc=26, y_loc=50, node_colour=Colours['yellow'], serial="n1")
    draft_graph.add_node(x_loc=451, y_loc=400, node_colour=Colours['blue'], serial="n2")
    draft_graph.add_node(x_loc=201, y_loc=520, node_colour=Colours['blue'], serial="n3")
    draft_graph.add_node(x_loc=750, y_loc=320, node_colour=Colours['blue'], serial="n4")
    draft_graph.add_node(x_loc=660, y_loc=748, node_colour=Colours['yellow'], serial="n5")
    draft_graph.add_node(x_loc=1200, y_loc=400, node_colour=Colours['red'], serial="n6")
    draft_graph.add_node(x_loc=790, y_loc=50, node_colour=Colours['yellow'], serial="n7")
    draft_graph.add_node(x_loc=871, y_loc=1052, node_colour=Colours['yellow'], serial="n8")
    draft_graph.add_node(x_loc=1040, y_loc=680, node_colour=Colours['blue'], serial="n9")
    draft_graph.add_node(x_loc=471, y_loc=1204, node_colour=Colours['red'], serial="n10")
    draft_graph.add_node(x_loc=1210, y_loc=1282, node_colour=Colours['red'], serial="n11")
    draft_graph.add_node(x_loc=55, y_loc=910, node_colour=Colours['blue'], serial="n12")
    draft_graph.add_node(x_loc=202, y_loc=1437, node_colour=Colours['yellow'], serial="n13")
    draft_graph.add_node(x_loc=661, y_loc=1508, node_colour=Colours['red'], serial="n14")
    draft_graph.add_node(x_loc=991, y_loc=1542, node_colour=Colours['blue'], serial="n15")

    draft_graph.center_node = "n2"

    for node in draft_graph.node_list:
        draft_graph.get_possible_connections(node.serial_num)

    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n3"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n2"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n4"), draft_graph.get_node_by_serial("n5"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n4"), draft_graph.get_node_by_serial("n6"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n7"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n10"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n11"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n5"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n9"), draft_graph.get_node_by_serial("n11"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n12"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n13"), draft_graph.get_node_by_serial("n10"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n14"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n15"), draft_graph.get_node_by_serial("n14"))

    question_one = QuestionObject('Is there a red node with an odd number of links?',
                                  QuestionTypes['BOOLEAN'], 12, Colours['red'], 1)
    question_two = QuestionObject('Which color has the smallest number of nodes?',
                                  QuestionTypes['MULTIPLE_CHOICE'], 17)
    question_three = QuestionObject('How many blue nodes are there?',
                                    QuestionTypes['NUMBER'], 1, Colours['blue'])
    question_four = QuestionObject('What is the color of the node with the largest number of links?',
                                   QuestionTypes['MULTIPLE_CHOICE'], 3)
    question_five = QuestionObject('Does every red node have a link to a yellow node?',
                                   QuestionTypes['BOOLEAN'], 9, Colours['red'], Colours['yellow'])
    question_six = QuestionObject('Does all the blue nodes have an even number of links?',
                                  QuestionTypes['BOOLEAN'], 13, Colours['blue'], 0)
    question_seven = QuestionObject('Are there more red nodes than blue nodes?',
                                    QuestionTypes['BOOLEAN'], 10, Colours['red'], Colours['blue'])
    draft_graph.question_object_list = [question_one, question_two, question_three, question_four, question_five,
                                        question_six, question_seven]

    return draft_graph


def create_graph_4():

    draft_graph = GraphObject(max_x=2000, max_y=1500, node_count=15, max_neighbors=5, extra_distance=1)
    draft_graph.add_node(x_loc=390, y_loc=920, node_colour=Colours['blue'], serial="n1")
    draft_graph.add_node(x_loc=200, y_loc=1100, node_colour=Colours['yellow'], serial="n2")
    draft_graph.add_node(x_loc=40, y_loc=500, node_colour=Colours['blue'], serial="n3")
    draft_graph.add_node(x_loc=695, y_loc=1105, node_colour=Colours['red'], serial="n4")
    draft_graph.add_node(x_loc=880, y_loc=1000, node_colour=Colours['yellow'], serial="n5")
    draft_graph.add_node(x_loc=1240, y_loc=1005, node_colour=Colours['yellow'], serial="n6")
    draft_graph.add_node(x_loc=997, y_loc=1297, node_colour=Colours['blue'], serial="n7")
    draft_graph.add_node(x_loc=1400, y_loc=700, node_colour=Colours['blue'], serial="n8")
    draft_graph.add_node(x_loc=745, y_loc=800, node_colour=Colours['red'], serial="n9")
    draft_graph.add_node(x_loc=1850, y_loc=705, node_colour=Colours['blue'], serial="n10")
    draft_graph.add_node(x_loc=1500, y_loc=955, node_colour=Colours['yellow'], serial="n11")
    draft_graph.add_node(x_loc=1950, y_loc=900, node_colour=Colours['red'], serial="n12")
    draft_graph.add_node(x_loc=200, y_loc=760, node_colour=Colours['red'], serial="n13")
    draft_graph.add_node(x_loc=1200, y_loc=312, node_colour=Colours['red'], serial="n14")
    draft_graph.add_node(x_loc=1405, y_loc=1100, node_colour=Colours['red'], serial="n15")

    draft_graph.center_node = "n1"

    for node in draft_graph.node_list:
        draft_graph.get_possible_connections(node.serial_num)

    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n13"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n2"), draft_graph.get_node_by_serial("n3"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n2"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n13"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n4"), draft_graph.get_node_by_serial("n5"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n7"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n11"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n15"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n7"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n7"), draft_graph.get_node_by_serial("n15"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n10"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n14"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n12"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n14"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n15"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n12"), draft_graph.get_node_by_serial("n15"))
    question_one = QuestionObject('Is there a red node that has at least two links to another red node?',
                                  QuestionTypes['BOOLEAN'], 11, Colours['red'], 2)
    question_two = QuestionObject('Is the sum of the links of all the red nodes even?',
                                  QuestionTypes['BOOLEAN'], 14, Colours['red'], 0)
    question_three = QuestionObject('Which color has the largest number of nodes?',
                                    QuestionTypes['MULTIPLE_CHOICE'], 16)
    question_four = QuestionObject('How many blue nodes have links to yellow nodes?',
                                   QuestionTypes['NUMBER'], 2, Colours['blue'], Colours['yellow'])
    question_five = QuestionObject('What is the color that contains the largest total number of links?',
                                   QuestionTypes['MULTIPLE_CHOICE'], 4)
    question_six = QuestionObject('Does every yellow node have a link to a red node?',
                                  QuestionTypes['BOOLEAN'], 9, Colours['yellow'], Colours['red'])
    question_seven = QuestionObject('Are there more blue nodes than yellow nodes?',
                                    QuestionTypes['BOOLEAN'], 10, Colours['blue'], Colours['yellow'])
    draft_graph.question_object_list = [question_one, question_two, question_three, question_four, question_five,
                                        question_six, question_seven]

    return draft_graph


def create_graph_5():

    draft_graph = GraphObject(max_x=1250, max_y=1800, node_count=15, max_neighbors=5, extra_distance=1)
    draft_graph.add_node(x_loc=169, y_loc=1534, node_colour=Colours['red'], serial='n1')
    draft_graph.add_node(x_loc=142, y_loc=243, node_colour=Colours['red'], serial='n2')
    draft_graph.add_node(x_loc=274, y_loc=1047, node_colour=Colours['red'], serial='n3')
    draft_graph.add_node(x_loc=78, y_loc=1383, node_colour=Colours['blue'], serial='n4')
    draft_graph.add_node(x_loc=140, y_loc=635, node_colour=Colours['blue'], serial='n5')
    draft_graph.add_node(x_loc=728, y_loc=1521, node_colour=Colours['yellow'], serial='n6')
    draft_graph.add_node(x_loc=754, y_loc=283, node_colour=Colours['blue'], serial='n7')
    draft_graph.add_node(x_loc=769, y_loc=1194, node_colour=Colours['blue'], serial='n8')
    draft_graph.add_node(x_loc=469, y_loc=1312, node_colour=Colours['blue'], serial='n9')
    draft_graph.add_node(x_loc=701, y_loc=894, node_colour=Colours['yellow'], serial='n10')
    draft_graph.add_node(x_loc=607, y_loc=84, node_colour=Colours['blue'], serial='n11')
    draft_graph.add_node(x_loc=839, y_loc=820, node_colour=Colours['red'], serial='n12')
    draft_graph.add_node(x_loc=837, y_loc=190, node_colour=Colours['yellow'], serial='n13')
    draft_graph.add_node(x_loc=604, y_loc=1648, node_colour=Colours['red'], serial='n14')
    draft_graph.add_node(x_loc=957, y_loc=447, node_colour=Colours['red'], serial='n15')

    draft_graph.center_node = "n5"

    for node in draft_graph.node_list:
        draft_graph.get_possible_connections(node.serial_num)

    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n3"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n2"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n10"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n12"), draft_graph.get_node_by_serial("n10"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n12"), draft_graph.get_node_by_serial("n11"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n12"), draft_graph.get_node_by_serial("n13"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n13"), draft_graph.get_node_by_serial("n15"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n7"), draft_graph.get_node_by_serial("n13"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n14"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n12"))

    question_one = QuestionObject('Is there a yellow node that has at least 3 links to another yellow node?',
                                  QuestionTypes['BOOLEAN'], 11, Colours['yellow'], 3)
    question_two = QuestionObject('Does all the red nodes have an odd number of links?',
                                  QuestionTypes['BOOLEAN'], 13, Colours['red'], 1)
    question_three = QuestionObject('How many yellow nodes are there?',
                                    QuestionTypes['NUMBER'], 1, Colours['yellow'])
    question_four = QuestionObject('What is the color that contains the smallest total number of links?',
                                   QuestionTypes['MULTIPLE_CHOICE'], 7)
    question_five = QuestionObject('Does every blue node have a link to a yellow node?',
                                   QuestionTypes['BOOLEAN'], 9, Colours['blue'], Colours['yellow'])
    question_six = QuestionObject('Is the number of blue nodes even?',
                                  QuestionTypes['BOOLEAN'], 15, Colours['blue'], 0)
    question_seven = QuestionObject('How many yellow nodes do not have links to red nodes?',
                                    QuestionTypes['NUMBER'], 5, Colours['yellow'], Colours['red'])
    draft_graph.question_object_list = [question_one, question_two, question_three, question_four, question_five,
                                        question_six, question_seven]

    return draft_graph


def create_graph_6():
    pass


def create_graph_7():
    pass


def create_graph_8():
    pass


def create_graph_9():
    pass


def create_graph_10():
    draft_graph = GraphObject(max_x=2350, max_y=3500, node_count=15, max_neighbors=5, extra_distance=1)
    draft_graph.add_node(x_loc=138, y_loc=2500, node_colour=Colours['blue'], serial='n1')
    draft_graph.add_node(x_loc=487, y_loc=2800, node_colour=Colours['yellow'], serial='n2')
    draft_graph.add_node(x_loc=1178, y_loc=2280, node_colour=Colours['blue'], serial='n3')
    draft_graph.add_node(x_loc=1640, y_loc=2700, node_colour=Colours['blue'], serial='n4')
    draft_graph.add_node(x_loc=1755, y_loc=1700, node_colour=Colours['red'], serial='n5')
    draft_graph.add_node(x_loc=1986, y_loc=1200, node_colour=Colours['red'], serial='n6')
    draft_graph.add_node(x_loc=1293, y_loc=1000, node_colour=Colours['red'], serial='n7')
    draft_graph.add_node(x_loc=1409, y_loc=700, node_colour=Colours['blue'], serial='n8')
    draft_graph.add_node(x_loc=1180, y_loc=200, node_colour=Colours['red'], serial='n14')
    draft_graph.add_node(x_loc=2286, y_loc=700, node_colour=Colours['yellow'], serial='n9')
    draft_graph.add_node(x_loc=718, y_loc=1100, node_colour=Colours['blue'], serial='n10')
    draft_graph.add_node(x_loc=346, y_loc=1704, node_colour=Colours['red'], serial='n11')
    draft_graph.add_node(x_loc=69, y_loc=1820, node_colour=Colours['yellow'], serial='n12')
    draft_graph.add_node(x_loc=489, y_loc=1880, node_colour=Colours['blue'], serial='n13')
    draft_graph.add_node(x_loc=189, y_loc=3440, node_colour=Colours['blue'], serial='n15')
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

    question_one = QuestionObject('Is there a yellow node that has at least 3 links to another yellow node?',
                                  QuestionTypes['BOOLEAN'], 11, Colours['yellow'], 3)
    question_two = QuestionObject('Does all the red nodes have an odd number of links?',
                                  QuestionTypes['BOOLEAN'], 13, Colours['red'], 1)
    question_three = QuestionObject('How many yellow nodes are there?',
                                    QuestionTypes['NUMBER'], 1, Colours['yellow'])
    question_four = QuestionObject('What is the color that contains the smallest total number of links?',
                                   QuestionTypes['MULTIPLE_CHOICE'], 7)
    question_five = QuestionObject('Does every blue node have a link to a yellow node?',
                                   QuestionTypes['BOOLEAN'], 9, Colours['blue'], Colours['yellow'])
    question_six = QuestionObject('Is the number of blue nodes even?',
                                  QuestionTypes['BOOLEAN'], 15, Colours['blue'], 0)
    question_seven = QuestionObject('How many yellow nodes do not have links to red nodes?',
                                    QuestionTypes['NUMBER'], 5, Colours['yellow'], Colours['red'])
    draft_graph.question_object_list = [question_one, question_two, question_three, question_four, question_five,
                                        question_six, question_seven]

    return draft_graph


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
        i += 1

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
        i += 1
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
