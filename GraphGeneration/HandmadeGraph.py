import unittest
from KivyFiles.GraphTabletDisplay import GraphTabletDisplay
from SupplementaryFiles.Enums import Colours
from SupplementaryFiles.GraphObj import GraphObject
from SupplementaryFiles.SaveGraph import save_graph
from SupplementaryFiles.LoadGraph import load_graph_from_file
<<<<<<< HEAD
import threading
import kivyFiles.KivyRunner
from kivyFiles.KivyRunner import GameType
=======

>>>>>>> 65cfe424ccb2d83fdc7156471b6eb3e63dbb53c3

def create_draft_graph_1():
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
    # Arrange
    max_neighbors = 5
    extra_distance = 1

    draft_graph = GraphObject(max_x=1050, max_y=1800, node_count=15 , max_neighbors=max_neighbors,
                              extra_distance=extra_distance)
    draft_graph.add_node(x_loc=1004, y_loc=1621, node_colour=Colours['yellow'], serial="n1")
    draft_graph.add_node(x_loc=1021, y_loc=1707, node_colour=Colours['red'], serial="n2")
    draft_graph.add_node(x_loc=653, y_loc=1607, node_colour=Colours['blue'], serial="n3")
    draft_graph.add_node(x_loc=943, y_loc=1202, node_colour=Colours['blue'], serial="n4")
    draft_graph.add_node(x_loc=422, y_loc=1367, node_colour=Colours['red'], serial="n5")
    draft_graph.add_node(x_loc=303, y_loc=1006, node_colour=Colours['red'], serial="n6")
    draft_graph.add_node(x_loc=233, y_loc=1307, node_colour=Colours['yellow'], serial="n7")
    draft_graph.add_node(x_loc=473, y_loc=602, node_colour=Colours['blue'], serial="n8")
    draft_graph.add_node(x_loc=244, y_loc=659, node_colour=Colours['red'], serial="n9")
    draft_graph.add_node(x_loc=431, y_loc=1003, node_colour=Colours['red'], serial="n10")
    draft_graph.add_node(x_loc=743, y_loc=603, node_colour=Colours['blue'], serial="n11")
    draft_graph.add_node(x_loc=854, y_loc=406, node_colour=Colours['red'], serial="n12")

    # draft_graph.add_node(x_loc=25, y_loc=910, node_colour=Colours['yellow'], serial="n12")
    # draft_graph.add_node(x_loc=212, y_loc=940, node_colour=Colours['blue'], serial="n13")
    # draft_graph.add_node(x_loc=82, y_loc=1780, node_colour=Colours['blue'], serial="n15")
    draft_graph.center_node = "n1"

    for node in draft_graph.node_list:
        draft_graph.get_possible_connections(node.serial_num)
    print ("4")
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n1"), draft_graph.get_node_by_serial("n2"))
    print ("5")
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n4"))
    print ("5.4")
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n3"), draft_graph.get_node_by_serial("n5"))
    print ("5.7")

    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n6"), draft_graph.get_node_by_serial("n7"))
    print ("6")
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n9"))
    print ("7")
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n10"))
    print ("8")
    draft_graph.connect_nodes(draft_graph.get_node_by_serial("n12"), draft_graph.get_node_by_serial("n11"))


    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n10"), draft_graph.get_node_by_serial("n11"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n11"), draft_graph.get_node_by_serial("n12"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n11"), draft_graph.get_node_by_serial("n13"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n8"), draft_graph.get_node_by_serial("n14"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n7"), draft_graph.get_node_by_serial("n8"))
    # draft_graph.connect_nodes(draft_graph.get_node_by_serial("n2"), draft_graph.get_node_by_serial("n15"))

    save_graph(draft_graph, "draft_graph_2.xml")

# create_draft_graph_2()

