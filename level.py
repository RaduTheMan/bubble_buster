from pygame.surface import Surface, SurfaceType
from random import randrange
from typing import Union
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
        self.__build_board()

    def __build_board(self):
        # TO CHANGE FROM HARDCODED VALUES INTO PROPER VARIABLES
        self.board = []
        current_height = self.score_area_height + 40
        last_length = 0
        for level_line in self.level_lines:
            current_position = (40, current_height) if len(level_line) == self.max_nr_circles_line else (60, current_height)
            last_length = self.max_nr_circles_line if len(level_line) == self.max_nr_circles_line else self.max_nr_circles_line - 1
            elements = []
            for color in level_line:
                if color in table.keys():
                    elements.append(Circle(self.radius, current_position, table[color]))
                    if color in self.available_colors.keys():
                        self.available_colors[color] += 1
                    else:
                        self.available_colors[color] = 1
                else:
                    elements.append(EmptyElement(current_position))
                current_position = current_position[0] + 40, current_height
            self.board.append(elements)
            current_height += 35

        while current_height <= self.available_width:
            last_length = 2 * self.max_nr_circles_line - 1 - last_length
            current_position = (40, current_height) if last_length == self.max_nr_circles_line else (60, current_height)
            elements = []
            for i in range(0, last_length):
                elements.append(EmptyElement(current_position))
                current_position = current_position[0] + 40, current_height
            self.board.append(elements)
            current_height += 35

    def provide_colors(self):
        colors = list(self.available_colors.keys())
        current_color_index = randrange(len(colors))
        next_color_index = randrange(len(colors))
        return {
            'current-color': table[colors[current_color_index]],
            'next-color': table[colors[next_color_index]]
        }

    def draw(self, window: Union[Surface, SurfaceType]):
        for level_line in self.board:
            for element in level_line:
                if isinstance(element, Circle):
                    element.draw(window)
