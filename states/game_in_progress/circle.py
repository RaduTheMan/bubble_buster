import pygame
from pygame.surface import Surface, SurfaceType
from typing import Union


class Circle:
    def __init__(self, radius, position, color):
        self.radius = radius
        self.position = position
        self.color = color
        self.rect_obj = pygame.Rect(position[0] - radius, position[1] - radius,
                                    2 * radius, 2 * radius)

    def draw(self, window: Union[Surface, SurfaceType]):
        pygame.draw.circle(window, self.color, self.position, self.radius)

    def update_rect_position(self):
        self.rect_obj.x = self.position[0] - self.radius
        self.rect_obj.y = self.position[1] - self.radius
