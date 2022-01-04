from pygame import image
from pygame.surface import Surface, SurfaceType
from typing import Union

from configs.states_config import state_config


class State:
    background = image.load(state_config['background'])

    def __init__(self, window: Union[Surface, SurfaceType]):
        self.window = window
        self.has_data_to_send = False
        self.received_data = None

    def initial_drawing(self):
        self.window.blit(self.background, (0, 0))

    def draw_state(self):
        pass
