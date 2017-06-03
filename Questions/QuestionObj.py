import questionsAnswering
from SupplementaryFiles.Enums import Colours

class QuestionObject():
    question_string = ""
    open_question = False
    user_answer = -1
    question_number = 0
    list_of_possible_answers = None
    args = []
    def __init__(self, questsion_string, question_number, *args):
        self.question_string = questsion_string
        self.quetion_number = question_number
        self.args = args

    def get_question_values (self):
        if (self.quetion_number == 1):
            self.open_question = False

        if (self.quetion_number == 2):
            self.open_question = False

        if (self.quetion_number == 3):
            self.open_question = True
            for color in Colours:
                self.list_of_possible_answers.append (color)

        if (self.quetion_number == 4):
            self.open_question = True
            for color in Colours:
                self.list_of_possible_answers.append (color)

        if (self.quetion_number == 5):
            self.open_question = False

        if (self.quetion_number == 6):
            self.open_question = True
            for color in Colours:
                self.list_of_possible_answers.append (color)

        if (self.quetion_number == 7):
            self.open_question = True
            for color in Colours:
                self.list_of_possible_answers.append (color)

        if (self.quetion_number == 8):
            self.open_question = True
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

        if (self.quetion_number == 9):
            self.open_question = True
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

        if (self.quetion_number == 10):
            self.open_question = True
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

        if (self.quetion_number == 11):
            self.open_question = True
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

        if (self.quetion_number == 12):
            self.open_question = True
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

        if (self.quetion_number == 13):
            self.open_question = True
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

        if (self.quetion_number == 14):
            self.open_question = True
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

        if (self.quetion_number == 15):
            self.open_question = True
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

        if (self.quetion_number == 16):
            self.open_question = True
            for color in Colours:
                self.list_of_possible_answers.append (color)

        if (self.quetion_number == 17):
            self.open_question = True
            for color in Colours:
                self.list_of_possible_answers.append (color)

    def getQuestionString (self):
        return self.question_string

    def isOpenQuestion (self):
        return self.open_question

    def getListOfPossibleAnswers (self):
        return self.list_of_possible_answers

    def setUserAnswer (self,answer):
        self.user_answer = answer