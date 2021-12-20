from circle import Circle
from border import Border
from states.state import State
from pygame.surface import Surface, SurfaceType
from typing import Union
import colors
import pygame
import geometry


class GameInProgress(State):
    def __init__(self, window: Union[Surface, SurfaceType],
                 game_in_progress_config):
        super().__init__(window)

        self.borders = []
        self.border_vertical_config = game_in_progress_config['border-vertical']
        self.border_horizontal_config = game_in_progress_config[
            'border-horizontal']
        self.velocity = game_in_progress_config['velocity']
        self.circle_config = game_in_progress_config['circle']
        self.shooting_circle = Circle(self.circle_config['radius'],
                                      (self.window.get_width() / 2,
                                       self.window.get_height() -
                                       2 * self.circle_config['radius']))
        self.is_shooting = False
        self.equation_line = dict()
        self.x_ratio = 0.0
        self.y_ratio = 0.0
        self.cntr = 0
        self.__initialize_borders()

    def __initialize_borders(self):
        self.borders.append(Border((0, 0),
                                   self.border_vertical_config, 'vertical', colors.GRAY))
        self.borders.append(Border((self.window.get_width() -
                                    self.border_vertical_config['width'], 0),
                                   self.border_vertical_config, 'vertical', colors.GRAY))
        self.borders.append(Border((0, 0),
                                   self.border_horizontal_config, 'horizontal', colors.GRAY))
        self.borders.append(Border((0,  self.window.get_height() -
                                    self.border_horizontal_config['height']),
                                   self.border_horizontal_config, 'horizontal', colors.GRAY))

    def draw_borders(self):
        for border in self.borders:
            border.draw(self.window)

    def draw_state(self):
        self.initial_drawing()
        self.draw_borders()
        self.is_collision_with_borders()
        pygame.draw.circle(self.window, colors.RED,
                           self.shooting_circle.position,
                           self.circle_config['radius'])
        self.shoot_circle()

    def is_collision_with_borders(self):
        for border in self.borders:
            if border.rect_obj.colliderect(self.shooting_circle.rect_obj):
                self.shooting_circle.position = self.shooting_circle.position[0] - self.x_ratio * self.velocity, \
                                                self.shooting_circle.position[1] - self.y_ratio * self.velocity
                if border.orientation == 'vertical':
                    self.equation_line['slope'] *= (-1)
                    self.__determine_ratios()
                else:
                    self.x_ratio = 0.0
                    self.y_ratio = 0.0
                break

    def shoot_circle(self):
        self.shooting_circle.position = self.shooting_circle.position[0] + self.x_ratio * self.velocity,\
                                        self.shooting_circle.position[1] + self.y_ratio * self.velocity
        self.shooting_circle.update_rect_position()

    def __determine_ratios(self):
        point = geometry.get_point_at_distance(self.shooting_circle.position,
                                               self.equation_line['slope'])
        self.x_ratio = point[0] - self.shooting_circle.position[0]
        self.y_ratio = point[1] - self.shooting_circle.position[1]

    def is_valid(self, mouse_position):
        return mouse_position[1] < self.shooting_circle.position[1]

    def listen_for_click(self, mouse_position):
        if not self.is_shooting and self.is_valid(mouse_position):
            self.equation_line = geometry.get_equation_line(self.shooting_circle.position, mouse_position)
            self.__determine_ratios()
            self.is_shooting = True


