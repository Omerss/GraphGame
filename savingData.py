'''
folder - name user id
inside:
rounds 10
each round :
real graph xml - graph_round_user id
user seen graph. (real/user_graph_user id_round)
user meta data - key presses by order. for each question- question id, user's answer, args. all precentgaes. button fuct 

'''
import os
from SupplementaryFiles.SaveGraph import save_graph
import json
from Questions import AnswerObject


def save_game_data(location, user_id, game_round, real_graph, user_graph, answers_object_list, node_seen_percentage,
                   user_answers_percentage, user_graph_answer_percentage, button_press_list, button_func_list):
    """
    general function that the game handler will call for.
    if there is no user id folder in the  LOCATION this function will create new one.
    the function pass the round number, and the relevant data for the following saving functions  
    :return: 
    """
    # create folder if not exist
    directory = location + str(user_id)
    if not os.path.exists(directory):
        os.makedirs(directory)
    save_game_graphs(directory, user_id, game_round, real_graph, user_graph)

    save_game_metadata(location, user_id, game_round, answers_object_list, node_seen_percentage,user_answers_percentage,
                       user_graph_answer_percentage, button_press_list, button_func_list)


def save_game_graphs(location, user_id, game_round, real_graph, user_graph):
    """
    
    :param location: an valid address- inside the user folder 
    :param user_id: int, user's id
    :param game_round: int, game round
    :param real_graph: graph object
    :param user_graph: graph object
    :return: 
    """
    save_graph(real_graph, location+"real_graph_"+str(user_id)+"_"+str(round)+".xml")
    save_graph(user_graph, location+"user's_graph_"+str(user_id)+"_"+str(round)+".xml")


def save_game_metadata(location, user_id, game_round, answers_object_list, node_seen_percentage,
                       user_answers_percentage, user_graph_answer_percentage, button_press_list, button_func_list):
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
    :return: 
    
    this function will create a file called - metadata_user id_ game round 
    the file will be in json format
    """
    dict_answers_object_list= {}
    for answer_object in answers_object_list:
        dict_answers_object_list.append(create_dict_for_answer_object(answer_object))
    the_json_data = create_dict_for_game_metadata(dict_answers_object_list, node_seen_percentage,
                                                  user_answers_percentage, user_graph_answer_percentage,
                                                  button_press_list, button_func_list)

    with open(location+"user_metadata"+str(user_id)+"_"+str(round)+".txt", 'w') as outfile:
        json.dump(the_json_data, outfile)


def create_dict_for_answer_object(answers_object):
    """
    
    :param answers_object: an valid answers_object 
    :return: dict with the values: question's id, question args, user's answer
    """
    answer_dict = {'question id number':answers_object.question_number,
                   'question arguments': answers_object.args, 'user answer': answers_object.user_answer}
    return answer_dict


def create_dict_for_game_metadata(dict_answers_object_list, node_seen_percentage, user_answers_percentage,
                                  user_graph_answer_percentage, button_press_list, button_func_list):
    """
    
    :param dict_answers_object_list: list of dicts representing the answer objects
    :param node_seen_percentage: float
    :param user_answers_percentage: float
    :param user_graph_answer_percentage: float
    :param button_press_list: list of the button pressing by order 
    :param button_func_list: list of the button functionality 
    :return: one big dictionary of everything
    """
    dictionary = {'user questions data': dict_answers_object_list, 'seen nodes precentage': node_seen_percentage,
                  'the precentage of user correct answers' : user_answers_percentage,
                  'the precentage of correct answers with the graph that the user saw': user_graph_answer_percentage,
                  'button pressed logger': button_press_list, 'button functionality' : button_func_list}
    return dictionary
