import questionsAnswering
from SupplementaryFiles import Utils
from SupplementaryFiles.Enums import Colours, QuestionTypes


class QuestionObject:
    """
    An object used for the questions displaying
    """
    question_string = None
    open_question = False
    user_answer = -1
    question_type_number = 0
    list_of_possible_answers = None
    args = None

    def __init__(self, question_string, question_type_number, question_id):
        self.question_string = question_string
        self.question_type_number = question_type_number
        self.get_question_values()
        self.question_id = question_id

    def get_question_values(self):
        if self.question_type_number == QuestionTypes.NUMBER:
            self.open_question = True

        elif self.question_type_number == QuestionTypes.MULTIPLE_CHOICE:
            self.open_question = False
            self.list_of_possible_answers = []
            for colour in Utils.get_enum_items(Colours):
                self.list_of_possible_answers.append(colour)

        elif self.question_type_number == QuestionTypes.BOOLEAN:
            self.open_question = False
            self.list_of_possible_answers = []
            self.list_of_possible_answers.append(True)
            self.list_of_possible_answers.append(False)

    def get_question_string(self):
        return self.question_string

    def is_open_question(self):
        return self.open_question

    def get_list_of_possible_answers(self):
        return self.list_of_possible_answers

    def set_user_answer(self, answer):
        self.user_answer = answer

    def get_question_number(self):
        return self.question_number

    def get_question_arguments(self):
        return self.args