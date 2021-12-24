from circle import Circle
from empty_element import EmptyElement
from level import Level
from border import Border
from states.state import State
from pygame.surface import Surface, SurfaceType
from configs.states_config import NEXT_STATE
from status_area import StatusArea
from typing import Union
import colors
import pygame
import geometry


class GameInProgress(State):
    def __init__(self, window: Union[Surface, SurfaceType],
                 game_in_progress_config):
        super().__init__(window)

        self.borders = []
        self.additional_borders = []
        self.border_vertical_config = game_in_progress_config['border-vertical']
        self.border_horizontal_config = game_in_progress_config[
            'border-horizontal']

        self.min_group_length = game_in_progress_config['min-group-length']
        self.velocity = game_in_progress_config['velocity']
        self.levels_config = game_in_progress_config['levels']
        self.circle_config = game_in_progress_config['circle']
        self.status_area = StatusArea(game_in_progress_config['status-area'],
                                      self.window, self.circle_config)
        self.line_config = game_in_progress_config['line-config']
        self.is_shooting = False
        self.equation_line = dict()
        self.nr_throws = 0
        self.nr_throws_trigger = game_in_progress_config['nr-throws-trigger']
        self.x_ratio = 0.0
        self.y_ratio = 0.0
        self.__initialize_borders()
        self.__initialize_levels()
        self.colors = self.current_level.provide_colors()
        self.shooting_position = game_in_progress_config['shooting-position']
        self.shooting_circle = Circle(self.circle_config['radius'],
                                      self.shooting_position,
                                      colors.DEFAULT)
        self.set_colors()

    def set_colors(self):
        self.shooting_circle.color = self.colors['current-color']
        self.status_area.next_circle_text.next_circle.color = self.colors[
            'next-color']

    def __initialize_levels(self):
        self.levels = []
        for level_config in self.levels_config:
            self.levels.append(Level(level_config,
                                     self.window,
                                     self.circle_config['radius'],
                                     self.status_area,
                                     self.min_group_length))
        self.levels_iter = iter(self.levels)
        self.current_level = next(self.levels_iter)
        self.status_area.level_text.set_level(
            self.levels.index(self.current_level) + 1)

    def __initialize_borders(self):
        self.borders.append(Border((0, self.status_area.height),
                                   self.border_vertical_config, 'vertical',
                                   colors.GRAY))
        self.borders.append(Border((self.window.get_width() -
                                    self.border_vertical_config['width'],
                                    self.status_area.height),
                                   self.border_vertical_config, 'vertical',
                                   colors.GRAY))
        self.borders.append(Border((0, self.status_area.height),
                                   self.border_horizontal_config, 'horizontal',
                                   colors.GRAY))
        self.borders.append(Border((0, self.window.get_height() -
                                    self.border_horizontal_config['height']),
                                   self.border_horizontal_config, 'horizontal',
                                   colors.GRAY))

    def spawn_additional_border(self):
        nr_additional_borders = len(self.additional_borders)
        position = (0, self.status_area.height + (nr_additional_borders + 1) *
                    self.border_horizontal_config['height'])
        self.additional_borders.append(
            Border(position, self.border_horizontal_config, 'horizontal',
                   colors.GRAY))

    def draw_borders(self):
        for border in self.borders:
            border.draw(self.window)
        for border in self.additional_borders:
            border.draw(self.window)

    def draw_current_level(self):
        self.current_level.draw(self.window)

    def draw_line(self, first_point, second_point, color):
        pygame.draw.line(self.window, color, first_point, second_point)

    def next_throw(self):
        self.is_shooting = False
        self.__reset_ratios()
        self.colors['current-color'] = self.colors['next-color']
        self.colors['next-color'] = self.current_level.provide_next_color()
        self.set_colors()
        self.shooting_circle.position = self.shooting_position

    def circle_reaches_end_line(self):
        positions = self.current_level.board.keys()
        for position in positions:
            element = self.current_level.board[position]
            if isinstance(element, Circle) and position[1] + element.radius > \
                    self.line_config['first-position'][1]:
                return True
        return False

    def draw_state(self):

        self.initial_drawing()
        self.draw_borders()
        self.draw_current_level()
        self.status_area.draw(self.window)
        self.is_collision_with_borders()
        if self.current_level.detect_collision(self.shooting_circle):
            if self.current_level.is_board_clear():
                self.current_level = next(self.levels_iter)
                self.additional_borders = []
                self.status_area.level_text.set_level(
                    self.levels.index(self.current_level) + 1)
                self.colors = self.current_level.provide_colors()
                self.set_colors()
                self.next_throw()
                self.nr_throws = 0
            else:
                self.next_throw()
                self.nr_throws += 1
        if self.nr_throws == self.nr_throws_trigger:
            self.nr_throws = 0
            self.current_level.shift_board()
            self.spawn_additional_border()
        if self.circle_reaches_end_line():
            pygame.event.post(pygame.event.Event(NEXT_STATE))

        self.draw_line(self.line_config['first-position'],
                       self.line_config['second-position'],
                       self.line_config['color'])
        self.shooting_circle.draw(self.window)
        self.shoot_circle()

    def is_collision_with_borders(self):
        for border in self.borders + self.additional_borders:
            if border.rect_obj.colliderect(self.shooting_circle.rect_obj):
                self.shooting_circle.position = self.shooting_circle.position[
                                                    0] - self.x_ratio * self.velocity, \
                                                self.shooting_circle.position[
                                                    1] - self.y_ratio * self.velocity
                if border.orientation == 'vertical':
                    self.equation_line['slope'] *= (-1)
                    self.__determine_ratios()
                else:
                    empty_elements = self.current_level.get_base_elements(
                        EmptyElement)
                    empty_elements.sort(
                        key=lambda empty_element: geometry.get_distance(
                            empty_element.position,
                            self.shooting_circle.position))
                    position = empty_elements[0].position
                    self.current_level.board[position] = Circle(
                        self.shooting_circle.radius, position,
                        self.shooting_circle.color)
                    self.current_level.update_available_colors(
                        self.current_level.board[position], "add")
                    self.current_level.pop_circles(
                        self.current_level.board[position])
                    if self.current_level.is_board_clear():
                        self.current_level = next(self.levels_iter)
                        self.additional_borders = []
                        self.status_area.level_text.set_level(
                            self.levels.index(self.current_level) + 1)
                        self.colors = self.current_level.provide_colors()
                        self.set_colors()
                        self.next_throw()
                        self.nr_throws = 0
                    else:
                        self.next_throw()
                        self.nr_throws += 1
                break

    def shoot_circle(self):
        self.shooting_circle.position = self.shooting_circle.position[
                                            0] + self.x_ratio * self.velocity, \
                                        self.shooting_circle.position[
                                            1] + self.y_ratio * self.velocity
        self.shooting_circle.update_rect_position()

    def __determine_ratios(self):
        point = geometry.get_point_at_distance(self.shooting_circle.position,
                                               self.equation_line['slope'])
        self.x_ratio = point[0] - self.shooting_circle.position[0]
        self.y_ratio = point[1] - self.shooting_circle.position[1]

    def __reset_ratios(self):
        self.x_ratio = 0.0
        self.y_ratio = 0.0

    def is_valid(self, mouse_position):
        return mouse_position[1] < self.shooting_circle.position[1] - \
               2 * self.circle_config['radius']

    def listen_for_click(self, mouse_position):
        if not self.is_shooting and self.is_valid(mouse_position):
            self.equation_line = geometry.get_equation_line(
                self.shooting_circle.position, mouse_position)
            self.__determine_ratios()
            self.is_shooting = True
