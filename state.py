from state_config import state_config
from pygame.surface import Surface, SurfaceType
from pygame import image
from typing import Union


class State:
    background = image.load(state_config['background'])

    def __init__(self, window: Union[Surface, SurfaceType]):
        self.window = window

    def initial_drawing(self):
        self.window.blit(self.background, (0, 0))

    def draw_state(self):
        pass
