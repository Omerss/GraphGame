import Utils
from GraphObj import GraphObject




def main():
    print("Loading up graph")
    fileRoot = "config.ini"
    Utils.read_config_file(fileRoot)
    size_of_graph = {"x":50,"y":50}

    starting_graph = GraphObject()





if __name__ == "__main__":
    main()