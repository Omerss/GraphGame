image_folder = "..//Images"
config = None

def read_config_file(path, save_to_main=False):
    my_config = read_file(path)
    if save_to_main:
        config = my_config
    return my_config

def read_file(path):
    config_dict = {}
    with open(path, 'r') as f:
        for line in f:
            new_line = parse_line(line)
            key = new_line.keys()
            if not key[0] in config_dict:
                config_dict[key[0]] = {}
            inner_key = new_line[key[0]].keys()
            config_dict[key[0]][inner_key[0]] = new_line[key[0]][inner_key[0]].rstrip()
    return config_dict

def parse_line(line):
    point_index = line.find(".")
    equal_index = line.find("=")
    new_dict = {}
    new_dict[line[:point_index]] = {}
    new_dict[line[:point_index]][line[point_index+1:equal_index]] = line[equal_index+1:]
    return new_dict


def max_nodes_per_size(size):
    max_nodes = 0
    return max_nodes


def get_enum_items(enum_object):
    list = enum_object.__dict__.keys()
    list.remove("__doc__")
    list.remove("__module__")
    return list
