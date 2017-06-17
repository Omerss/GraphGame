from Queue import Queue

from QuestionObj import QuestionObject
from Questions.QuestionsDisplayObj import QuestionDisplay
from SupplementaryFiles.Enums import Colours, QuestionTypes

def main():
    questionOne = QuestionObject("how many red nodes there are?", QuestionTypes.NUMBER)
    questionThree = QuestionObject("what is the color that contain the node with the maximun links in the graph?", QuestionTypes.MULTIPLE_CHOICE)
    questionFive = QuestionObject("how many red nodes do not have links blue nodes?", QuestionTypes.NUMBER)
    questionNine = QuestionObject("does every node at color yellow have link to a node of color red?", QuestionTypes.BOOLEAN)
    questionTen = QuestionObject( "is there more red nodes than yellow nodes?", QuestionTypes.BOOLEAN)

    questionList = [questionOne,questionThree,questionFive,questionNine, questionTen]
    q = Queue()
    display = QuestionDisplay(questionList, q)
    display.run()

main()