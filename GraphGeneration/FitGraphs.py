# 1478.4, 'max_y': 1200
# 640.0, 'max_y': 600


class FitGraphs():

    def __init__(self, graph):
        zoom_x = 1536.0 / 640
        zoom_y = 1090.0 / 600
        size_x = graph.size["max_x"] * zoom_x
        size_y = graph.size["max_y"] * zoom_y
        self.get_nodes(graph, zoom_x, zoom_y)

    def get_nodes(self, original_graph, zoom_x, zoom_y):
        max_x = 0
        max_y = 0
        for node in original_graph.node_list:
            x_coor = int(node.x * zoom_x)
            y_coor = int(node.y * zoom_y)
            if x_coor > max_x:
                max_x = x_coor
            if y_coor > max_y:
                max_y = y_coor
            new_serial = node.serial_num
            colour = node.colour['name']
            print "draft_graph.add_node(x_loc={}, y_loc={}, node_colour=Colours['{}'], serial='{}')".format(x_coor, y_coor, colour, new_serial)
        print "max_x={}, max_y={}".format(max_x, max_y)