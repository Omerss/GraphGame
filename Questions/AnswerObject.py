import questionsAnswering
from Enums import Colours
class AnswerObj():

    question_number = 0
    args = []
    user_seen_graph = None
    real_graph = None
    question_function = None
    user_answer = ""
    user_graph_answer = ""
    real_answer = ""
    def __init__(self, user_seen_graph, real_graph, user_answer, question_number, *args):
        self.question_number = question_number
        self.user_seen_graph = user_seen_graph
        self.real_graph = real_graph
        self.user_answer = user_answer
        self.args = args

    def get_question_results (self):
        if (self.quetion_number== 1):
            self.question_function = questionsAnswering.question_one
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0])
            self.real_answer = self.question_function(self.real_graph, self.args[0])
            return [self.user_answer, self.user_graph_answer, self.real_answer]
        if (self.quetion_number== 2):
            self.question_function = questionsAnswering.question_two
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0], self.args[1])
            self.real_answer = self.question_function(self.real_graph, self.args[0], self.args[1])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.quetion_number== 3):
            self.question_function = questionsAnswering.question_three
            self.user_graph_answer = self.question_function(self.user_seen_graph)
            self.real_answer = self.question_function(self.real_graph)
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.quetion_number== 4):
            self.question_function = questionsAnswering.question_four
            self.user_graph_answer = self.question_function(self.user_seen_graph)
            self.real_answer = self.question_function(self.real_graph)
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.quetion_number== 5):
            self.question_function = questionsAnswering.question_five
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0], self.args[1])
            self.real_answer = self.question_function(self.real_graph, self.args[0], self.args[1])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.quetion_number== 6):
            self.question_function = questionsAnswering.question_six
            self.user_graph_answer = self.question_function(self.user_seen_graph)
            self.real_answer = self.question_function(self.real_graph)
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.quetion_number== 7):
            self.question_function = questionsAnswering.question_seven
            self.user_graph_answer = self.question_function(self.user_seen_graph)
            self.real_answer = self.question_function(self.real_graph)
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.quetion_number == 8):
            self.question_function = questionsAnswering.question_eight
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0])
            self.real_answer = self.question_function(self.real_graph, self.args[0])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.quetion_number == 9):
            self.question_function = questionsAnswering.question_nine
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0], self.args[1])
            self.real_answer = self.question_function(self.real_graph, self.args[0], self.args[1])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.quetion_number == 10):
            self.question_function = questionsAnswering.question_ten
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0], self.args[1])
            self.real_answer = self.question_function(self.real_graph, self.args[0], self.args[1])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.quetion_number == 11):
            self.question_function = questionsAnswering.question_eleven
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0], self.args[1])
            self.real_answer = self.question_function(self.real_graph, self.args[0], self.args[1])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.quetion_number == 12):
            self.question_function = questionsAnswering.question_twelve
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0], self.args[1])
            self.real_answer = self.question_function(self.real_graph, self.args[0], self.args[1])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.quetion_number == 13):
            self.question_function = questionsAnswering.question_thirteen
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0], self.args[1])
            self.real_answer = self.question_function(self.real_graph, self.args[0], self.args[1])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.quetion_number == 14):
            self.question_function = questionsAnswering.question_fourteen
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0], self.args[1])
            self.real_answer = self.question_function(self.real_graph, self.args[0], self.args[1])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.quetion_number == 15):
            self.question_function = questionsAnswering.question_fifteen
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0], self.args[1])
            self.real_answer = self.question_function(self.real_graph, self.args[0], self.args[1])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.quetion_number == 16):
            self.question_function = questionsAnswering.question_sixteen
            self.user_graph_answer = self.question_function(self.user_seen_graph)
            self.real_answer = self.question_function(self.real_graph)
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.quetion_number == 17):
            self.question_function = questionsAnswering.question_seventeen
            self.user_graph_answer = self.question_function(self.user_seen_graph)
            self.real_answer = self.question_function(self.real_graph)
            return [self.user_answer, self.user_graph_answer, self.real_answer]
