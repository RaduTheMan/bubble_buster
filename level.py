from pygame.surface import Surface, SurfaceType
from typing import Union
from circle import Circle
from empty_element import EmptyElement
from colors import table


class Level:

    def __init__(self, level_config: str, window: Union[Surface, SurfaceType], radius):
        level_lines = level_config.split(';')
        self.level_lines = [level_line.split(',') for level_line in level_lines]
        self.max_nr_circles_line = len(self.level_lines[0])
        self.available_width = window.get_height() - 5 * radius
        self.radius = radius
        self.__build_board()

    def __build_board(self):
        # TO CHANGE FROM HARDCODED VALUES INTO PROPER VARIABLES
        self.board = []
        current_height = 40
        for level_line in self.level_lines:
            current_position = (40, current_height) if len(level_line) == self.max_nr_circles_line else (60, current_height)
            elements = []
            for color in level_line:
                if color in table.keys():
                    elements.append(Circle(self.radius, current_position, table[color]))
                else:
                    elements.append(EmptyElement(current_position))
                current_position = current_position[0] + 40, current_height
            self.board.append(elements)
            current_height += 35
        while current_height <= self.available_width:
            current_height += 35
            pass

    def draw(self, window: Union[Surface, SurfaceType]):
        for level_line in self.board:
            for element in level_line:
                if isinstance(element, Circle):
                    element.draw(window)
