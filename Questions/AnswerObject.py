import questionsAnswering


class AnswerObject:

    question_function = None
    user_answer = ""
    user_graph_answer = ""
    real_answer = ""

    def __init__(self, question_object, user_seen_graph, real_graph):
        self.question_id = question_object.question_data.question_id
        self.question_string = question_object.question_data.question_string
        self.user_answer = question_object.get_answer()
        self.args = question_object.question_data.args
        self.user_seen_graph = user_seen_graph
        self.real_graph = real_graph

        self.get_question_results()

    def get_question_results(self):
        if self.question_id == 1:
            self.question_function = questionsAnswering.question_one
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0])
            self.real_answer = self.question_function(self.real_graph, self.args[0])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if self.question_id == 2:
            self.question_function = questionsAnswering.question_two
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0], self.args[1])
            self.real_answer = self.question_function(self.real_graph, self.args[0], self.args[1])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if self.question_id == 3:
            self.question_function = questionsAnswering.question_three
            self.user_graph_answer = self.question_function(self.user_seen_graph)
            self.real_answer = self.question_function(self.real_graph)
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if self.question_id == 4:
            self.question_function = questionsAnswering.question_four
            self.user_graph_answer = self.question_function(self.user_seen_graph)
            self.real_answer = self.question_function(self.real_graph)
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.question_id== 5):
            self.question_function = questionsAnswering.question_five
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0], self.args[1])
            self.real_answer = self.question_function(self.real_graph, self.args[0], self.args[1])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.question_id== 6):
            self.question_function = questionsAnswering.question_six
            self.user_graph_answer = self.question_function(self.user_seen_graph)
            self.real_answer = self.question_function(self.real_graph)
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.question_id== 7):
            self.question_function = questionsAnswering.question_seven
            self.user_graph_answer = self.question_function(self.user_seen_graph)
            self.real_answer = self.question_function(self.real_graph)
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.question_id == 8):
            self.question_function = questionsAnswering.question_eight
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0])
            self.real_answer = self.question_function(self.real_graph, self.args[0])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.question_id == 9):
            self.question_function = questionsAnswering.question_nine
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0], self.args[1])
            self.real_answer = self.question_function(self.real_graph, self.args[0], self.args[1])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.question_id == 10):
            self.question_function = questionsAnswering.question_ten
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0], self.args[1])
            self.real_answer = self.question_function(self.real_graph, self.args[0], self.args[1])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.question_id == 11):
            self.question_function = questionsAnswering.question_eleven
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0], self.args[1])
            self.real_answer = self.question_function(self.real_graph, self.args[0], self.args[1])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.question_id == 12):
            self.question_function = questionsAnswering.question_twelve
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0], self.args[1])
            self.real_answer = self.question_function(self.real_graph, self.args[0], self.args[1])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.question_id == 13):
            self.question_function = questionsAnswering.question_thirteen
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0], self.args[1])
            self.real_answer = self.question_function(self.real_graph, self.args[0], self.args[1])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.question_id == 14):
            self.question_function = questionsAnswering.question_fourteen
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0], self.args[1])
            self.real_answer = self.question_function(self.real_graph, self.args[0], self.args[1])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.question_id == 15):
            self.question_function = questionsAnswering.question_fifteen
            self.user_graph_answer = self.question_function(self.user_seen_graph, self.args[0], self.args[1])
            self.real_answer = self.question_function(self.real_graph, self.args[0], self.args[1])
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.question_id == 16):
            self.question_function = questionsAnswering.question_sixteen
            self.user_graph_answer = self.question_function(self.user_seen_graph)
            self.real_answer = self.question_function(self.real_graph)
            return [self.user_answer, self.user_graph_answer, self.real_answer]

        if (self.question_id == 17):
            self.question_function = questionsAnswering.question_seventeen
            self.user_graph_answer = self.question_function(self.user_seen_graph)
            self.real_answer = self.question_function(self.real_graph)
            return [self.user_answer, self.user_graph_answer, self.real_answer]
