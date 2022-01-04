from states.game_in_progress.circle import Circle


def is_neighbour_same_color(neighbour, visited, extracted):
    return isinstance(neighbour, Circle) and \
           neighbour.position not in visited.keys() and \
           neighbour.color == extracted.color


def is_neighbour_circle(neighbour, visited, extracted):
    return isinstance(neighbour, Circle) and \
           neighbour.position not in visited.keys()
