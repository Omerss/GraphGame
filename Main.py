import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.widget import Widget
from random import randint, random
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from NodeObject import *
from GraphObj import *

circles = []
colors = [[1,0,0],[0,1,0],[0,0,1],[1,0,1],[1,1,0],[0,1,1]]

class GraphNode(Widget):
    x_coor = 0
    y_coor = 0

    def __init__(self, **kwargs):
        super(GraphNode, self).__init__(**kwargs)
        self.bind(pos=self.redraw)
        self.bind(size=self.redraw)
        self.x_coor = randint(100, 650)
        self.y_coor = randint(30, 560)
        self.size = [50, 50]
        self.pos = [self.x_coor,self.y_coor]

    def redraw(self, *args):
        self.canvas.clear()
        with self.canvas:
            Ellipse(pos=self.pos, size=self.size)

    def move_up(self):
        self.y_coor += 10
        self.pos = [self.x_coor, self.y_coor]

    def move_down(self):
        self.y_coor -= 10
        self.pos = [self.x_coor, self.y_coor]

    def move_left(self):
        self.x_coor -= 10
        self.pos = [self.x_coor,self.y_coor]

    def move_right(self):
        self.x_coor += 10
        self.pos = [self.x_coor,self.y_coor]

    def moveGraph(self,newX,newY):
        self.x_coor = self.x_coor + newX
        self.y_coor = self.y_coor + newY
        self.pos = [self.x_coor,self.y_coor]

    def moveJump(self,newX,newY):
        self.x_coor = newX
        self.y_coor = newY
        self.pos = [self.x_coor,self.y_coor]

def buttonUp(instance):
    for i in range(len(circles)):
        circles[i].moveUp()
def buttonDown(instance):
    for i in range(len(circles)):
        circles[i].moveDown()
def buttonLeft(instance):
    for i in range(len(circles)):
        circles[i].moveLeft()
def buttonRight(instance):
    for i in range(len(circles)):
        circles[i].moveRight()
def buttonJump(instance):
    x = randint(-100,100)
    y= randint(-100,100)
    for i in range(len(circles)):
        circles[i].moveGraph(x,y)


# class instructionLabel(Button):
#     def __init__(self,**kwargs):
#         super(instructionLabel,self).__init__(**kwargs)
#         with self.canvas.before:
#                 Color(1,1,1)
#                 Rectangle(pos = (700,0),size = (100,600))
#
# class instructionPanel(BoxLayout):
#     def __init__(self,**kwargs):
#         super(instructionPanel,self).__init__(**kwargs)
#         self.orientation='vertical'
#         self.padding = 20
#         self.spacing = 10


class MyLayout(FloatLayout):

    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        with self.canvas:
            for i in range(10):
                x = randint(0, len(colors)-1)
                Color(colors[x][0], colors[x][1], colors[x][2])
                circles.append(GraphNode())

        layout = GridLayout(cols=1,col_default_width=100, col_force_default=True)
        button1 = Button(background_normal='button1.jpg')
        button1.bind(on_press=buttonJump)
        button2 = Button(background_normal='button2.jpg')
        button2.bind(on_press=buttonDown)
        button3 = Button(background_normal='button3.jpg')
        button3.bind(on_press=buttonLeft)
        button4 = Button(background_normal='button4.jpg')
        button4.bind(on_press=buttonRight)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        self.add_widget(layout)
        ##label=instructionLabel(text = "this is a \nsample text", color=(0,0,1),markup=True, pos=(350,0))
        ##self.add_widget(label)
        ##layoutRight = instructionPanel()
        ##self.add_widget(layoutRight)
        buttonInst = Button(text="this is my sample text",size_hint=(.1,1), pos_hint={'x':.9})
        self.add_widget(buttonInst)


class SampleApp(App):
    def build(self):
        lay = MyLayout()
        return lay


if __name__ == "__main__":
    SampleApp().run()