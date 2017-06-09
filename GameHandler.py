import threading
import os

import time
from structlog import get_logger
from GameData.GameDataHandler import GameDataHandler
from Questions.AnswerObj import AnswerObj
from Questions.QuestionObj import QuestionObject
from SupplementaryFiles.CreateRandGraph import create_rand_graph
from SupplementaryFiles import Utils
from SupplementaryFiles.LoadGraph import load_graph_from_file
from kivyFiles.GraphTabletGame import GraphTabletGame

CONFIG_FILE_PATH = "./config.ini"

def kivy_thread_graph_game(self, *args):
    print(threading.currentThread().getName(), 'Starting')
    self.display = GraphTabletGame(args[2], args[0], args[1])
    if args[3]:
        self.display.run()
    else:
        self.display.build()

class GameHandler:

    stop_threads = False
    real_user = True
    machine_signal = None

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
        self.log = get_logger()
        self.score = 0

    def run_single_game(self, graph_file_path, graph_config, real_user=True, machine_signal=None):
        """
        Does a single run of a game - 3 stages:
        Graph learning - the main game section.
        Questionnaire - A list of questions about the graph
        Results - The result screen and summary of the data.
        :param real_user: Bool
        :param graph_file_path: A path to a graph xml. The graph object also contains data about the questions
        :param graph_config: A graph config file containing basic structure data about the graph. Number of nodes etc.

        """
        self.real_user = real_user
        self.machine_signal = machine_signal
        self.log.info("Setting up a single game")
        if graph_file_path is None:
            self.current_graph = create_rand_graph(graph_config)
        else:
            self.current_graph = load_graph_from_file(graph_file_path)
        self.current_data_handler = GameDataHandler(graph_config)
        self.current_turn = 0
        self.stop_threads = False

        # Stage 1 - Run game
        self.log.info("Starting Stage 1 - Run game")
        self.current_step_count = 0
        # Register event
        if self.real_user:
            click_thread = threading.Thread(name='press_button_event',
                                            target=self.event_pressed_button,
                                            args=(self.button_event,)).start()

        self.log.info("Starting main kivy thread")
        display_thread = threading.Thread(name="Kivy display thread",
                                          target=self.kivy_thread_graph_game,
                                          args=([], self.button_event, self.current_graph, real_user)).start()
        time.sleep(5)
        self.current_data_handler.add_view_to_db(self.display.get_info_from_screen())
        if not self.real_user:
            # Pass signal to machine player to start pressing keys
            self.machine_signal.set()

        while True:
            if self.stop_threads:
                break

        # This is just trying to catch threads if they don't close.
        # Don't look too much into this as it's just trowing everything and hoping something sticks.
        if self.display is not None:
            self.log.debug("Try to join thread display")
            #self.display.stop()
            if display_thread is not None:
                display_thread.join(5)
        self.log.debug("Checking if threads did not close correctly")
        if display_thread is not None and display_thread.is_alive():
            raise Exception("Threads not closed - thread={}".format(display_thread.name))

        if self.real_user:
            click_thread.join(5)
            if click_thread is not None and click_thread.is_alive():
                raise Exception("Threads not closed - thread={}".format(click_thread.name))

            # Stage 2 - Questionnaire
            self.log.info("Starting Stage 2 - Questionnaire")

    #         # Stage 3 - Results scnreen
    #         self.log.info("Starting Stage 3 - Result Screen")
    #         # user_seen_graph_answers = set_answer_objects(userSeenGraph)
    #         # full_graph_answers = set_answer_objects(fullGraph)
    #
    #
    #         know_graph = self.current_data_handler.graph
            # Stage 3 - Results screen
    #         self.log.info("Starting Stage 3 - Result Screen")
    #         known_graph = self.current_data_handler.graph
    #         display_thread = threading.Thread(name="Kivy display thread",
    #                                           target=self.kivy_thread,
    #                                           args=([], self.button_event, known_graph)).start()
        else:
            # Machine user. Only get percentage score
            pass
        return self.score

    @staticmethod
    def set_answer_objects(graph, question_list):
        """

        :param question_list: question objects
        :return: 
        """
        answer_objects = []
        for question in question_list:
            question_number = question.get_question_number()
            question_arguments = question.get_question_arguments()
            answer_object = AnswerObj(graph, question_number, question_arguments)
            answer_objects.append(answer_object)
        return answer_objects

    def kivy_thread_graph_game(self, *args):
        print(threading.currentThread().getName(), 'Starting')
        self.display = GraphTabletGame(args[2], args[0], args[1])
        if args[3]:
            self.display.run()
        else:
            self.display.build()

    def event_pressed_button(self, button_event):
        """Wait for the event to be set before doing anything"""
        while True:

            self.log.debug("wait_for_event starting")
            button_clicked = button_event.wait()
            self.log.debug("event set.", new_event=button_clicked)
            self.log.info("Collecting data from display")
            self.display.set_button_status(False)
            data = self.display.get_info_from_screen()
            self.current_data_handler.add_view_to_db(data)
            # We clear the event so it could be called again. If we dont do this then calling the event again will not
            # actually do anything.
            button_event.clear()
            self.current_turn = self.current_turn + 1
            self.display.set_button_status(True)

            if self.current_turn == self.max_turns:
                self.stop_threads = True
                break

    def machine_press_button(self, button_num):
        self.display.press_button(button_num)
        self.current_turn = self.current_turn + 1
        data = self.display.get_info_from_screen()
        self.current_data_handler.add_view_to_db(data)
        if self.current_turn == self.max_turns:
            self.stop_threads = True
        self.machine_signal.set()

