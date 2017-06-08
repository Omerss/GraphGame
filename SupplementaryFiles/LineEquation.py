from Point import Point

LINES_ALWAYS_MEET = 'always'  # used when both line equations have the same slope + const


class LineEquation:
    def __init__(self):
        """
        edge1 and edge2 are the x value of the edge point of the line
        """
        self.slope = None
        self.const = None
        self.edge1 = None
        self.edge2 = None

    def __repr__(self):
        return 'slope:{}, const:{}, edge1:{}, edge2:{}'.format(self.slope, self.const, self.edge1, self.edge2)

    @staticmethod
    def check_collision_point(eq1, eq2):
        """

        :param eq1: a LineEquation type
        :param eq2: a LineEquation type
        :return: True if the collision of the two line actually happens on the graph
        """
        point = LineEquation.get_equation_collision_point(eq1, eq2)
        if point is None:
            return False

        if point == LINES_ALWAYS_MEET:
            if LineEquation.point_in_between_edges([eq1.edge1], eq2) \
                    or LineEquation.point_in_between_edges([eq1.edge2], eq2) \
                    or LineEquation.point_in_between_edges([eq2.edge1], eq1) \
                    or LineEquation.point_in_between_edges([eq2.edge2], eq1):
                return True
            else:
                return False

        if LineEquation.point_in_between_edges(point, eq1) and LineEquation.point_in_between_edges(point, eq2):
            return True
        else:
            return False

    @staticmethod
    def point_in_between_edges(point, eq1):
        if eq1.edge1 <= point[0] <= eq1.edge2 or eq1.edge1 >= point[0] >= eq1.edge2:
            return True
        else:
            return False

    @staticmethod
    def create_equation(point1, point2):
        """
        Creates a line equation give two points as edges
        :return:  A line LineEquation object
        """
        assert isinstance(point1, Point) and isinstance(point2, Point)
        if point1.x == point2.x:
            pass
        else:
            # y = m*x + b
            location_equation = LineEquation()
            location_equation.slope = float(point1.y - point2.y) / (point1.x - point2.x)
            location_equation.const = point1.y - location_equation.slope * point1.x  # b
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
        slope_variation = eq1.slope - eq2.slope
        const_variation = eq2.const - eq1.const
        if slope_variation == 0:
            if const_variation == 0:
                return LINES_ALWAYS_MEET
            else:
                # Lines are parallel
                return None
        else:
            if slope_variation < 0:
                slope_variation *= -1
                const_variation *= -1
            point_x = const_variation / slope_variation
            point_y = point_x * eq1.slope + eq1.const
            return point_x, point_y
