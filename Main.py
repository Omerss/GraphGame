import configparser
from GraphObj import GraphObject

dataFile = configparser.ConfigParser()


def main():
    print("Loading up graph")
    filePath = "config.ini"

    read_config_file(filePath)
    print(dataFile["GeneralParams"]["NodeCount"])

    startingGraph = GraphObject(filePath)

def read_config_file(path):
    dataFile.sections()
    dataFile.read(path)


if __name__ == "__main__":
    main()