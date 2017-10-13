import unittest
from KivyFiles.GraphTabletDisplay import GraphTabletDisplay
from SupplementaryFiles.Enums import Colours
from SupplementaryFiles.GraphObj import GraphObject
from SupplementaryFiles.SaveGraph import save_graph
from SupplementaryFiles.LoadGraph import load_py_graph


def create_draft_graph_1():

    draft_graph = GraphObject(max_x=1050, max_y=1800, node_count=15 , max_neighbors=5, extra_distance=1)
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
    draft_graph.add_node(x_loc=82, y_loc=1780, node_colour=Colours['blue'], serial="n15")
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

    save_graph(draft_graph, "draft_graph_1.xml")

create_draft_graph_1()


def create_draft_graph_2():

    draft_graph = GraphObject(max_x=1250, max_y=1800, node_count=15 , max_neighbors=5, extra_distance=1)
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

    save_graph(draft_graph, "draft_graph_2.xml")

# create_draft_graph_2()


def create_draft_graph_3():

    draft_graph = GraphObject(max_x=1250, max_y=1600, node_count=15 , max_neighbors=5, extra_distance=1)
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

    save_graph(draft_graph, "draft_graph_3.xml")


def create_draft_graph_4():

    draft_graph = GraphObject(max_x=2000, max_y=2000, node_count=15 , max_neighbors=5, extra_distance=1)
    draft_graph.add_node(x_loc=390, y_loc=920, node_colour=Colours['red'], serial="n1")
    draft_graph.add_node(x_loc=200, y_loc=1100, node_colour=Colours['yellow'], serial="n2")
    draft_graph.add_node(x_loc=40, y_loc=500, node_colour=Colours['blue'], serial="n3")
    draft_graph.add_node(x_loc=695, y_loc=1105, node_colour=Colours['red'], serial="n4")
    draft_graph.add_node(x_loc=880, y_loc=1000, node_colour=Colours['yellow'], serial="n5")
    draft_graph.add_node(x_loc=1240, y_loc=1005, node_colour=Colours['yellow'], serial="n6")
    draft_graph.add_node(x_loc=997, y_loc=1297, node_colour=Colours['blue'], serial="n7")
    draft_graph.add_node(x_loc=1400, y_loc=700, node_colour=Colours['blue'], serial="n8")
    draft_graph.add_node(x_loc=745, y_loc=800, node_colour=Colours['blue'], serial="n9")
    draft_graph.add_node(x_loc=1850, y_loc=705, node_colour=Colours['blue'], serial="n10")
    draft_graph.add_node(x_loc=1500, y_loc=955, node_colour=Colours['yellow'], serial="n11")
    draft_graph.add_node(x_loc=1950, y_loc=900, node_colour=Colours['red'], serial="n12")
    draft_graph.add_node(x_loc=1000, y_loc=300, node_colour=Colours['red'], serial="n13")
    draft_graph.add_node(x_loc=1507, y_loc=312, node_colour=Colours['red'], serial="n14")
    draft_graph.add_node(x_loc=1405, y_loc=1310, node_colour=Colours['red'], serial="n15")

    draft_graph.center_node = "n1"

    for node in draft_graph.node_list:
        draft_graph.get_possible_connections(node.serial_num)

    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n2"), draft_graph.get_node_by_serial("n3"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n2"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n4"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n4"), draft_graph.get_node_by_serial("n5"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n5"), draft_graph.get_node_by_serial("n7"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n8"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n11"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n7"), draft_graph.get_node_by_serial("n15"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n9"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n10"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n13"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n14"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n12"))
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n14"))

    save_graph(draft_graph, "draft_graph_4.xml")

create_draft_graph_4()


def create_draft_graph_5():

    draft_graph = GraphObject(max_x=1250, max_y=1800, node_count=15 , max_neighbors=5, extra_distance=1)
    draft_graph.add_node(x_loc=169, y_loc=1534, node_colour=Colours['red'], serial='n1')
    draft_graph.add_node(x_loc=142, y_loc=243, node_colour=Colours['red'], serial='n2')
    draft_graph.add_node(x_loc=274, y_loc=1047, node_colour=Colours['red'], serial='n3')
    draft_graph.add_node(x_loc=78, y_loc=1383, node_colour=Colours['blue'], serial='n4')
    draft_graph.add_node(x_loc=140, y_loc=635, node_colour=Colours['blue'], serial='n5')
    draft_graph.add_node(x_loc=729, y_loc=1622, node_colour=Colours['blue'], serial='n6')
    draft_graph.add_node(x_loc=754, y_loc=283, node_colour=Colours['blue'], serial='n7')
    draft_graph.add_node(x_loc=769, y_loc=1194, node_colour=Colours['blue'], serial='n8')
    draft_graph.add_node(x_loc=469, y_loc=1312, node_colour=Colours['blue'], serial='n9')
    draft_graph.add_node(x_loc=701, y_loc=894, node_colour=Colours['yellow'], serial='n10')
    draft_graph.add_node(x_loc=607, y_loc=84, node_colour=Colours['blue'], serial='n11')
    draft_graph.add_node(x_loc=839, y_loc=820, node_colour=Colours['red'], serial='n12')
    draft_graph.add_node(x_loc=837, y_loc=190, node_colour=Colours['yellow'], serial='n13')
    draft_graph.add_node(x_loc=605, y_loc=1647, node_colour=Colours['red'], serial='n14')
    draft_graph.add_node(x_loc=957, y_loc=467, node_colour=Colours['red'], serial='n15')

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
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n8"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n11"), draft_graph.get_node_by_serial("n8"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n13"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n14"), draft_graph.get_node_by_serial("n12"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n7"), draft_graph.get_node_by_serial("n15"))

    save_graph(draft_graph, "draft_graph_5.xml")