import math


def get_equation_line(first_point, second_point):
    if first_point[0] == second_point[0]:
        return {
            'slope': "UNDEFINED",
            'b': 0
        }
    slope = (first_point[1] - second_point[1]) / \
            (first_point[0] - second_point[0])
    b = first_point[1] - slope * first_point[0]
    return {
        'slope': slope,
        'b': b
    }


def get_distance(first_point, second_point):
    return math.sqrt((second_point[0] - first_point[0]) ** 2
                     + (second_point[1] - first_point[1]) ** 2)


def get_point_at_distance(point, slope, distance=0.25):
    if slope != "UNDEFINED":
        magnitude = math.sqrt(1 + slope ** 2)
        n = 1 / magnitude, slope / magnitude
    else:
        n = 0, 1
    first_solution = point[0] + distance * n[0], point[1] + distance * n[1]
    second_solution = point[0] - distance * n[0], point[1] - distance * n[1]
    return first_solution if first_solution[1] < point[1] else second_solution
