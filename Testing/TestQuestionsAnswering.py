import unittest

from SupplementaryFiles.GraphObj import GraphObject
from kivyFiles.GraphTabletGame import GraphTabletGame
from SupplementaryFiles.Enums import Colours
from SupplementaryFiles.GraphObj import GraphObject
from SupplementaryFiles.SaveGraph import save_graph
from SupplementaryFiles.LoadGraph import load_graph_from_file
from Questions import QuestionsAnswers
import unittest
import threading

class TestGraph(unittest.TestCase):
    # how many nodes of color X are there?
    def test_question_one(self):
       print ("1")
       # Arrange
       max_neighbors = 5
       extra_distance = 1

       new_graph = GraphObject(max_x=1000, max_y=1000, node_count=10, max_neighbors=max_neighbors,
                               extra_distance=extra_distance)
       new_graph.add_node(150, 100, node_colour=Colours['yellow'])
       new_graph.add_node(100, 800, node_colour=Colours['red'])
       new_graph.add_node(150, 500, node_colour=Colours['blue'])
       new_graph.add_node(150, 300, node_colour=Colours['blue'])
       new_graph.add_node(550, 100, node_colour=Colours['red'])
       new_graph.add_node(450, 500, node_colour=Colours['yellow'])
       new_graph.add_node(350, 600, node_colour=Colours['yellow'])
       new_graph.add_node(250, 700, node_colour=Colours['red'])
       new_graph.add_node(150, 800, node_colour=Colours['blue'])
       new_graph.add_node(50, 900, node_colour=Colours['blue'])


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
       answer_color_red = QuestionsAnswers.question_one(new_graph, Colours['red'])
       answer_color_blue = QuestionsAnswers.question_one(new_graph, Colours['blue'])
       answer_color_yellow = QuestionsAnswers.question_one(new_graph, Colours['yellow'])
    #   print (answer_color_blue)
       #assert
       self.assertEqual(answer_color_blue, 4)
       self.assertEqual(answer_color_red, 3)
       self.assertEqual(answer_color_yellow, 3)


       # Act question 2
       ## how many nodes of color X have links to nodes of color Y?

       answer_color_red_red = QuestionsAnswers.question_two(new_graph, Colours['red'], Colours['red'])
       answer_color_blue_red = QuestionsAnswers.question_two(new_graph, Colours['red'], Colours['blue'])
       answer_color_yellow_red = QuestionsAnswers.question_two(new_graph, Colours['yellow'], Colours['red'])
       answer_color_blue_yellow = QuestionsAnswers.question_two(new_graph, Colours['blue'], Colours['yellow'])
       answer_color_blue_blue = QuestionsAnswers.question_two(new_graph, Colours['blue'], Colours['blue'])
       answer_color_yellow_yellow = QuestionsAnswers.question_two(new_graph, Colours['yellow'], Colours['yellow'])

       self.assertEqual(answer_color_red_red, 0)
       self.assertEqual(answer_color_blue_red, 3)
       self.assertEqual(answer_color_yellow_red, 3)
       self.assertEqual(answer_color_blue_yellow, 3)
       self.assertEqual(answer_color_blue_blue, 4)
       self.assertEqual(answer_color_yellow_yellow, 0)



       # Act question 3
       ## what is the color that contain the node with the maximun links in the graph?
       answer_max_3 = QuestionsAnswers.question_three(new_graph)
       self.assertEqual(answer_max_3, 'blue')

       # Act question 4
       # what is the color that contain the maximum sum of links in the graph?
       answer_max_4 = QuestionsAnswers.question_three(new_graph)
       self.assertEqual(answer_max_4, 'blue')

      # Act question 5
       # how many nodes of color X  do not have links to nodes of color Y?

       answer_color_red_red = QuestionsAnswers.question_five(new_graph, Colours['red'], Colours['red'])
       answer_color_red_blue = QuestionsAnswers.question_five(new_graph, Colours['red'], Colours['blue'])
       answer_color_yellow_red = QuestionsAnswers.question_five(new_graph, Colours['yellow'], Colours['red'])
       answer_color_blue_yellow = QuestionsAnswers.question_five(new_graph, Colours['blue'], Colours['yellow'])
       answer_color_blue_blue = QuestionsAnswers.question_five(new_graph, Colours['blue'], Colours['blue'])
       answer_color_yellow_yellow = QuestionsAnswers.question_five(new_graph, Colours['yellow'], Colours['yellow'])

       self.assertEqual(answer_color_red_red, 3)
       self.assertEqual(answer_color_red_blue, 0)
       self.assertEqual(answer_color_yellow_red, 0)
       self.assertEqual(answer_color_blue_yellow, 1)
       self.assertEqual(answer_color_blue_blue, 0)
       self.assertEqual(answer_color_yellow_yellow, 3)


       # Act question 6
       # what is the color that contain the node with the minimum links in the graph?

       answer_min_6 = QuestionsAnswers.question_six(new_graph)

       self.assertEqual(answer_min_6, 'yellow')


      # Act question 7
       # what is the color that contain the minimum sum of links in the graph?
       answer_min_7 = QuestionsAnswers.question_seven(new_graph)

       self.assertEqual(answer_min_7, 'yellow')

       # Act question 8
       # is there a nodes of color X that have a link to another node of color X?

       answer_color_red = QuestionsAnswers.question_eight(new_graph, Colours['red'])
       answer_color_blue = QuestionsAnswers.question_eight(new_graph, Colours['blue'])
       answer_color_yellow = QuestionsAnswers.question_eight(new_graph, Colours['yellow'])

       #assert
       self.assertEqual(answer_color_blue, True)
       self.assertEqual(answer_color_red, False)
       self.assertEqual(answer_color_yellow, False)


       # Act question 9
       # does every node at color X have link to a node of color Y?

       answer_color_red_red = QuestionsAnswers.question_nine(new_graph, Colours['red'], Colours['red'])
       answer_color_red_blue = QuestionsAnswers.question_nine(new_graph, Colours['red'], Colours['blue'])
       answer_color_yellow_red = QuestionsAnswers.question_nine(new_graph, Colours['yellow'], Colours['red'])
       answer_color_blue_yellow = QuestionsAnswers.question_nine(new_graph, Colours['blue'], Colours['yellow'])
       answer_color_blue_blue = QuestionsAnswers.question_nine(new_graph, Colours['blue'], Colours['blue'])
       answer_color_yellow_yellow = QuestionsAnswers.question_nine(new_graph, Colours['yellow'], Colours['yellow'])

       self.assertEqual(answer_color_red_red, False)
       self.assertEqual(answer_color_red_blue, True)
       self.assertEqual(answer_color_yellow_red, True)
       self.assertEqual(answer_color_blue_yellow, False)
       self.assertEqual(answer_color_blue_blue, True)
       self.assertEqual(answer_color_yellow_yellow, False)


       # Act question 10
       # is there more nodes of color X than nodes of color Y?


       answer_color_red_red = QuestionsAnswers.question_ten(new_graph, Colours['red'], Colours['red'])
       answer_color_red_blue = QuestionsAnswers.question_ten(new_graph, Colours['red'], Colours['blue'])
       answer_color_yellow_red = QuestionsAnswers.question_ten(new_graph, Colours['yellow'], Colours['red'])
       answer_color_blue_yellow = QuestionsAnswers.question_ten(new_graph, Colours['blue'], Colours['yellow'])
       answer_color_blue_blue = QuestionsAnswers.question_ten(new_graph, Colours['blue'], Colours['blue'])
       answer_color_yellow_yellow = QuestionsAnswers.question_ten(new_graph, Colours['yellow'], Colours['yellow'])

       self.assertEqual(answer_color_red_red, False)
       self.assertEqual(answer_color_red_blue, False)
       self.assertEqual(answer_color_yellow_red, False)
       self.assertEqual(answer_color_blue_yellow, True)
       self.assertEqual(answer_color_blue_blue, False)
       self.assertEqual(answer_color_yellow_yellow, False)

       # Act question 11
       # is there a nodes of color X that have at least Number link to another node of color X?

       answer_color_red = QuestionsAnswers.question_eleven(new_graph, Colours['red'], 1)
       answer_color_blue = QuestionsAnswers.question_eleven(new_graph, Colours['blue'])
       answer_color_yellow = QuestionsAnswers.question_eleven(new_graph, Colours['yellow'], 3)

       #assert
       self.assertEqual(answer_color_blue, False)
       self.assertEqual(answer_color_red, False)
       self.assertEqual(answer_color_yellow, False)

       # Act question 12
       # is there a node of color X with odd (flag =1)/ even (flag=0) number of links?

       answer_color_red = QuestionsAnswers.question_twelve(new_graph, Colours['red'], 1)
       answer_color_blue = QuestionsAnswers.question_twelve(new_graph, Colours['blue'], 1)
       answer_color_yellow = QuestionsAnswers.question_twelve(new_graph, Colours['yellow'], 0)

       #assert
       self.assertEqual(answer_color_red, False)
       self.assertEqual(answer_color_blue, False)
       self.assertEqual(answer_color_yellow, True)

       # Act question 13
       # does all the color X nodes have odd (flag =1)/ even (flag=0) number of links?

       answer_color_red = QuestionsAnswers.question_thirteen(new_graph, Colours['red'], 1)
       answer_color_blue = QuestionsAnswers.question_thirteen(new_graph, Colours['blue'], 0)
       answer_color_yellow = QuestionsAnswers.question_thirteen(new_graph, Colours['yellow'], 1)

       #assert
       self.assertEqual(answer_color_red, False)
       self.assertEqual(answer_color_blue, True)
       self.assertEqual(answer_color_yellow, False)

       # Act question 14
       #does the sum of the links in all the nodes at color X is odd (flag =1)/ even (flag=0)?

       answer_color_red = QuestionsAnswers.question_fourteen(new_graph, Colours['red'], 0)
       answer_color_blue = QuestionsAnswers.question_fourteen(new_graph, Colours['blue'], 1)
       answer_color_yellow = QuestionsAnswers.question_fourteen(new_graph, Colours['yellow'], 0)

       #assert
       self.assertEqual(answer_color_red, True)
       self.assertEqual(answer_color_blue, False)
       self.assertEqual(answer_color_yellow, True)

       # Act question 15
       #does the number of nodes at color X is odd (flag =1)/ even (flag=0)?
       answer_color_red = QuestionsAnswers.question_fifteen(new_graph, Colours['red'], 0)
       answer_color_blue = QuestionsAnswers.question_fifteen(new_graph, Colours['blue'], 1)
       answer_color_yellow = QuestionsAnswers.question_fifteen(new_graph, Colours['yellow'], 0)

       #assert
       self.assertEqual(answer_color_red, False)
       self.assertEqual(answer_color_blue, False)
       self.assertEqual(answer_color_yellow, False)

       # Act question 16
       # which color has the maximum number of nodes?
       answer_max_16 = QuestionsAnswers.question_sixteen(new_graph)
       self.assertEqual(answer_max_16, 'blue')


       # Act question 17
       # which color has the minimum number of nodes?
       answer_min_17 = QuestionsAnswers.question_seventeen(new_graph)
       self.assertEqual(answer_min_17, 'yellow')