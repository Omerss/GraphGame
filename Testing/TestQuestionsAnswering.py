import unittest

from SupplementaryFiles.GraphObj import GraphObject
from kivyFiles.GraphTabletGame import GraphTabletGame
from SupplementaryFiles.Enums import Colours
from SupplementaryFiles.GraphObj import GraphObject
from SupplementaryFiles.SaveGraph import save_graph
from SupplementaryFiles.LoadGraph import load_graph_from_file
from Questions import questionsAnswering
import unittest
import threading

class TestGraph(unittest.TestCase):
    # how many nodes of color X are there?
    def test_question_one(self):
       # Arrange
       max_neighbors = 5
       extra_distance = 1

       new_graph = GraphObject(max_x=1000, max_y=1000, node_count=10, max_neighbors=max_neighbors,
                               extra_distance=extra_distance)
       new_graph.add_node(150, 100, node_colour=Colours.yellow)
       new_graph.add_node(100, 800, node_colour=Colours.red)
       new_graph.add_node(150, 500, node_colour=Colours.blue)
       new_graph.add_node(150, 300, node_colour=Colours.blue)
       new_graph.add_node(550, 100, node_colour=Colours.red)
       new_graph.add_node(450, 500, node_colour=Colours.yellow)
       new_graph.add_node(350, 600, node_colour=Colours.yellow)
       new_graph.add_node(250, 700, node_colour=Colours.red)
       new_graph.add_node(150, 800, node_colour=Colours.blue)
       new_graph.add_node(50, 900, node_colour=Colours.blue)


       for node in new_graph.node_list:
           new_graph.get_possible_connections(node.serial_num)

       new_graph.connect_nodes(new_graph.node_list[0], new_graph.node_list[1])
       new_graph.connect_nodes(new_graph.node_list[2], new_graph.node_list[3])
       new_graph.connect_nodes(new_graph.node_list[4], new_graph.node_list[5])
       new_graph.connect_nodes(new_graph.node_list[6], new_graph.node_list[7])
       new_graph.connect_nodes(new_graph.node_list[8], new_graph.node_list[9])
       new_graph.connect_nodes(new_graph.node_list[9], new_graph.node_list[0])
       new_graph.connect_nodes(new_graph.node_list[0], new_graph.node_list[3])
       new_graph.connect_nodes(new_graph.node_list[4], new_graph.node_list[8])
       new_graph.connect_nodes(new_graph.node_list[2], new_graph.node_list[5])
       new_graph.connect_nodes(new_graph.node_list[7], new_graph.node_list[3])
       new_graph.connect_nodes(new_graph.node_list[1], new_graph.node_list[3])



       #save_graph(new_graph, "testSavingGraph2.xml")
       #new_loaded_graph = load_graph_from_file("testSavingGraph2.xml")

        #Act question 1
       # how many nodes of color X there is?
       answer_color_red = questionsAnswering.question_one(new_graph, Colours.red)
       answer_color_blue = questionsAnswering.question_one(new_graph, Colours.blue)
       answer_color_yellow = questionsAnswering.question_one(new_graph, Colours.yellow)
    #   print (answer_color_blue)
       #assert
       self.assertEqual(answer_color_blue, 4)
       self.assertEqual(answer_color_red, 3)
       self.assertEqual(answer_color_yellow, 3)


       # Act question 2
       ## how many nodes of color X have links to nodes of color Y?

       answer_color_red_red = questionsAnswering.question_two(new_graph, Colours.red,  Colours.red)
       answer_color_blue_red = questionsAnswering.question_two(new_graph, Colours.red, Colours.blue)
       answer_color_yellow_red = questionsAnswering.question_two(new_graph, Colours.yellow,  Colours.red)
       answer_color_blue_yellow = questionsAnswering.question_two(new_graph, Colours.blue, Colours.yellow)
       answer_color_blue_blue = questionsAnswering.question_two(new_graph, Colours.blue, Colours.blue)
       answer_color_yellow_yellow = questionsAnswering.question_two(new_graph, Colours.yellow, Colours.yellow)
       self.assertEqual(answer_color_red_red, 0)
       self.assertEqual(answer_color_blue_red, 3)
       self.assertEqual(answer_color_yellow_red, 3)
       self.assertEqual(answer_color_blue_yellow, 3)
       self.assertEqual(answer_color_blue_blue, 4)
       self.assertEqual(answer_color_yellow_yellow, 0)



       # Act question 3
       ## what is the color that contain the node with the maximun links in the graph?
       answer_max_3 = questionsAnswering.question_three(new_graph)
       self.assertEqual(answer_max_3, 'blue')

       # Act question 4
       # what is the color that contain the maximum sum of links in the graph?
       answer_max_4 = questionsAnswering.question_three(new_graph)
       self.assertEqual(answer_max_4, 'blue')

      # Act question 5
       # how many nodes of color X  do not have links to nodes of color Y?
