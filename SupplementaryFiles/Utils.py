import configparser

config = configparser.ConfigParser()
config.sections()
image_folder = "..//Images"


def read_config_file(path, save_to_main=False):
    my_config = configparser.ConfigParser()
    my_config.sections()
    my_config.read(path)
    if save_to_main:
        config.read(path)
    return my_config


def max_nodes_per_size(size):
    max_nodes = 0
    return max_nodes


def get_enum_items(enum_object):
    list = enum_object.__dict__.keys()
    list.remove("__doc__")
    list.remove("__module__")
    return list