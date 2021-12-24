import pygame
from pygame.surface import Surface, SurfaceType
import random
from typing import Union

import colors
import geometry
from circle import Circle
from empty_element import EmptyElement
from colors import table
from lee import Lee
from neighbour_conditions import is_neighbour_same_color, is_neighbour_circle
from status_area import calculate_score


class Level:

    def __init__(self, level_config: str, window: Union[Surface, SurfaceType], radius, status_area, min_group_length):
        level_lines = level_config.split(';')
        self.level_lines = [level_line.split(',') for level_line in level_lines]
        self.max_nr_circles_line = len(self.level_lines[0])
        self.available_width = window.get_height() - 5 * radius
        self.available_colors = dict()
        self.min_group_length = min_group_length
        self.radius = radius
        self.status_area = status_area
        self.directions = [(-self.radius, -(2 * self.radius - 5)), (self.radius, -(2 * self.radius - 5)), (2 * self.radius, 0), (self.radius, 2 * self.radius - 5),
                           (-self.radius, 2 * self.radius - 5), (-2 * self.radius, 0)]
        self.board = dict()
        self.__build_board()

    def __build_board(self):
        current_height = self.status_area.height + 2 * self.radius
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

        while current_height <= self.available_width + 2 * self.radius - 5:
            last_length = 2 * self.max_nr_circles_line - 1 - last_length
            current_position = (2 * self.radius, current_height) if last_length == self.max_nr_circles_line else (3 * self.radius, current_height)
            for i in range(0, last_length):
                self.board[current_position] = EmptyElement(current_position)
                current_position = current_position[0] + 2 * self.radius, current_height
            current_height += 2 * self.radius - 5

    def shift_board(self):
        new_board = dict()
        for key, value in self.board.items():
            key = key[0], key[1] + self.radius
            if isinstance(value, Circle):
                new_board[key] = Circle(value.radius, key, value.color)
            else:
                new_board[key] = EmptyElement(key)
        self.board = new_board

    def is_board_clear(self):
        return len(self.available_colors) == 0

    def get_base_elements(self, type_element):
        positions = list(self.board.keys())
        positions.sort(key=lambda position: position[1])
        min_height = positions[0][1]
        base_positions = [position for position in positions if position[1] == min_height]
        base_elements = []
        for base_position in base_positions:
            element = self.board[base_position]
            if isinstance(element, type_element):
                base_elements.append(element)
        return base_elements

    def get_front_elements(self, type_element):
        positions = list(self.board.keys())
        positions.sort(key=lambda position: position[1], reverse=True)
        max_height = positions[0][1]
        front_positions = [position for position in positions if position[1] == max_height]
        front_elements = []
        for front_position in front_positions:
            element = self.board[front_position]
            if isinstance(element, type_element):
                front_elements.append(element)
        return front_elements

    def update_available_colors(self, circle, method):
        color_code = colors.get_color_code(circle.color)
        if method == "remove":
            self.available_colors[color_code] -= 1
        elif method == "add":
            if color_code in self.available_colors.keys():
                self.available_colors[color_code] += 1
            else:
                self.available_colors[color_code] = 1
        if self.available_colors[color_code] == 0:
            self.available_colors.pop(color_code)

    def provide_colors(self):
        colors = list(self.available_colors.keys())
        current_color_index = random.randint(0, len(colors) - 1)
        next_color_index = random.randint(0, len(colors) - 1)
        return {
            'current-color': table[colors[current_color_index]],
            'next-color': table[colors[next_color_index]]
        }

    def provide_next_color(self):
        colors = list(self.available_colors.keys())
        next_color_index = random.randint(0, len(colors) - 1)
        return table[colors[next_color_index]]

    def __get_position_shot_circle(self, collision_position, shooting_circle):
        neighbours_positions = [
            (collision_position[0] + direction[0],
             collision_position[1] + direction[1]) for
            direction in self.directions]
        neighbours_valid_positions = [neighbour_position for neighbour_position
                                      in neighbours_positions if
                                      neighbour_position in self.board.keys()]
        neighbours = [self.board[neighbour_valid_position] for
                      neighbour_valid_position in neighbours_valid_positions]
        empty_neighbours = [neighbour for neighbour in neighbours if
                            isinstance(neighbour, EmptyElement)]
        empty_neighbours.sort(
            key=lambda neighbour: geometry.get_distance(neighbour.position,
                                                        shooting_circle.position))
        element_to_update = empty_neighbours[0]
        self.board[element_to_update.position] = Circle(shooting_circle.radius,
                                                        element_to_update.position,
                                                        shooting_circle.color)
        return element_to_update.position

    def pop_circles(self, starting_circle):
        algorithm = Lee(self.board, [starting_circle],
                        self.directions, is_neighbour_same_color)
        algorithm.run()
        to_pop_circles = algorithm.visited
        nr_circles_popped = 0
        if len(to_pop_circles) >= self.min_group_length:
            nr_circles_popped += len(to_pop_circles)
            for circle_position in to_pop_circles.keys():
                self.update_available_colors(self.board[circle_position], "remove")
                self.board[circle_position] = EmptyElement(circle_position)
            base_circles = self.get_base_elements(Circle)
            algorithm = Lee(self.board, base_circles,
                        self.directions, is_neighbour_circle)
            algorithm.run()
            for key, value in self.board.items():
                if isinstance(value, Circle) and key not in algorithm.visited.keys():
                    self.update_available_colors(value, "remove")
                    nr_circles_popped += 1
                    self.board[value.position] = EmptyElement(value.position)
        current_throw_score = calculate_score(nr_circles_popped)
        self.status_area.score_text.add_score(current_throw_score)

    def update_board(self, collision_position, shooting_circle):
        starting_circle_position = self.__get_position_shot_circle(
            collision_position, shooting_circle)
        starting_circle = self.board[starting_circle_position]
        self.update_available_colors(starting_circle, "add")
        self.pop_circles(starting_circle)

    def detect_collision(self, shooting_circle):
        positions = list(self.board.keys())
        for position in positions:
            if isinstance(self.board[position], Circle):
                if geometry.get_distance(position, shooting_circle.position) <= self.board[position].radius + shooting_circle.radius:
                    self.update_board(position, shooting_circle)
                    return True
        return False

    def draw(self, window: Union[Surface, SurfaceType]):
        positions = list(self.board.keys())
        for position in positions:
            if isinstance(self.board[position], Circle):
                self.board[position].draw(window)
