from states.state import State
from pygame.surface import Surface, SurfaceType
from typing import Union
import pygame


class GameInProgress(State):
    def __init__(self, window: Union[Surface, SurfaceType]):
        super().__init__(window)
        self.game_text = pygame.font.SysFont('comicsans', 40)\
            .render("Game in progress", True, (255, 255, 255))

    def draw_state(self):
        self.initial_drawing()
        self.window.blit(self.game_text, (10, 10))
