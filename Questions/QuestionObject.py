import questionsAnswering
from SupplementaryFiles import Utils
from SupplementaryFiles.Enums import Colours, QuestionTypes


class QuestionObject:
    """
    An object used for the questions displaying
    """

    def __init__(self, question_string, question_type_number, question_id, *args)\
            :
        self.question_string = question_string.format(*tuple([item['name'] for item in args]))
        self.question_type_number = question_type_number
        self.get_question_values()
        self.question_id = question_id
        self.args = args

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

