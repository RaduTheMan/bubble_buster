import pygame
from pygame.surface import Surface, SurfaceType
from typing import Union


class Border:

    def __init__(self, position, border_config, orientation, color):
        self.rect_obj = pygame.Rect(position[0], position[1],
                                    border_config['width'],
                                    border_config['height'])
        self.orientation = orientation
        self.color = color

    def draw(self, window: Union[Surface, SurfaceType]):
        pygame.draw.rect(window, self.color, self.rect_obj)
