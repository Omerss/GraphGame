import logging
import threading
import os

from GameData.GameDataHandler import GameDataHandler
from SupplementaryFiles.CreateRandGraph import create_rand_graph
from SupplementaryFiles import Utils
from SupplementaryFiles.LoadGraph import load_graph_from_file
from kivyFiles.GraphTabletGame import GraphTabletGame

CONFIG_FILE_PATH = "./config.ini"


class GameHandler:

    stop_threads = False

    def __init__(self):
        self.config = Utils.read_config_file(CONFIG_FILE_PATH)
        self.current_graph = None
        self.current_data_handler = None
        self.display = None

        self.current_step_count = 0
        self.button_event = threading.Event()
        Utils.image_folder = "{}\\{}".format(os.getcwd(), self.config['Default']['image_folder'])
        self.max_turns = int(self.config['Default']['max_turns'])
        self.current_turn = 0
        self.stop_threads = False

    def run_single_game(self, graph, graph_config):
        """
        Does a single run of a game - 3 stages:
        Graph learning - the main game section.
        Questionnaire - A list of questions about the graph
        Results - The result screen and summary of the data.
        :param graph: A path to a graph xml. The graph object also contains data about the questions
        :param graph_config: A graph config file containing basic structure data about the graph. Number of nodes etc.

        """
        logging.info("Setting up a single game")
        if graph is None:
            self.current_graph = create_rand_graph(graph_config)
        else:
            self.current_graph = load_graph_from_file(graph)
        self.current_data_handler = GameDataHandler(graph_config)
        self.current_turn = 0


        # Stage 1 - Run game
        self.current_step_count = 0
        # Register event
        click_thread = threading.Thread(name='block',
                                        target=self.event_pressed_button,
                                        args=(self.button_event,))
        click_thread.start()
        #dispatcher.connect(self.event_press_button, signal=SIG_BUTTON_PRESS, sender=dispatcher.Any)

        logging.info("Starting main kivy thread")
        display_thread = threading.Thread(name="Kivy display thread", target=self.kivy_thread, args=([], self.button_event))
        display_thread.start()

        while True:
            if self.current_turn == self.max_turns:
                logging.info("Finished running stage 1")
                self.stop_threads = True
                break
        self.display.stop()
        display_thread.join()
        click_thread.join()

        # Stage 2 - Questionnaire
        logging.info("Starting Questionnaire")

        # Stage 3 - Results screen
        logging.info("Starting Result Screen")

        print("end")

    def kivy_thread(self, *args):
        print(threading.currentThread().getName(), 'Starting')
        self.display = GraphTabletGame(self.current_graph, args[0], args[1])
        while True:
            self.display.run()
            if self.stop_threads:
                break

    def event_pressed_button(self, button_event):
        """Wait for the event to be set before doing anything"""
        while True:
            logging.debug('wait_for_event starting')
            button_clicked = button_event.wait()
            logging.debug('event set: %s', button_clicked)
            data = self.read_data_from_window
            print("do something with the data")
            button_event.clear()
            self.current_turn = self.current_turn + 1
            if self.stop_threads:
                break

    def read_data_from_window(self):
        """
        Gets data from the kivy game. Data = {'nodes': [NodeObject list]. 'edges':[(NodeObject, NodeObject)]}
        In edges, if NodeObject has serial = None
        :return:
        """
        node_list = []
        return node_list

