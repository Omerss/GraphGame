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

