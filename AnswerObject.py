import questionsAnswering
from Enums import Colours
class AnswerObj():

    question_number = 0
    args = []
    result = ""
    graph = None
    question_function = None

    def __init__(self, graph, question_number, *args):
        self.question_number = question_number
        self.graph = graph
        self.args = args

    def get_question_result (self):
        if (self.quetion_number== 1):
            self.question_function = questionsAnswering.question_one
            self.result = self.question_function(self.graph, self.args[0])
            return self.result
        if (self.quetion_number== 2):
            self.question_function = questionsAnswering.question_two
            self.result = self.question_function(self.graph, self.args[0], self.args[1])
            return self.result

        if (self.quetion_number== 3):
            self.question_function = questionsAnswering.question_three
            self.result = self.question_function(self.graph)
            return self.result

        if (self.quetion_number== 4):
            self.question_function = questionsAnswering.question_four
            self.result = self.question_function(self.graph)
            return self.result

        if (self.quetion_number== 5):
            self.question_function = questionsAnswering.question_five
            self.result = self.question_function(self.graph, self.args[0], self.args[1])
            return self.result

        if (self.quetion_number== 6):
            self.question_function = questionsAnswering.question_six
            self.result = self.question_function(self.graph)
            return self.result

        if (self.quetion_number== 7):
            self.question_function = questionsAnswering.question_seven
            self.result = self.question_function(self.graph)
            return self.result

        if (self.quetion_number == 8):
            self.question_function = questionsAnswering.question_eight
            self.result = self.question_function(self.graph, self.args[0])
            return self.result

        if (self.quetion_number == 9):
            self.question_function = questionsAnswering.question_nine
            self.result = self.question_function(self.graph, self.args[0], self.args[1])
            return self.result

        if (self.quetion_number == 10):
            self.question_function = questionsAnswering.question_ten
            self.result = self.question_function(self.graph, self.args[0], self.args[1])
            return self.result

        if (self.quetion_number == 11):
            self.question_function = questionsAnswering.question_eleven
            self.result = self.question_function(self.graph, self.args[0], self.args[1])
            return self.result

        if (self.quetion_number == 12):
            self.question_function = questionsAnswering.question_twelve
            self.result = self.question_function(self.graph, self.args[0], self.args[1])
            return self.result

        if (self.quetion_number == 13):
            self.question_function = questionsAnswering.question_thirteen
            self.result = self.question_function(self.graph, self.args[0], self.args[1])
            return self.result

        if (self.quetion_number == 14):
            self.question_function = questionsAnswering.question_fourteen
            self.result = self.question_function(self.graph, self.args[0], self.args[1])
            return self.result

        if (self.quetion_number == 15):
            self.question_function = questionsAnswering.question_fifteen
            self.result = self.question_function(self.graph, self.args[0], self.args[1])
            return self.result

        if (self.quetion_number == 16):
            self.question_function = questionsAnswering.question_sixteen
            self.result = self.question_function(self.graph)
            return self.result

        if (self.quetion_number == 17):
            self.question_function = questionsAnswering.question_seventeen
            self.result = self.question_function(self.graph)
            return self.result
