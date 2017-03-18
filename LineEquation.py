from Point import Point


class LineEquation:
    def __init__(self):
        """
        edge1 and edge2 are the x value of the edge point of the line
        """
        self.slope = None
        self.const = None
        self.edge1 = None
        self.edge2 = None

    @staticmethod
    def check_collision_point(eq1, eq2):
        """

        :param eq1: a LineEquation type
        :param eq2: a LineEquation type
        :return: True if the collision of the two line actually happens on the graph
        """
        point = LineEquation.get_equation_collision_point(eq1, eq2)
        if (eq1.edge1 < point[0] < eq1.edge2) or \
                (eq1.edge1 > point[0] > eq1.edge2) or \
                (eq2.edge1 < point[0] < eq2.edge2) or \
                (eq2.edge1 > point[0] > eq2.edge2):
            return True
        else:
            return False

    @staticmethod
    def create_equation(point1, point2):
        """
        Creates a line equation give two points as edges
        :return:  A line LineEquation object
        """
        assert (type(point1) == Point and type(point2) == Point)
        if point1.x == point2.x:
            pass
        else:
            # y = m*x + b
            location_equation = LineEquation()
            location_equation.slope = (point1.y - point2.y)/(point1.x - point2.x)
            location_equation.const = point1.y - location_equation.slope*point1.y #b
            location_equation.edge1 = min(point1.x, point2.x)
            location_equation.edge2 = max(point1.x, point2.x)
            return location_equation

    @staticmethod
    def get_equation_collision_point(eq1, eq2):
        """

        :param eq1: a LineEquation type
        :param eq2: a LineEquation type
        :return: An absolute collision point in virtual space. This point might not exists if vectors are capped.
        """
        tmp_x = eq1.slope - eq2.slope
        tmp_const = eq2.const - eq1.const
        if tmp_x < 0:
            tmp_x *= -1
            tmp_const *= -1
        point_x = tmp_const / tmp_x
        point_y = point_x * eq1.slope + eq1.const
        return point_x, point_y



