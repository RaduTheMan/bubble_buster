import math


def get_equation_line(first_point, second_point):
    slope = (first_point[1] - second_point[1]) / (first_point[0] - second_point[0])
    b = first_point[1] - slope * first_point[0]
    return {
        'slope': slope,
        'b': b
    }


def get_distance(first_point, second_point):
    return math.sqrt((second_point[0] - first_point[0]) ** 2
                     + (second_point[1] - first_point[1]) ** 2)


def get_point_at_distance(first_point, second_point, distance=0.5):
    n = get_distance(first_point, second_point)
    x = first_point[0] + distance / n * (second_point[0] - first_point[0])
    y = first_point[1] + distance / n * (second_point[1] - first_point[1])
    return x, y
