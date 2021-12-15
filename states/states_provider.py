from pygame.surface import Surface, SurfaceType
from configs.states_config import menu_config
from states.menu import Menu
from states.game_in_progress import GameInProgress
from states.game_over import GameOver
from typing import Union


def get_states_registry(window: Union[Surface, SurfaceType]):
    states_registry = {'menu': Menu(window, menu_config),
                       'game_in_progress': GameInProgress(window),
                       'game_over': GameOver(window)}
    return states_registry
