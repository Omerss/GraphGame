from enum import Enum


class Colours(Enum):
    red = {'R': 1, 'G': 0, 'B': 0, 'name': "red"}
    yellow = {'R': 1, 'G': 1, 'B': 0, 'name': "yellow"}
    blue = {'R': 0, 'G': 0, 'B': 1, 'name': "blue"}


class Shapes(Enum):
    circle = {'name': "Circle"}
