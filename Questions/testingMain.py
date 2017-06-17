from QuestionObj import QuestionObject
from Questions.QuestionsDisplayObj import QuestionDisplay
from SupplementaryFiles.Enums import Colours
from SupplementaryFiles.CreateRandGraph import create_rand_graph

def main():
    questionOne = QuestionObject("how many red nodes there are?", 1)
    questionThree = QuestionObject("what is the color that contain the node with the maximun links in the graph?", 2)
    questionFive = QuestionObject("how many red nodes do not have links blue nodes?", 1)
    questionNine = QuestionObject("does every node at color yellow have link to a node of color red?", 3)
    questionTen = QuestionObject( "is there more red nodes than yellow nodes?", 3)

    questionList = [questionOne,questionThree,questionFive,questionNine, questionTen]

    display = QuestionDisplay(questionList)
    display.run()
