from enum import Enum


Colours = {'yellow': {'R': 1, 'G': 1, 'B': 0, 'name': "yellow"}, 'red': {'R': 1, 'G': 0, 'B': 0, 'name': "red"},
           'blue': {'R': 0, 'G': 0, 'B': 1, 'name': "blue"}}


class Shapes(Enum):
    circle = {'name': "Circle"}


class QuestionTypes(Enum):
    NUMBER = 1
    MULTIPLE_CHOICE = 2
    BOOLEAN = 3
