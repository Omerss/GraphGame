from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.label import Label

from kivyFiles.GraphLayout import GraphLayout


class ResultDisplay(App):
    parent_screen = None

    def __init__(self, parent_screen=None):
        self.parent_screen = parent_screen
        self.the_widget = ResultWidget(self, self.parent_screen.main_app)

    def load(self):
        pass


class ResultWidget(GridLayout):
    question_list = None
    main_app = None
    parent_app = None

    def __init__(self, parent_app, main_app):
        super(ResultWidget, self).__init__(rows=3, cols=1)

        self.parent_app = parent_app
        self.main_app = main_app

        self.layout = GridLayout(rows=10, cols=2)
        self.layout.add_widget(self.get_question_result_grid(question_list=self.main_app.user_answers))

        map_grid = GridLayout(rows=2, cols=1)
        graph1 = GraphLayout(self.main_app.discovered_graph,
                             button_funcs=[],
                             signal=None,
                             button_lst=[],
                             dim={'max_x': 100, 'max_y': 100},
                             button_width=0)
        graph1.fit_graph_to_screen()
        map_grid.add_widget(graph1)
        graph2 = GraphLayout(self.main_app.true_graph,
                             button_funcs=[],
                             signal=None,
                             button_lst=[],
                             dim={'max_x': 100, 'max_y': 100},
                             button_width=0)
        graph2.fit_graph_to_screen()
        map_grid.add_widget(graph2)
        self.layout.add_widget(map_grid)

        self.add_widget(self.layout)
        res = self.calculate_percentage(self.main_app.user_answers)
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
        self.parent_app.end_results()

    @staticmethod
    def get_question_result_grid(question_list):
        question_result_grid = GridLayout(rows=len(question_list), cols=1)

        for item in question_list:
            new_question = GridLayout(rows=3, cols=1)
            new_question.add_widget(Label(text=item.question_string))

            keys = GridLayout(rows=1, cols=3)
            keys.add_widget(Label(text="User Answer"))
            keys.add_widget(Label(text="User Graph Answer"))
            keys.add_widget(Label(text="True Answer"))
            new_question.add_widget(keys)

            answers = GridLayout(rows=1, cols=3)
            answers.add_widget(Label(text=str(item.user_answer)))
            answers.add_widget(Label(text=str(item.user_graph_answer)))
            answers.add_widget(Label(text=str(item.real_answer)))
            new_question.add_widget(answers)

            question_result_grid.add_widget(new_question)

        return question_result_grid

    def calculate_percentage(self, answer_list):
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
        user_graph_num_of_nodes = len(user_seen_graph.node_list)
        real_graph_num_of_nodes = len(real_graph.node_list)
        return float(user_graph_num_of_nodes) / float(real_graph_num_of_nodes)

    def build(self):
        return self.meta_layout
