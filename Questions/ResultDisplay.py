from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.label import Label

from Questions.AnswerObject import AnswerObject
from kivyFiles.GraphLayout import GraphLayout


class ResultDisplay(App):
    parent_screen = None

    def __init__(self, parent_screen=None):
        self.parent_screen = parent_screen
        self.the_widget = ResultWidget(self, self.parent_screen.main_app)

    def load(self):
        self.the_widget.on_enter()


class ResultWidget(GridLayout):
    question_list = None
    main_app = None
    parent_app = None

    def __init__(self, parent_app, main_app):
        super(ResultWidget, self).__init__(rows=3, cols=1)

        self.parent_app = parent_app
        self.main_app = main_app

    def on_enter(self):
        self.layout = GridLayout(rows=10, cols=2)
        self.layout.add_widget(self.get_question_result_grid(main_app_data=self.main_app))

        map_grid = GridLayout(rows=2, cols=1)
        graph_discovered = GraphLayout(original_graph=self.main_app.discovered_graph,
                                       dim={'max_x': 100, 'max_y': 100},
                                       zoom_rate=0.5,
                                       edge_size=1)
        map_grid.add_widget(graph_discovered)
        graph_true = GraphLayout(self.main_app.true_graph,
                                 dim={'max_x': 100, 'max_y': 100},
                                 zoom_rate=0.5,
                                 edge_size=1)
        map_grid.add_widget(graph_true)
        self.layout.add_widget(map_grid)

        self.add_widget(self.layout)
        res = self.calculate_percentage(self.main_app)
        self.add_widget(Label(text="possible_success 1: {}; true_success 2: {}; discovery grade: {}"
                              .format(res['possible_success'],
                                      res['true_success'],
                                      self.game_grade(self.main_app.discovered_graph,
                                                      self.main_app.true_graph)),
                              size_hint_y=None, height=50))

        self.submit_button = Button(text='Done', size_hint_y=None, height=50)
        self.submit_button.bind(on_press=self.stop_me)
        self.add_widget(self.submit_button)

    def stop_me(self, instance):
        self.parent_app.parent_screen.end_results()

    @staticmethod
    def get_question_result_grid(main_app_data):

        current_graph = main_app_data.current_graph
        discovered_graph = main_app_data.discovered_graph
        graph_answers = [AnswerObject(item, discovered_graph, current_graph) for item in main_app_data.question_list]
        user_answers = main_app_data.user_answers

        question_result_grid = GridLayout(rows=len(graph_answers), cols=1)

        for item in graph_answers:
            new_question = GridLayout(rows=3, cols=1)
            new_question.add_widget(Label(text=item.question_string))

            keys = GridLayout(rows=1, cols=3)
            keys.add_widget(Label(text="User Answer"))
            keys.add_widget(Label(text="User Graph Answer"))
            keys.add_widget(Label(text="True Answer"))
            new_question.add_widget(keys)

            answers = GridLayout(rows=1, cols=3)
            answers.add_widget(Label(text=str(item.get_answer())))
            answers.add_widget(Label(text=str(item.get_answer())))
            answers.add_widget(Label(text=str(item.get_answer())))
            new_question.add_widget(answers)

            question_result_grid.add_widget(new_question)

        return question_result_grid


    def calculate_percentage(self, main_app):
        return {'possible_success': 1,
                'true_success': 0.5}
        answer_list = main_app.question_list
        user_answers_percentage = 0
        user_graph_answer_percentage = 0
        for answer in answer_list:
            answers_list = answer.get_question_results()
            if answers_list[0] == answers_list[1]:
                user_answers_percentage = user_answers_percentage + 1
            if answers_list[1] == answers_list[2]:
                user_graph_answer_percentage = user_graph_answer_percentage + 1
        num_of_questions = len(answer_list)
        user_possible_success = user_answers_percentage * 100 / float(num_of_questions)
        user_true_success = user_graph_answer_percentage * 100 / float(num_of_questions)
        return {'possible_success': user_possible_success, 'true_success': user_true_success}

    @staticmethod
    def game_grade(user_seen_graph, real_graph):
        return 4
        user_graph_num_of_nodes = len(user_seen_graph.node_list)
        real_graph_num_of_nodes = len(real_graph.node_list)
        return float(user_graph_num_of_nodes) / float(real_graph_num_of_nodes)

    def build(self):
        return self.meta_layout
