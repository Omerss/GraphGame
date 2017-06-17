from QuestionObj import QuestionObject
from SupplementaryFiles.Enums import Colours
from SupplementaryFiles.CreateRandGraph import create_rand_graph

def main():
    graph = create_rand_graph(config_file)
    questionOne = QuestionObject("how many red nodes there are?", 1,graph, Colours.red)
    questionThree = QuestionObject("what is the color that contain the node with the maximun links in the graph?", 3, graph)
    questionFive = QuestionObject("how many ref nodes do not have links blue nodes?", 5,graph, Colours.red, Colours.blue)
    questionNine = QuestionObject("does every node at color yellow have link to a node of color red?", 9,graph, Colours.yellow, Colours.red)
    questionTen = QuestionObject( "is there more red nodes than yellow nodes?", 10 , graph,Colours.red, Colours.yellow)

    questionList = [questionOne,questionThree,questionFive,questionNine, questionTen]

    pass
