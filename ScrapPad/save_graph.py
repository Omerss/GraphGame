from SupplementaryFiles.CreateRandGraph import create_rand_graph
from SupplementaryFiles.SaveGraph import save_graph

graph = create_rand_graph("../GraphsData/config.ini")
save_graph(graph, "tmp")