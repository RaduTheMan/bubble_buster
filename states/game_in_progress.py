from circle import Circle
from states.state import State
from pygame.surface import Surface, SurfaceType
from typing import Union
import colors
import pygame


class GameInProgress(State):
    def __init__(self, window: Union[Surface, SurfaceType],
                 game_in_progress_config):
        super().__init__(window)

        self.border_vertical_config = game_in_progress_config['border-vertical']
        self.border_horizontal_config = game_in_progress_config[
            'border-horizontal']
        self.circle_config = game_in_progress_config['circle']
        self.shooting_circle = Circle(self.circle_config['radius'])
        self.shooting_circle.position = (self.window.get_width() / 2,
                                         self.window.get_height() -
                                         2 * self.shooting_circle.radius)
        self.__initialize_borders()

    def __initialize_borders(self):
        self.border_vertical_rect_left = pygame.Rect(0, 0,
                                                     self.border_vertical_config[
                                                         'width'],
                                                     self.border_vertical_config[
                                                         'height'])
        self.border_vertical_rect_right = pygame.Rect(
            self.window.get_width() - self.border_vertical_config[
                'width'], 0,
            self.border_vertical_config[
                'width'],
            self.border_vertical_config[
                'height'])
        self.border_horizontal_top = pygame.Rect(0, 0, self.border_horizontal_config['width'], self.border_horizontal_config['height'])
        self.border_horizontal_bottom = \
            pygame.Rect(0,
                        self.window.get_height() -
                        self.border_horizontal_config['height'],
                        self.border_horizontal_config['width'],
                        self.border_horizontal_config['height'])

    def draw_borders(self):
        pygame.draw.rect(self.window, colors.GRAY,
                         self.border_vertical_rect_left)
        pygame.draw.rect(self.window, colors.GRAY,
                         self.border_vertical_rect_right)
        pygame.draw.rect(self.window, colors.GRAY, self.border_horizontal_top)
        pygame.draw.rect(self.window, colors.GRAY, self.border_horizontal_bottom)

    def draw_state(self):
        self.initial_drawing()
        self.draw_borders()
        pygame.draw.circle(self.window, (255, 0, 0),
                           self.shooting_circle.position, 20, 0)
