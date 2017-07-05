
from QuestionObj import QuestionObject
from Questions.ResultDisplay import ResultDisplay
from SupplementaryFiles.Enums import Colours, QuestionTypes


def main():
    questionOne = QuestionObject("how many red nodes there are?", QuestionTypes.NUMBER, 111)
    questionThree = QuestionObject("what is the color that contain the node with the maximun links in the graph?", QuestionTypes.MULTIPLE_CHOICE, 222)
    questionFive = QuestionObject("how many red nodes do not have links blue nodes?", QuestionTypes.NUMBER, 4)
    questionNine = QuestionObject("does every node at color yellow have link to a node of color red?", QuestionTypes.BOOLEAN, 12)
    questionTen = QuestionObject( "is there more red nodes than yellow nodes?", QuestionTypes.BOOLEAN, 14)

    question_list = []
    display = ResultDisplay(question_list)
    display.run()
    answers = q.get()
    for item in answers:
        print("question #{} - {}".format(item.question_number, item.get_answer()))


main()