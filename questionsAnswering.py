import GraphObj
import NodeObject
import Enums
from Enums import Colours


#questions functions:


# how many nodes of color X there is?
def question_one(graph_object, color_x):
    """

    :param graph_object: a valid graph object
    :param color_x: a valid color enum
    :return: the number of nodes in graph_object of the color color_x
    """
    number_of_nodes = boolean_scan_of_nodes(graph_object, is_nodes_of_color,1, color_x)

    return number_of_nodes


# how many nodes of color X have links to nodes of color Y?
def question_two(graph_object, color_x, color_y):
    """

    :param graph_object: a valid graph object
    :param color_x: a valid color enum
    :param color_y: a valid color enum
    :return: the number of nodes in graph_object of the color color_x that have links to nodes of color color_y
    """
    number_of_nodes = boolean_scan_of_nodes(graph_object, is_color_x_link_color_y, 1, color_x, color_y)

    return number_of_nodes



# what is the color that contain the node with the maximun links in the graph?
def question_three(graph_object):
    """

    :param graph_object: a valid graph object
    :return: the Name of the color of the node with the maximun links
    """
    dictionary = scan_nodes_colors(graph_object,3)
    max_value = -1
    max_key = ''
    for key in dictionary:
        if dictionary.get(key) > max_value:
            max_value = dictionary.get(key)
            max_key = key


    return max_key



# what is the color that contain the maximun sum of links in the graph?
def question_four(graph_object):
    """

    :param graph_object: a valid graph object
    :return: the color of the nodes with maximum sum of links
    """

return



# going through the graph object and returning an dict of all the colors and the number of nodes at that color
def scan_nodes_colors(graph_object, flag):
    """
    :param GraphObject: a valid graph object to be scanned
    :param flag: 1- to return the number of nodes at each color. 2- to return the total number of links all the nodes at each color have. 3- to return the max number of links
    :return: if the flag is 1, then return dict contains the number of nodes at each color. if 2 then return dict contains total number of links all the nodes at each color have.
    """
    dictionary = {'red':0, 'green':0, 'blue':0, 'white':0 }
    for node in graph_object.node_list:
        if (node.serial is None):
            continue
        else:
            str_color = node.colour['name']
            if flag == 1:
                dictionary[str_color] = dictionary.get(str_color) +1
            if flag == 2:
                dictionary[str_color] = dictionary.get(str_color) + node.get_num_neighbors()
            if flag == 3:
                if dictionary.get(str_color)< node.get_num_neighbors():
                    dictionary[str_color] =  node.get_num_neighbors()

    return  dictionary



# Scaning all the nodes in the GraphObject with given Boolean expression, and return the number of nodes that answer to that boolean expression.

def boolean_scan_of_nodes(graph_object, boolean_expression, flag, *args):
    """

    :param GraphObject: a valid graph object to be scanned
    :param Boolean_expression: the  boolean expression that will be used for questioning while scaning the graph. the  boolean expression will be at the following format -
    param - valid node object. return -  true/false.
    :param flag: 1- to return the number of nodes answering the boolean expression. 2- to return the total number of links all the nodes of nodes answering the boolean expression have.
    :return: if the flag is 1, then return the number of nodes answering the boolean expression. if 2 then return the total number of links all the nodes answering the boolean expression. have.
    """

    return



# Scaning all the nodes in the GraphObject with given Boolean expression, and asking does all the nodes answer to the Boolean expression

def boolean_all_the_nodes_quetioning(graph_object, boolean_expression):
    """

    :param GraphObject: a valid graph object to be scanned
    :param Boolean_expression: the  boolean expression that will be used for questioning while scaning the graph. the  boolean expression will be at the following format -
    param - valid node object. return -  true/false.
    :return: true - if all the nodes in GraphObject answer to the Boolean expression. flase else.
    """
    return



#boolean expressions:

def is_nodes_of_color(node_object, color):
    """

    :param node_object: a valid node object
    :param color: a valid color enum
    :return: true if node_object is at the color- "color". else- return false
    """
    if (node_object.serial is None):
        return False
    else:
        if (node_object.colour == color):
            return True
    return False

def is_color_x_link_color_y(node_object, color_x, color_y):
    """

    :param node_object: a valid node object
    :param color_x: a valid color enum
    :param color_y: a valid color enum
    :return: true - if node_object of color color_x and link to a node of color color_y. else - false
    """
    if (node_object.serial is None):
        return False
    else:
        if (node_object.colour == color_x):
            for node in node_object.neighbors:
                if (node.colour == color_y):
                    return True
    return False
