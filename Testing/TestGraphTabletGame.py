from KivyFiles.GraphTabletGame import GraphTabletGame
import unittest

class TestGraphTabletGame(unittest.TestCase):

    def test_buttons(self):
        game = GraphTabletGame()
        game.build()
        game.layout.kivy_graph.print_graph_nodes()
        game.press_button(1)
        print "pressed button1 (move_up)"
        game.layout.kivy_graph.print_graph_nodes()
        game.press_button(2)
        print "pressed button2 (move_down)"
        game.layout.kivy_graph.print_graph_nodes()
        game.press_button(2)
        print "pressed button2 (move_down)"
        game.layout.kivy_graph.print_graph_nodes()
        game.press_button(3)
        print "pressed button3 (move_right)"
        game.layout.kivy_graph.print_graph_nodes()
        game.press_button(4)
        print "pressed button4 (move_left)"
        game.layout.kivy_graph.print_graph_nodes()
        game.press_button(4)
        print "pressed button4 (move_left)"
        game.layout.kivy_graph.print_graph_nodes()
        print "finished checking buttons"

    def test_screen_visibility(self):
        game = GraphTabletGame()
        game.build()
        nodes = game.get_onscreen_nodes()
        print nodes
        edges = game.get_onscreen_edges(nodes)
        print edges



