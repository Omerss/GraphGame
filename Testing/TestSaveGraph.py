import unittest
from kivyFiles.GraphTabletGame import GraphTabletGame
from SupplementaryFiles.Enums import Colours
from SupplementaryFiles.GraphObj import GraphObject
from SupplementaryFiles.SaveGraph import save_graph
from SupplementaryFiles.LoadGraph import load_graph_from_file
import threading
class TestSaveGraph(unittest.TestCase):
    def test_save_and_load_graph(self):
        # Arrange
        max_neighbors = 5
        extra_distance = 1

        new_graph = GraphObject(max_x=1000, max_y=1000, node_count=10 , max_neighbors=max_neighbors,
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

        new_graph.connect_nodes (new_graph.node_list[0],new_graph.node_list[1])
        new_graph.connect_nodes (new_graph.node_list[2],new_graph.node_list[3])
        new_graph.connect_nodes (new_graph.node_list[4],new_graph.node_list[5])
        new_graph.connect_nodes (new_graph.node_list[6],new_graph.node_list[7])
        new_graph.connect_nodes (new_graph.node_list[8],new_graph.node_list[9])
        new_graph.connect_nodes (new_graph.node_list[9],new_graph.node_list[0])
        new_graph.connect_nodes (new_graph.node_list[0],new_graph.node_list[3])
        new_graph.connect_nodes (new_graph.node_list[4],new_graph.node_list[8])
        new_graph.connect_nodes (new_graph.node_list[2],new_graph.node_list[5])
        new_graph.connect_nodes (new_graph.node_list[7],new_graph.node_list[3])
        new_graph.connect_nodes (new_graph.node_list[3],new_graph.node_list[1])
        # Act
        save_graph(new_graph, "testSavingGraph2.xml")
        new_loaded_graph = load_graph_from_file("testSavingGraph2.xml")

        #assert
       # button_event = threading.Event()

        #display = GraphTabletGame([],new_graph , button_event)

    #    display.build()
        size = 0
        neighbors = set()
        possible_neighbors = set()
        real = True
        colour = Colours['red']

        self.assertEqual(new_loaded_graph.line_colour, Colours['red'])
        self.assertEqual(new_loaded_graph.size['max_x'],1000)
        self.assertEqual(new_loaded_graph.size['max_y'],1000)
        self.assertEqual(new_loaded_graph.node_count,10 )
        self.assertEqual(new_loaded_graph.max_neighbors, 5)
        self.assertEqual(new_loaded_graph.extra_distance,1)

        self.assertEqual(new_loaded_graph.connections[0], (min(new_loaded_graph.node_list[0].serial_num, new_loaded_graph.node_list[1].serial_num), max(new_loaded_graph.node_list[0].serial_num, new_loaded_graph.node_list[1].serial_num)))
        self.assertEqual(new_loaded_graph.connections[1], (min(new_loaded_graph.node_list[2].serial_num, new_loaded_graph.node_list[3].serial_num), max(new_loaded_graph.node_list[2].serial_num, new_loaded_graph.node_list[3].serial_num)))
        self.assertEqual(new_loaded_graph.connections[2], (min(new_loaded_graph.node_list[4].serial_num, new_loaded_graph.node_list[5].serial_num), max(new_loaded_graph.node_list[4].serial_num, new_loaded_graph.node_list[5].serial_num)))
        self.assertEqual(new_loaded_graph.connections[3], (min(new_loaded_graph.node_list[6].serial_num, new_loaded_graph.node_list[7].serial_num), max(new_loaded_graph.node_list[6].serial_num, new_loaded_graph.node_list[7].serial_num)))

        self.assertEqual(new_loaded_graph.node_list[0].serial_num, new_graph.node_list[0].serial_num)
        self.assertEqual(new_loaded_graph.node_list[0].size, 50)
        self.assertEqual(new_loaded_graph.node_list[0].colour, Colours['yellow'])
        print (new_graph.node_list[0].x==150)

        self.assertEqual(new_loaded_graph.node_list[0].x,150)
        self.assertEqual(new_loaded_graph.node_list[0].y, 100)
        self.assertEqual(new_loaded_graph.node_list[1].serial_num, new_graph.node_list[1].serial_num)
        self.assertEqual(new_loaded_graph.node_list[1].size, 50)
        self.assertEqual(new_loaded_graph.node_list[1].colour, Colours['red'])
        self.assertEqual(new_loaded_graph.node_list[1].x, 100)
        self.assertEqual(new_loaded_graph.node_list[1].y, 800)
        self.assertEqual(new_loaded_graph.node_list[2].serial_num, new_graph.node_list[2].serial_num)
        self.assertEqual(new_loaded_graph.node_list[2].size, 50)
        self.assertEqual(new_loaded_graph.node_list[2].colour, Colours['blue'])
        self.assertEqual(new_loaded_graph.node_list[2].x, 150)
        self.assertEqual(new_loaded_graph.node_list[2].y, 500)