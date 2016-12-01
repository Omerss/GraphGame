import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color, Ellipse
from kivy.uix.widget import Widget
from random import randint,random

circles = []

class GraphNode(Widget):
    x_coor = 0
    y_coor = 0
    def __init__(self, **kwargs):
        super(GraphNode, self).__init__(**kwargs)
        self.bind(pos=self.redraw)
        self.bind(size=self.redraw)
        self.x_coor = randint(100, 770)
        self.y_coor = randint(30, 560)
        self.size = [40, 40]
        self.pos = [self.x_coor,self.y_coor]

    def redraw(self, *args):
        self.canvas.clear()
        with self.canvas:
            Ellipse(pos=self.pos, size=self.size)

    def moveUp(self):
        self.y_coor = self.y_coor + 10
        self.pos = [self.x_coor,self.y_coor]

    def moveDown(self):
        self.y_coor = self.y_coor - 10
        self.pos = [self.x_coor, self.y_coor]

    def moveLeft(self):
        self.x_coor = self.x_coor - 10
        self.pos = [self.x_coor,self.y_coor]

    def moveRight(self):
        self.x_coor = self.x_coor + 10
        self.pos = [self.x_coor,self.y_coor]

def callback1(instance):
    for i in range(len(circles)):
        circles[i].moveUp()
def callback2(instance):
    for i in range(len(circles)):
        circles[i].moveDown()
def callback3(instance):
    for i in range(len(circles)):
        circles[i].moveLeft()
def callback4(instance):
    for i in range(len(circles)):
        circles[i].moveRight()

class myLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(myLayout, self).__init__(**kwargs)
        with self.canvas:
            Color(1,0,0)
            circles.append(GraphNode())
            Color(0,1,0)
            circles.append(GraphNode())
            Color(0,0,1)
            circles.append(GraphNode())
        layout = BoxLayout(orientation='vertical',size_hint=(0.1, 1), padding=10, spacing=20)
        button1 = Button(background_normal='button1.png')
        button1.bind(on_press=callback1)
        button2 = Button(background_normal='button2.jpg')
        button2.bind(on_press=callback2)
        button3 = Button(background_normal='button3.jpg')
        button3.bind(on_press=callback3)
        button4 = Button(background_normal='button4.jpg')
        button4.bind(on_press=callback4)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        self.add_widget(layout)


class SampleApp(App):
    def build(self):
        lay = myLayout()
        return lay


if __name__ == "__main__":
    SampleApp().run()



