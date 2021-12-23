from pygame.surface import Surface, SurfaceType
import random
from typing import Union

import geometry
from circle import Circle
from empty_element import EmptyElement
from colors import table


class Level:

    def __init__(self, level_config: str, window: Union[Surface, SurfaceType], radius, score_area_height):
        level_lines = level_config.split(';')
        self.level_lines = [level_line.split(',') for level_line in level_lines]
        self.max_nr_circles_line = len(self.level_lines[0])
        self.available_width = window.get_height() - 5 * radius
        self.available_colors = dict()
        self.radius = radius
        self.score_area_height = score_area_height
        self.directions = [(-self.radius, -(2 * self.radius - 5)), (self.radius, -(2 * self.radius - 5)), (2 * self.radius, 0), (self.radius, 2 * self.radius - 5),
                           (-self.radius, 2 * self.radius - 5), (-2 * self.radius, 0)]
        self.__build_board()

    def __build_board(self):
        self.board = dict()
        current_height = self.score_area_height + 2 * self.radius
        last_length = 0
        for level_line in self.level_lines:
            current_position = (2 * self.radius, current_height) if len(level_line) == self.max_nr_circles_line else (3 * self.radius, current_height)
            last_length = self.max_nr_circles_line if len(level_line) == self.max_nr_circles_line else self.max_nr_circles_line - 1
            for color in level_line:
                if color in table.keys():
                    self.board[current_position] = Circle(self.radius, current_position, table[color])
                    if color in self.available_colors.keys():
                        self.available_colors[color] += 1
                    else:
                        self.available_colors[color] = 1
                else:
                    self.board[current_position] = EmptyElement(current_position)
                current_position = current_position[0] + 2 * self.radius, current_height
            current_height += 2 * self.radius - 5

        while current_height <= self.available_width:
            last_length = 2 * self.max_nr_circles_line - 1 - last_length
            current_position = (2 * self.radius, current_height) if last_length == self.max_nr_circles_line else (3 * self.radius, current_height)
            for i in range(0, last_length):
                self.board[current_position] = EmptyElement(current_position)
                current_position = current_position[0] + 2 * self.radius, current_height
            current_height += 2 * self.radius - 5

    def provide_colors(self):
        colors = list(self.available_colors.keys())
        current_color_index = random.randint(0, len(colors) - 1)
        next_color_index = random.randint(0, len(colors) - 1)
        return {
            'current-color': table[colors[current_color_index]],
            'next-color': table[colors[next_color_index]]
        }

    def detect_collision(self, shooting_circle):
        positions = list(self.board.keys())
        for position in positions:
            if isinstance(self.board[position], Circle):
                if geometry.get_distance(position, shooting_circle.position) <= self.board[position].radius + shooting_circle.radius:
                    neighbours_positions = [(position[0] + direction[0], position[1] + direction[1]) for direction in self.directions]
                    neighbours_valid_positions = [neighbour_position for neighbour_position in neighbours_positions if neighbour_position in self.board.keys()]
                    neighbours = [self.board[neighbour_valid_position] for neighbour_valid_position in neighbours_valid_positions]
                    empty_neighbours = [neighbour for neighbour in neighbours if isinstance(neighbour, EmptyElement)]
                    empty_neighbours.sort(key=lambda neighbour: geometry.get_distance(neighbour.position, shooting_circle.position))
                    element_to_update = empty_neighbours[0]
                    self.board[element_to_update.position] = Circle(shooting_circle.radius, element_to_update.position, shooting_circle.color)
                    return True
        return False

    def draw(self, window: Union[Surface, SurfaceType]):
        positions = list(self.board.keys())
        for position in positions:
            if isinstance(self.board[position], Circle):
                self.board[position].draw(window)
