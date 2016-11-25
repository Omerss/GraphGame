

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import *
import random
import math
from random import random

import Utils
from NodeObject import NodeObject
from GraphObj import GraphObject

def creatRandGraph (numberOfNodes,lineColor, circlesSize, lowLimitOfGraph, highLimitOfGraph,lineWidth, extraSpace,maxConnections,minNodeConnections):
    newGraph = GraphObject()

    for i in range(0, numberOfNodes):

        xRandom = random.randint(lowLimitOfGraph, highLimitOfGraph)
        yRandom = random.randint(lowLimitOfGraph, highLimitOfGraph)
        if ((checkCollisions(xRandom, yRandom, newGraph, circlesSize, lineWidth, extraSpace))):
            i = i - 1
            continue

        color = getColor()

        newGraph.addNode (i, xRandom,yRandom, circlesSize, color, "circle",circlesSize)

    connectGraph(newGraph)
    return newGraph, lineColor, lineWidth


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        with self.canvas:
            graph,lineColor, lineWidth = creatRandGraph(numberOfNodes,lineColor, circlesSize, lowLimitOfGraph, highLimitOfGraph,lineWidth, extraSpace,maxConnections,minNodeConnections)

            for i in range(0, len(graph.node_list)):
                # paint the color
                color = graph.node_list[i].colour
                doTheRightColor (color)

                #paint the circle
                Line(circle=(graph.node_list[i].location ('x'),  graph.node_list[i].location ('y'), graph.node_list[i].size), width=lineWidth)

                #paint the lines

                color = lineColor
                doTheRightColor (color)
                drawConnections (graph.node_list[i])







class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()






def drawConnections (node):
    for i in range (0,len(node.neighbors)):
        drawLine(node.location ('x'),node.location ('y'),node.neighbors[i].location ('x'), node.neighbors[i].location ('y'))

def drawLine (xNode0,yNode0,xNode,yNode):
    Line(points=[xNode0, yNode0 ,xNode, yNode])

def getColor ():
    return "green"


def doTheRightColor (color):
    if (color == "black"):
        Color(0.0, 0.0, 0.0)
    if (color == "red"):
        Color(1.0, 0.0, 0.0)
    if (color == "green"):
        Color(0.0, 1.0, 0.0)
    if (color == "blue"):
        Color(0.0, 0.0, 1.0)

def connectGraph (graph,maxConnections,minNodeConnections):
    for i in range(0, len(graph.node_list)):
        graph.get_possible_connections(graph.node_list[i])

    for i in range(0, len(graph.node_list)):
        if ((len(graph.node_list[i].neighbors))<maxConnections):
            for j in range (0, ((len(graph.node_list[i].neighbors))-minNodeConnections)) :
                if (len(list) ==0 ):
                    print "error"
                    break
                nodeIndex = graph.get_best_connection(graph.node_list[i])
                graph.connect_nodes (graph.node_list[i],graph.get_node_by_serial(nodeIndex))#find by index)


    return graph

def checkCollisions(xRandom,yRandom,graph,circlesSize,lineWidth,extraSpace):
    for i in range(0, len(graph.node_list)):
        if ((checkCollision(xRandom,yRandom,graph.node_list[i].xLocation,graph.node_list[i].yLocation,extraSpace))):
            return 1

    return 0

def checkCollision (xRandom,yRandom,xNode,yNode,circlesSize,lineWidth,extraSpace):
    dis = math.sqrt(math.pow((xRandom - xNode, 2) + math.pow((yRandom - yNode, 2))))
    if (dis < (lineWidth + circlesSize) * 2):
        return 1
    return 0