from pygame.surface import Surface, SurfaceType
from menu import Menu
from game_in_progress import GameInProgress
from game_over import GameOver
from typing import Union


def get_states_registry(window: Union[Surface, SurfaceType]):
    states_registry = {'menu': Menu(window),
                       'game_in_progress': GameInProgress(window),
                       'game_over': GameOver(window)}
    return states_registry
