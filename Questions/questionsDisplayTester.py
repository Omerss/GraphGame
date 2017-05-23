from QuestionsDisplayObj import QuestionDisplay
import unittest
from QuestionObj import QuestionObject





if __name__ == '__main__':
    question1 = QuestionObject( "do you like cats?", 1)
    question2 = QuestionObject("do you like bats?", 2)
    question3 = QuestionObject("do you like smurfs?", 3)
    question4 = QuestionObject("???", 4)
    question5 = QuestionObject("!!!!", 5)
    x = QuestionDisplay()
    x.run()