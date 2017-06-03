import questionsAnswering
from SupplementaryFiles.Enums import Colours


class QuestionObject():
    question_string = None
    open_question = False
    user_answer = -1
    question_number = 0
    list_of_possible_answers = None
    args = None

    def __init__(self, question_string, question_number, *args):
        self.question_string = question_string
        self.question_number = question_number
        self.args = args

    def get_question_values(self):
        if (self.question_number == 1 or self.question_number == 2 or self.question_number == 5):
            self.open_question = True

        if (self.question_number == 3 or self.question_number == 4 or self.question_number == 6
            or self.question_number == 7 or self.question_number == 16 or self.question_number == 17):
            self.open_question = False
            for color in Colours:
                self.list_of_possible_answers.append(color)

        if (self.question_number == 8 or self.question_number == 9 or self.question_number == 10
            or self.question_number == 11 or self.question_number == 12 or self.question_number == 13
            or self.question_number == 14 or self.quetion__number == 15):
            self.open_question = False
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

    def getQuestionString (self):
        return self.question_string

    def isOpenQuestion (self):
        return self.open_question

    def getListOfPossibleAnswers (self):
        return self.list_of_possible_answers

    def setUserAnswer (self,answer):
        self.user_answer = answer

    def get_question_number (self):
        return self.question_number

    def get_question_arguments (self):
        return self.args