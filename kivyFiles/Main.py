import kivy
kivy.require('1.9.1')

from CreateRandGraph import create_rand_graph
from GraphTabletGame import GraphTabletGame

if __name__ == "__main__":
    game = GraphTabletGame(create_rand_graph("../config.ini"),None,None)
    game.run()