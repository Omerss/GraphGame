import os
from Queue import Queue

from QuestionObject import QuestionObject
from Questions.AnswerObject import AnswerObject
from Questions.QuestionWidgets import IntInput
from Questions.QuestionsDisplay import QuestionDisplay
from Questions.ResultDisplay import ResultDisplay
from SupplementaryFiles.CreateRandGraph import create_rand_graph
from SupplementaryFiles.Enums import Colours, QuestionTypes


def main():

    user_graph = create_rand_graph("{}\..\GraphsData\config.ini".format(os.getcwd()))
    true_graph = create_rand_graph("{}\..\GraphsData\config.ini".format(os.getcwd()))
    for i in range(len(user_graph.node_list)):
        user_graph.node_list[i].colour = Colours.yellow['name']
        true_graph.node_list[i].colour = Colours.red['name']

    for i in range(len(user_graph.node_list)-5):
        user_graph.node_list[i].colour = Colours.red['name']

    answer_list = []

    for i in range(10):
        question_data = QuestionObject("how many {} nodes there are?", QuestionTypes.NUMBER, 1, Colours.red)
        question = IntInput(question=question_data)
        question.text = '6'
        answer = AnswerObject(question_object=question, user_seen_graph=user_graph, real_graph=true_graph)
        answer_list.append(answer)

    display = ResultDisplay(answer_list, user_graph, true_graph)
    display.run()

if __name__ == "__main__":
    main()

