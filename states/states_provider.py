from pygame.surface import Surface, SurfaceType
from typing import Union

from configs.states_config import menu_config, \
    game_in_progress_config, game_over_config

from states.menu.menu import Menu
from states.game_in_progress.game_in_progress import GameInProgress
from states.game_over.game_over import GameOver


def get_states_registry(window: Union[Surface, SurfaceType]):
    states_registry = {
        'menu': Menu(window, menu_config),
        'game_in_progress': GameInProgress(window, game_in_progress_config),
        'game_over': GameOver(window, game_over_config)}
    return states_registry
