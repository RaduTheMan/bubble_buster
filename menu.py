from state import State
from pygame.surface import Surface, SurfaceType
from typing import Union
from text import Text


class Menu(State):
    def __init__(self, window: Union[Surface, SurfaceType], menu_config):
        super().__init__(window)
        self.title = Text(menu_config['title'])

    def draw_state(self):
        self.initial_drawing()
        self.window.blit(self.title.text, (self.window.get_width() / 2 -
                                           self.title.text.get_width() / 2, 10))
