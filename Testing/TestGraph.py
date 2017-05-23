import unittest

from SupplementaryFiles.GraphObj import GraphObject


class TestNode(unittest.TestCase):

    def test_create_graph(self):
        # Arrange
        max_neighbors = 5
        extra_distance = 1
        # Act
        new_graph = GraphObject(max_x=1000, max_y=1000, node_count=20, max_neighbors=max_neighbors, extra_distance=extra_distance)
        # Assert
        assert (new_graph.node_list == [])
        assert (new_graph.extra_distance == extra_distance)
        assert (new_graph.max_neighbors == max_neighbors)

    def test_add_node(self):
        # Arrange
        x_coor = 50
        y_coor = 50
        size = 4
        new_graph = GraphObject(max_x=1000, max_y=1000, node_count=20, max_neighbors=5,
                                extra_distance=10)

        # Act
        new_graph.add_node(x_coor, y_coor, node_size=size)

        # Assert
        assert (new_graph.node_list[0].location('x') == x_coor)
        assert (new_graph.node_list[0].location('y') == y_coor)
        assert (new_graph.node_list[0].size == size)

    def test_get_possible_connections(self):
        # Arrange
        new_graph = GraphObject(max_x=1000, max_y=1000, node_count=20, max_neighbors=5,
                                extra_distance=10)

        # Act
        new_graph.add_node(50, 50)
        new_graph.add_node(50, 100)
        new_graph.add_node(50, 200)
        serial1 = new_graph.node_list[0].serial_num
        serial2 = new_graph.node_list[1].serial_num
        serial3 = new_graph.node_list[2].serial_num
        list = new_graph.get_possible_connections(serial1)

        # Assert
        assert (list.__contains__(serial3))
        assert (not (list.__contains__(serial2)))



    def test_get_best_connection(self):
        # Arrange
        new_graph = GraphObject(max_x=1000, max_y=1000, node_count=20, max_neighbors=5,
                                extra_distance=10)
        new_graph.add_node(50, 50)
        new_graph.add_node(50, 100)
        new_graph.add_node(50, 200)
        serial = new_graph.node_list[0].serial_num
        serial3 = new_graph.node_list[2].serial_num

        # Act
        list = new_graph.get_possible_connections(serial)
        id = new_graph.get_best_connection(list)

        # Assert
        assert (id == serial3)


    def test_get_node_by_serial(self):
        # Arrange
        new_graph = GraphObject(max_x=1000, max_y=1000, node_count=20, max_neighbors=5,
                                extra_distance=10)
        new_graph.add_node(50, 50)
        new_graph.add_node(50, 100)
        new_graph.add_node(50, 200)

        # Act
        serial = new_graph.node_list[0].serial_num
        serial2 = new_graph.node_list[1].serial_num
        serial3 = new_graph.node_list[2].serial_num

        # Assert
        assert ((new_graph.get_node_by_serial(serial).location('y')) == 10)
        assert ((new_graph.get_node_by_serial(serial2).location('y')) == 100)
        assert ((new_graph.get_node_by_serial(serial3).location('y')) == 200)


    def test_is_node_far_enough(self):
        # Arrange
        new_graph = GraphObject(max_x=1000, max_y=1000, node_count=20, max_neighbors=5,
                                extra_distance=10)
        new_graph.add_node(50, 50)
        new_graph.add_node(50, 100)
        new_graph.add_node(50, 200)
        serial = new_graph.node_list[0].serial_num
        serial2 = new_graph.node_list[1].serial_num
        serial3 = new_graph.node_list[2].serial_num

        # Act

        # Assert
        assert (not(new_graph.is_node_far_enough(new_graph.node_list [1],new_graph.node_list[0],new_graph.node_list[2])))
        assert (new_graph.is_node_far_enough(new_graph.node_list[0], new_graph.node_list [1],new_graph.node_list [2]))


    def test_get_serial(self):
        # Arrange
        new_graph = GraphObject(max_x=1000, max_y=1000, node_count=20, max_neighbors=5,
                                extra_distance=10)
        new_graph.add_node(50, 50)
        new_graph.add_node(50, 200)
        serial = new_graph.node_list[0].serial_num
        serial2 = new_graph.node_list[1].serial_num

        # Act
        checkSerial = new_graph.get_serial(new_graph.node_list[0])
        checkSerial2 = new_graph.get_serial(new_graph.node_list[1])

        # Assert
        assert (checkSerial == serial)
        assert  (checkSerial2 == serial2)


if __name__ == '__main__':
    unittest.main()

