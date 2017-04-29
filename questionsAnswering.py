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
    :return: the Name of the color of the nodes with maximum sum of links
    """
    dictionary = scan_nodes_colors(graph_object, 2)
    max_value = -1
    max_key = ''
    for key in dictionary:
        if dictionary.get(key) > max_value:
            max_value = dictionary.get(key)
            max_key = key

    return max_key



# how many nodes of color X  do not have links to nodes of color Y?
def question_five(graph_object, color_x, color_y):
    """

    :param graph_object: a valid graph object
    :param color_x: a valid color enum
    :param color_y: a valid color enum
    :return: the number of nodes in graph_object of the color color_x that do not have links to nodes of color color_y
    """
    number_of_nodes = boolean_scan_of_nodes(graph_object, is_color_x_unlink_color_y, 1, color_x, color_y)

    return number_of_nodes


# what is the color that contain the node with the minimum links in the graph?
def question_six(graph_object):
    """

    :param graph_object: a valid graph object
    :return: the Name of the color of the node with the minimum links
    """
    dictionary = scan_nodes_colors(graph_object,4)
    min_value = 9999999
    min_key = ''
    for key in dictionary:
        if dictionary.get(key) < min_value:
            min_value = dictionary.get(key)
            min_key = key

    return min_key


# what is the color that contain the minimum sum of links in the graph?
def question_seven(graph_object):
    """

    :param graph_object: a valid graph object
    :return: the Name of the color of the nodes with minimum sum of links
    """
    dictionary = scan_nodes_colors(graph_object, 2)
    min_value = 9999999
    min_key = ''
    for key in dictionary:
        if dictionary.get(key) < min_value:
            min_value = dictionary.get(key)
            min_key = key

    return min_key



# is there a nodes of color X that have a link to another node of color X?
def question_eight(graph_object, color_x):
    """

    :param graph_object: a valid graph object
    :param color_x: a valid color enum
    :return: true - if there is nodes in graph_object of the color color_x that have links to another node of color color_x.
    """
    number_of_nodes = boolean_scan_of_nodes(graph_object, is_color_x_link_color_y, 1, color_x, color_x)
    if number_of_nodes>0:
        return  True
    else:
        return False



#does every node at color X have link to a node of color Y?
def question_nine (graph_object, color_x, color_y):
    """

    :param graph_object: a valid graph object
    :param color_x: a valid color enum
    :param color_y: a valid color enum
    :return: true - if all the nodes in graph_object of the color color_x  have links to a node of color color_y.
    """
    number_of_nodes_color_x= question_one(graph_object,color_x)
    number_color_x_link_y = question_two(graph_object,color_x,color_y)
    if (number_color_x_link_y==number_of_nodes_color_x):
        return  True
    else:
        return False

    # is there more nodes of color X than nodes of color Y?
def question_ten(graph_object, color_x, color_y):
        """

        :param graph_object: a valid graph object
        :param color_x: a valid color enum
        :param color_y: a valid color enum
        :return: the 1 if there is more node of color color_x. 0 otherwise
        """

        dictionary = scan_nodes_colors(graph_object, 1)
        if dictionary.get(color_x['name']) > dictionary.get(color_y['name']):
            return True
        else:
            return False


# is there a nodes of color X that have at least Number link to another node of color X?
def question_eleven(graph_object, color_x, number=2):
    """

    :param graph_object:  a valid graph object
    :param color_x: a valid color enum
    :param number: a positive integer
    :return:  true - if there is nodes in graph_object of the color color_x that have at least "number" of links to another nodes of color color_x.
    """

    number_of_node = boolean_scan_of_nodes(graph_object, is_color_x_link_color_y, 1, color_x,color_x,number)
    if number_of_node > 0:
        return True
    else:
        return False

#is there a node of color X with odd (flag =1)/ even (flag=0) number of links?
def question_twelve(graph_object, color_x, flag):
    """

    :param graph_object: a valid graph object
    :param color_x: a valid color enum
    :param flag: 1 or 0
    :return: if flag = 1, return true if there is a color_x node with odd number of links. if 0 otherwise.
    """

    number_of_nodes = boolean_scan_of_nodes(graph_object, is_node_with_odd_links,1, color_x,flag)
    if number_of_nodes>0:
        return True
    else:
        return False
# does all the color X nodes have odd (flag =1)/ even (flag=0) number of links?
def question_thirteen(graph_object, color_x, flag):
    """

    :param graph_object: a valid graph object
    :param color_x: a valid color enum
    :param flag: flag: 1 or 0
    :return:  if flag = 1, return true if all color_x nodes has odd number of links. if 0 otherwise.
    """
    number_of_nodes = boolean_scan_of_nodes(graph_object, is_node_with_odd_links,1, color_x,flag)
    num = question_one(graph_object, color_x)
    if number_of_nodes == num:
        return True
    else:
        return False

#does the sum of the links in all the nodes at color X is odd (flag =1)/ even (flag=0)?
def question_fourteen(graph_object, color_x, flag):
    """

    :param graph_object: a valid graph object
    :param color_x: a valid color enum
    :param flag: flag: 1 or 0
    :return:  if flag = 1, return true if the sum of all the links at the color_x nodes is odd. if 0 otherwise.
       """
    dictionary = scan_nodes_colors(graph_object, 2)
    if dictionary.get(color_x['name']) %2 ==0:
        if flag == 0:
            return True
        else:
            return False
    else:
        if flag == 0:
            return False
        else:
            return True


#does the number of nodes at color X is odd (flag =1)/ even (flag=0)?
def question_fifteen(graph_object, color_x, flag):
    """
    :param graph_object: a valid graph object
    :param color_x: a valid color enum
    :param flag: flag: 1 or 0
    :return:  if flag = 1, return true if the number of nodes at color X is odd. if 0 otherwise.
    """

    dictionary = scan_nodes_colors(graph_object, 1)
    if dictionary.get(color_x['name']) %2 ==0:
        if flag == 0:
            return True
        else:
            return False
    else:
        if flag == 0:
            return False
        else:
            return True


# which color has the maximum number of nodes?
def question_sixteen(graph_object):
    """

    :param graph_object: a valid graph object
    :return: the Name of the color with the maximum number of nodes
    """

    dictionary = scan_nodes_colors(graph_object, 1)
    max_value = -1
    max_key = ''
    for key in dictionary:
        if dictionary.get(key) > max_value:
            max_value = dictionary.get(key)
            max_key = key

    return max_key


# which color has the minimum number of nodes?
def question_seventeen(graph_object):
    """

    :param graph_object: a valid graph object
    :return: the Name of the color with the minimum number of nodes
    """

    dictionary = scan_nodes_colors(graph_object, 1)
    min_value = 9999999
    min_key = ''
    for key in dictionary:
        if dictionary.get(key) < min_value:
            min_value = dictionary.get(key)
            min_key = key

    return min_key




#useful functions:

# going through the graph object and returning an dict of all the colors and the number of nodes at that color
def scan_nodes_colors(graph_object, flag):
    """
    :param GraphObject: a valid graph object to be scanned
    :param flag: 1- to return the number of nodes at each color. 2- to return the total number of links all the nodes at each color have. 3- to return the max number of links
    :return: if the flag is 1, then return dict contains the number of nodes at each color. if 2 then return dict contains total number of links all the nodes at each color have.
    """
    dictionary = {'red':None, 'green':None, 'blue':None, 'white':None }
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
                if dictionary.get(str_color)< node.get_num_neighbors() or dictionary.get(str_color) is None:
                    dictionary[str_color] =  node.get_num_neighbors()
            if flag == 4:
                if dictionary.get(str_color)> node.get_num_neighbors() or dictionary.get(str_color) is None:
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
    sum = 0
    for node in graph_object.node_list:
        if (node.serial is None):
            continue
        else:

            if flag == 1:
                if (boolean_expression(node, args)):
                    sum= sum +1
            if flag == 2:
                if (boolean_expression(node, args)):
                    sum = sum + node.get_num_neighbors()

    return sum


#unused function
#  Scaning all the nodes in the GraphObject with given Boolean expression, and asking does all the nodes answer to the Boolean expression
#
# def boolean_all_the_nodes_quetioning(graph_object, boolean_expression):
#     """
#
#     :param GraphObject: a valid graph object to be scanned
#     :param Boolean_expression: the  boolean expression that will be used for questioning while scaning the graph. the  boolean expression will be at the following format -
#     param - valid node object. return -  true/false.
#     :return: true - if all the nodes in GraphObject answer to the Boolean expression. flase else.
#     """
#     return
#
#

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

def is_color_x_link_color_y(node_object, color_x, color_y, num=1 ):
    """

    :param node_object: a valid node object
    :param color_x: a valid color enum
    :param color_y: a valid color enum
    :return: true - if node_object of color color_x and link to a node of color color_y. else - false
    """
    if (node_object.serial is None):
        return False
    else:
        tmp =0
        if (node_object.colour == color_x):
            for node in node_object.neighbors:
                if (node.colour == color_y):
                    tmp = tmp +1
                    if (tmp >= num):
                        return True
    return False


def is_color_x_unlink_color_y(node_object, color_x, color_y):
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
                    return False
            return True
    return False


def is_node_with_odd_links (node_object, color_x, flag=1):
    """

    :param node_object: a valid node object
    :param color_x:a valid color enum
    :param flag: 1 or 0
    :return: if flag = 1, return true if node_object have odd num of links.
            if flag = 0, return true if node_object have even num of links.
    """
    if (node_object.serial is None):
        return False
    else:
        if (flag == 1):
            if (node_object.get_num_neighbors() %2 ==0):
                return False
        else:
            if (node_object.get_num_neighbors() % 2 == 1):
                return False
    return True