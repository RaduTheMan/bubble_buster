from state import State
from pygame.surface import Surface, SurfaceType
from typing import Union


class GameOver(State):
    def __init__(self, window: Union[Surface, SurfaceType]):
        super().__init__(window)

    def draw_state(self):
        self.initial_drawing()
