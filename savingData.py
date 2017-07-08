'''
folder - name user id
insdie:
rounds 10
each round :
real graph xml - graph_round_user id
user seen graph. (real/user_graph_user id_round)
user meta data - key presses by order. for each question- question id, user's answer, args. all precentgaes. button fuct 

'''



def save_game_data ():
    """
    general function that the game handler will call for.
    if there is no user id folder in the  LOCATION this function will create new one.
    the function pass the round number, and the relevant data for the following saving functions  
    :return: 
    """


def save_game_graphs (location, user_id, game_round, real_graph, user_graph):
    """
    
    :param location: an valid address- inside the user folder 
    :param user_id: int, user's id
    :param game_round: int, game round
    :param real_graph: graph object
    :param user_graph: graph object
    :return: none if success, error string if failed 
    """


def save_game_metadata(location, user_id, game_round, answers_object_list, node_seen_percentage, user_answers_percentage, user_graph_answer_percentage, button_press_list, button_func_list):
    """
    json.dumps
    :param location: an valid address- inside the user folder 
    :param user_id: int, user's id
    :param game_round: int, game round
    :param answers_object_list: list contains answer objects
    :param node_seen_percentage: float
    :param user_answers_percentage: float
    :param user_graph_answer_percentage: float
    :param button_press_list: list of the button pressing by order 
    :param button_func_list: list of the button functionality
    :return: none if success, error string if failed 
    
    this function will create a file called - metadata_user id_ game round 
    the file will be in json format
    """


def create_dict_for_answer_object(answers_object):
    """
    
    :param answers_object: an valid answers_object 
    :return: dict with the values: question's id, question args, user's answer
    """


def create_dict_for_game_metadata(dict_answers_object_list, node_seen_percentage, user_answers_percentage, user_graph_answer_percentage, button_press_list, button_func_list):
    """
    
    :param dict_answers_object_list: list of dicts representing the answer objects
    :param node_seen_percentage: float
    :param user_answers_percentage: float
    :param user_graph_answer_percentage: float
    :param button_press_list: list of the button pressing by order 
    :param button_func_list: list of the button functionality 
    :return: one big dictionary of everything
    """