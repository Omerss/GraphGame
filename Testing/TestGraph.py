import random
import math
from random import random

import Utils
from NodeObject import NodeObject
from GraphObj import GraphObject



def testCreate_graph ():
    newGraph = GraphObject ()
    assert (newGraph.node_list == [])
    #assert (newGraph.size == {})
    assert (newGraph.extra_distance == 1)
    assert (newGraph.max_neighbors == 4)
    return 1


def testAdd_node():
    newGraph = GraphObject()
    newGraph.add_node(1,10)
    assert(newGraph.node_list[0].location('x')==1)
    assert (newGraph.node_list[0].location('y') == 10)
    assert (newGraph.node_list[0].size == 1)
    location = {'x': 1, 'y': 10}
    assert (newGraph.node_list[0].serial == newGraph.get_serial(location))
    return 1


def testGet_possible_connections():
    newGraph = GraphObject()
    newGraph.add_node(1, 10)
    newGraph.add_node(1, 100)
    newGraph.add_node(1, 200)
    serial = newGraph.node_list[0].serial
    serial2 = newGraph.node_list[1].serial
    serial3 =newGraph.node_list[2].serial
    list = newGraph.get_possible_connections(serial)

    assert (list.__contains__(serial3))
    assert (not(list.__contains__(serial2)))
    return 1

def testGet_best_connection():
    newGraph = GraphObject()
    newGraph.add_node(1, 10)
    newGraph.add_node(1, 100)
    newGraph.add_node(1, 200)
    serial = newGraph.node_list[0].serial
    serial3 =newGraph.node_list[2].serial
    list = newGraph.get_possible_connections(serial)
    id = newGraph.get_best_connection(list)
    assert (id ==serial3)
    return 1


def testGet_node_by_serial():
    newGraph = GraphObject()
    newGraph.add_node(1, 10)
    newGraph.add_node(1, 100)
    newGraph.add_node(1, 200)
    serial = newGraph.node_list[0].serial
    serial2 = newGraph.node_list[1].serial
    serial3 = newGraph.node_list[2].serial

    assert ((newGraph.get_node_by_serial(serial).location('y'))==10)
    assert ((newGraph.get_node_by_serial(serial2).location('y')) == 100)
    assert ((newGraph.get_node_by_serial(serial3).location('y')) == 200)

    return 1

def testIs_node_far_enough():
    newGraph = GraphObject()
    newGraph.add_node(1, 10)
    newGraph.add_node(1, 100)
    newGraph.add_node(1, 200)
    serial = newGraph.node_list[0].serial
    serial2 = newGraph.node_list[1].serial
    serial3 = newGraph.node_list[2].serial
    return 1

def testGet_serial ():

    return 1
