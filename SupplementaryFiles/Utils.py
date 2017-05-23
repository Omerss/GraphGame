import configparser

config = configparser.ConfigParser()


def read_config_file(path):
    config.sections()
    config.read(path)

    # assert config file
    return config


def max_nodes_per_size(size):
    max_nodes = 0
    return max_nodes


def get_enum_items(enum_object):
    list = enum_object.__dict__.keys()
    list.remove("__doc__")
    list.remove("__module__")
    return list