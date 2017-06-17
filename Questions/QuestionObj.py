import questionsAnswering
from SupplementaryFiles.Enums import Colours

#an object used for the questions displaying
class QuestionObject():
    question_string = None
    open_question = False
    user_answer = -1
    question_type_number = 0
    list_of_possible_answers = None
    args = None
# question_type_number - 1- open question, question_type_number-2 close question with answers derived from colors, question_type_number-3 yes/no question
    def __init__(self, question_string, question_type_number):
        self.question_string = question_string
        self.question_type_number = question_type_number
        self.get_question_values()

    def get_question_values(self):
        if (self.question_type_number== 1):
            self.open_question = True

        if (self.question_type_number == 2):
            self.open_question = False
            for color in Colours:
                self.list_of_possible_answers.append(color)

        if (self.question_type_number == 3 ):
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