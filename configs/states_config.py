import os
import pygame
import colors
from configs.config_loader import ConfigLoader

NEXT_STATE = pygame.USEREVENT + 1
window_config = ConfigLoader.load_config(os.path.join('configs', 'window-config.json'))

state_config = {'background': os.path.join('Resources', 'background.png')}
menu_config = {
    'title': {
        'text': 'Bubble Buster',
        'font-size': 50,
        'font-type': 'comic-sans',
        'color': colors.WHITE
    },
    'title-image': {
        'path': os.path.join('Resources', 'pow.png'),
        'width': 500,
        'height': 374
    },
    'buttons': [
        {
            'title': {
                'text': 'Play',
                'font-size': 35,
                'font-type': 'comic-sans',
                'color': colors.WHITE
            },
            'action': lambda: pygame.event.post(pygame.event.Event(NEXT_STATE)),
            'background': os.path.join('Resources', 'play-game-background.png'),
            'width': 180,
            'height': 70
        },
        {
            'title': {
                'text': 'Quit',
                'font-size': 35,
                'font-type': 'comic-sans',
                'color': colors.WHITE
            },
            'action': lambda: pygame.event.post(pygame.event.Event(pygame.QUIT)),
            'background': os.path.join('Resources', 'quit-game-background.png'),
            'width': 180,
            'height': 70
        }
    ]
}

game_in_progress_config = {
    'circle': {
        'radius': 20
    },
    'velocity': 5,
    'border-vertical': {
        'width': 20,
        'height': window_config['height']
    },
    'border-horizontal': {
        'width': window_config['width'],
        'height': 20
    }
}
