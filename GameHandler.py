import threading

import time

import logging
from pydispatch import dispatcher

from GameDataHandler import GameDataHandler
from SupplementaryFiles.LoadGraph import load_graph_from_file
from SupplementaryFiles.Utils import read_config_file
from kivyFiles.GraphTabletGame import GraphTabletGame

CONFIG_FILE_PATH = "./config.ini"
SIG_BUTTON_PRESS = 'A button has been pressed in kivy'


class GameHandler:

    def __init__(self):
        self.config = read_config_file(CONFIG_FILE_PATH)
        self.current_graph = None
        self.current_data_handler = None
        self.display = None

        self.current_step_count = 0
        self.button_event = threading.Event()

    def run_single_game(self, graph, graph_config):
        """
        Does a single run of a game - 3 stages:
        Graph learning - the main game section.
        Questionnaire - A list of questions about the graph
        Results - The result screen and summary of the data.
        :param graph: A path to a graph xml. The graph object also contains data about the questions
        :param graph_config: A graph config file containing basic structure data about the graph. Number of nodes etc.

        """
        self.current_graph = load_graph_from_file(graph)
        self.current_data_handler = GameDataHandler(graph_config)

        # Stage 1 - Run game
        self.current_step_count = 0
        # Register event
        click_thread = threading.Thread(name='block',
                                        target=self.event_pressed_button,
                                        args=self.button_event)
        click_thread.start()
        #dispatcher.connect(self.event_press_button, signal=SIG_BUTTON_PRESS, sender=dispatcher.Any)
        # Run kivy
        display_thread = threading.Thread(name="Kivy display thread", target=self.kivy_thread, args=([], self.button_event))
        display_thread.start()


    def kivy_thread(self, *args):
        print(threading.currentThread().getName(), 'Starting')
        self.display = GraphTabletGame(self.current_graph, args[0], args[1])

    def event_pressed_button(self, button_event):
        """Wait for the event to be set before doing anything"""
        logging.debug('wait_for_event starting')
        button_clicked = button_event.wait()
        logging.debug('event set: %s', button_clicked)
        data = self.read_data_from_window
        print("do something with the data")

    def read_data_from_window(self):
        """
        Gets data from the kivy game. Data = {'nodes': [NodeObject list]. 'edges':[(NodeObject, NodeObject)]}
        In edges, if NodeObject has serial = None
        :return:
        """
        node_list = []
        return node_list

