import threading
import os
import time
from Queue import Queue

from structlog import get_logger
from GameData.GameDataHandler import GameDataHandler
from Questions.AnswerObj import AnswerObj

from Questions.AnswerObject import AnswerObject
from Questions.QuestionObj import QuestionObject
from Questions.QuestionsDisplayObj import QuestionDisplay
from Questions.ResultDisplay import ResultDisplay
from SupplementaryFiles.CreateRandGraph import create_rand_graph
from SupplementaryFiles import Utils
from SupplementaryFiles.Enums import QuestionTypes
from SupplementaryFiles.LoadGraph import load_graph_from_file
from kivyFiles.GraphTabletGame import GraphTabletGame

from kivy.app import App

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
        self.max_turns = 1 # todo - remove this!
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
        self.display = GraphTabletGame(self.current_graph, [], self.button_event)

        if self.real_user:
            click_thread = threading.Thread(name='press_button_event',
                                            target=self.event_pressed_button,
                                            args=(self.button_event,)).start()

        self.log.info("Starting main kivy thread")

        self.display.build()
        time.sleep(3)
        self.current_data_handler.add_view_to_db(self.display.get_info_from_screen())
        if real_user:
            self.display.run()
        else:
            # Pass signal to machine player to start pressing keys
            self.machine_signal.set()

        if self.real_user:
            if click_thread is not None and click_thread.is_alive():
                click_thread.join(5)
                raise Exception("Threads not closed - thread={}".format(click_thread.name))

            # Stage 2 - Questionnaire
            self.log.info("Starting Stage 2 - Questionnaire")
            questions = self.create_questions()
            q = Queue()
            self.log.info("Starting Questionnaire kivy thread")
            self.display = QuestionDisplay(questions, q)
            self.display.run()
            user_answers = q.get()

            for item in user_answers:
                print("question #{} - {}".format(item.question_number, item.get_answer()))

            full_answers = []
            for item in user_answers:
                full_answers.append(AnswerObject(question_object=item,
                                                 user_seen_graph=self.current_data_handler.graph,
                                                 real_graph=self.current_graph))

            # Stage 3 - Results screen
            self.log.info("Starting Stage 3 - Result Screen")

            self.display = QuestionDisplay(questions, q)
            self.display.run()
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


    def kivy_thread_results(self):
        print(threading.currentThread().getName(), 'Starting')
        self.display = ResultDisplay()
        self.display.run()

    def kivy_thread_graph_game(self, **kwargs):
        print(threading.currentThread().getName(), 'Starting')
        self.display = GraphTabletGame(kwargs['graph'], kwargs['button_funcs'], kwargs['button_event'])
        if kwargs['real_user']:
            self.display.run()
        else:
            self.display.build()
        while not self.stop_threads:
            pass

    def event_pressed_button(self, button_event):
        """Wait for the event to be set before doing anything"""
        while True:

            self.log.debug("wait_for_event starting")
            button_clicked = button_event.wait()
            self.log.debug("event set", new_event=button_clicked)
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
                time.sleep(5)
                self.display.stop()
                break

    def machine_press_button(self, button_num):
        self.display.press_button(button_num)
        self.current_turn = self.current_turn + 1
        data = self.display.get_info_from_screen()
        self.current_data_handler.add_view_to_db(data)
        if self.current_turn == self.max_turns:
            self.stop_threads = True
        self.machine_signal.set()

    def create_questions(self):
        """
        Creates a list of QuestionObject
        """
        questionOne = QuestionObject("how many red nodes there are?", QuestionTypes.NUMBER, 111)
        questionThree = QuestionObject("what is the color that contain the node with the maximun links in the graph?",
                                       QuestionTypes.MULTIPLE_CHOICE, 222)
        questionFive = QuestionObject("how many red nodes do not have links blue nodes?", QuestionTypes.NUMBER, 4)
        questionNine = QuestionObject("does every node at color yellow have link to a node of color red?",
                                      QuestionTypes.BOOLEAN, 12)
        questionTen = QuestionObject("is there more red nodes than yellow nodes?", QuestionTypes.BOOLEAN, 14)

        question_list = [questionOne, questionThree, questionFive, questionNine, questionTen]

        return question_list

    def game_grade (self, user_seen_graph, real_graph):
        user_graph_num_of_nodes = len(user_seen_graph.node_list)
        real_graph_num_of_nodes = len(real_graph.node_list)
        return float(user_graph_num_of_nodes)/float(real_graph_num_of_nodes)