import questionsAnswering
from Enums import Colours

class QuestionObject():
    question_string= ""
    is_the_question_open = ""
    user_answer = ""
    question_number = ""
    list_of_possible_answers = None
    args = []
    def __init__(self, questsion_string, question_number, *args):
        self.question_string = question_string
        self.quetion_number = question_number
        self.args = args

    def get_question_values (self):
        if (self.quetion_number== 1):
            self.is_the_question_open = False

        if (self.quetion_number== 2):
            self.is_the_question_open = False

        if (self.quetion_number== 3):
            self.is_the_question_open = True
            for color in Colours:
                self.list_of_possible_answers.append (color)

        if (self.quetion_number== 4):
            self.is_the_question_open = True
            for color in Colours:
                self.list_of_possible_answers.append (color)

        if (self.quetion_number== 5):
            self.is_the_question_open = False

        if (self.quetion_number== 6):
            self.is_the_question_open = True
            for color in Colours:
                self.list_of_possible_answers.append (color)

        if (self.quetion_number== 7):
            self.is_the_question_open = True
            for color in Colours:
                self.list_of_possible_answers.append (color)

        if (self.quetion_number == 8):
            self.is_the_question_open = True
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

        if (self.quetion_number == 9):
            self.is_the_question_open = True
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

        if (self.quetion_number == 10):
            self.is_the_question_open = True
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

        if (self.quetion_number == 11):
            self.is_the_question_open = True
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

        if (self.quetion_number == 12):
            self.is_the_question_open = True
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

        if (self.quetion_number == 13):
            self.is_the_question_open = True
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

        if (self.quetion_number == 14):
            self.is_the_question_open = True
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

        if (self.quetion_number == 15):
            self.is_the_question_open = True
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

        if (self.quetion_number == 16):
            self.is_the_question_open = True
            for color in Colours:
                self.list_of_possible_answers.append (color)

        if (self.quetion_number == 17):
            self.is_the_question_open = True
            for color in Colours:
                self.list_of_possible_answers.append (color)
