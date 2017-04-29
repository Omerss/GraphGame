from SupplementaryFiles.NodeObject import NodeObject
class KivyAPI:
    def __init__(self, kivy_graph,bottom_left, top_right, **kwargs):
        self.kivy_graph = kivy_graph
        self.bottom_left = bottom_left
        self.top_right = top_right

    def get_info_from_screen (self):
        """
        :return: node_list of all nodes on the screen. node = [location on screen, size, colour, shape, neighbors, serial]
        """
        kivy_node_list = []
        kivy_edge_list = []
        # go over  all the nodes and check which inside the border
        for kivy_node in self.kivy_graph.nodes:
            if (self.check_if_node_inside_border(kivy_node)):
                kivy_node_list.append(kivy_node)
            #if its half in the range

        # go over  all the edges and check which inside the border
        for kivy_edge in self.kivy_graph.edges:
            #if all the edge inside the border
            if (self.check_if_node_inside_border(kivy_edge.node1)
                or self.check_if_node_inside_border(kivy_edge.node2)
                or self.check_if_line_inside_screen (kivy_edge)):
                    kivy_edge_list.append(kivy_edge)
        #now we create the new nodes
        node_list = []
        i=0
        for kivy_node in kivy_node_list:
            new_node = NodeObject (i,self.calculate_location_on_screen(kivy_node), kivy_node.node_size) #add definition of node's color and shape
            node_list[i] = new_node
            i = i+1
        for kivy_edge in kivy_edge_list:
            #if edge's both nodes inside the screen
            if (self.check_if_node_insid_border(kivy_edge.node1)
                and self.check_if_node_insid_border(kivy_edge.node2)):
                index1 = kivy_node_list.index(kivy_edge.node1)
                index2 = kivy_node_list.index(kivy_edge.node2)
                node_list[index1].neighbors.add (node_list[index2])
                node_list[index2].neighbors.add(node_list[index1])
            # if node1 inside the screen and node 2 not
            if(self.check_if_node_insid_border(kivy_edge.node1)
               and not self.check_if_node_insid_border(kivy_edge.node2)):
                index1 = kivy_node_list.index(kivy_edge.node1)
                new_imaginary_node = self.create_imaginary_node(kivy_edge,kivy_edge.node2)
                node_list[index1].neighbors.add(new_imaginary_node)
                new_imaginary_node.neighbors.add(node_list[index1])
                node_list[i] = new_imaginary_node
                i=i+1
            # if node2 inside the screen and node 1 not
            if(self.check_if_node_insid_border(kivy_edge.node2)
               and not self.check_if_node_insid_border(kivy_edge.node1)):
                index2 = kivy_node_list.index(kivy_edge.node2)
                new_imaginary_node = self.create_imaginary_node(kivy_edge, kivy_edge.node1)
                node_list[index2].neighbors.add(new_imaginary_node)
                new_imaginary_node.neighbors.add(node_list[index2])
                node_list[i] = new_imaginary_node
                i=i+1
            #if both edge's nodes outside the screen
            if( not (self.check_if_node_insid_border(kivy_edge.node2))
               and not self.check_if_node_insid_border(kivy_edge.node1)):
                new_imaginary_node1 = self.create_imaginary_node(kivy_edge, kivy_edge.node1)
                new_imaginary_node2 = self.create_imaginary_node(kivy_edge, kivy_edge.node2)
                new_imaginary_node1.neighbors.add(new_imaginary_node2)
                new_imaginary_node2.neighbors.add(new_imaginary_node1)
                node_list[i] = new_imaginary_node1
                i=i+1
                node_list[i] = new_imaginary_node2
                i=i+1
        return  node_list

    def check_if_node_inside_border (self,kivy_node):
        x_max = self.bottom_left[0] #check
        x_min = self.top_right[0] #check
        y_max =self.bottom_left[1] #check
        y_min =self.top_right[1] #check
        if ((kivy_node.x_coor + (kivy_node.self) / 2 < x_max)
            and (kivy_node.x_coor - (kivy_node.self) / 2 > x_min)
            and (kivy_node.y_coor + (kivy_node.self) / 2 < y_max)
            and (kivy_node.y_coor - (kivy_node.self) / 2 > y_min)):
            return True
        # if its half in the range
        elif ((kivy_node.x_coor < x_max)
              and (kivy_node.x_coor > x_min)
              and (kivy_node.y_coor < y_max)
              and (kivy_node.y_coor > y_min)):

            # think what to do
            return False


    def create_imaginary_node(self,kivy_edge,node):
        edge_slope  = ((kivy_edge.node1.coor_y)-(kivy_edge.node2.coor_y))/((kivy_edge.node1.coor_x)-(kivy_edge.node2.coor_x))
        edge_constent = kivy_edge.node1.coor_y -(edge_slope* kivy_edge.node1.coor_x)
        edge_line_equation = lambda x: edge_slope*x + edge_constent
        if (node.coor_x > self.x_max):
            if (edge_line_equation(self.x_max) > self.y_min
                and (edge_line_equation(self.x_max) < self.y_max )):
                pass
            else:
                pass
        elif  (node.coor_x < self.x_min):
            pass


    def calculate_location_on_screen (self, node):
        x = node.coor_x - self.x_min
        y = node.coor_y - self.y_min
        location = {'x': x, 'y': y}
        return  location

    def  check_if_line_inside_screen (self,kivy_edge):

        x_max = self.bottom_left[0] #check
        x_min = self.top_right[0] #check
        y_max =self.bottom_left[1] #check
        y_min =self.top_right[1] #check

        if ((self.x_max < kivy_edge.node1.coor_x)
            and (self.x_max < kivy_edge.node2.coor_x)):
            return False
        if ((self.x_min > kivy_edge.node1.coor_x)
            and (self.x_min > kivy_edge.node2.coor_x)):
            return False
        if ((self.y_max < kivy_edge.node1.coor_y)
            and (self.y_max < kivy_edge.node2.coor_y)):
            return False
        if ((self.y_min > kivy_edge.node1.coor_y)
            and (self.x_min > kivy_edge.node2.coor_y)):
            return False

        edge_slope  = ((kivy_edge.node1.coor_y)-(kivy_edge.node2.coor_y))/((kivy_edge.node1.coor_x)-(kivy_edge.node2.coor_x))
        edge_constent = kivy_edge.node1.coor_y -(edge_slope* kivy_edge.node1.coor_x)
        edge_line_equation = lambda x: edge_slope*x + edge_constent
        reverse_edge_line_equation = lambda y: (y-edge_constent)/(edge_slope)
        # now we check if its touch the screen boareders
        if (edge_line_equation (x_max) > y_min and
            edge_line_equation(x_max) < y_max) :
            return  True
        if (edge_line_equation (x_min) > y_min and
            edge_line_equation(x_min) < y_max) :
            return True
        if (reverse_edge_line_equation (y_min) > x_min and
                    reverse_edge_line_equation(y_min) < x_max) :
            return True
        if (reverse_edge_line_equation (y_max) > x_min and
                    reverse_edge_line_equation(y_max) < x_max) :
            return True

        return False