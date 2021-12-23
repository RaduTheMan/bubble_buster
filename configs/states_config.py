import os
import pygame
import colors
from configs.config_loader import ConfigLoader

NEXT_STATE = pygame.USEREVENT + 1
window_config = ConfigLoader.load_config(
    os.path.join('configs', 'window-config.json'))

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
            'action': lambda: pygame.event.post(
                pygame.event.Event(pygame.QUIT)),
            'background': os.path.join('Resources', 'quit-game-background.png'),
            'width': 180,
            'height': 70
        }
    ]
}

game_in_progress_config = {
    'circle': {
        'radius': 20.0
    },
    'min-group-length': 3,
    'velocity': 20,
    'border-vertical': {
        'width': 20,
        'height': window_config['height']
    },
    'border-horizontal': {
        'width': window_config['width'],
        'height': 20
    },
    'line-padding': 10,
    'status-area': {
        'height': 50,
        'padding': 10,
        'score-config': {
            'text': 'Score: ',
            'font-size': 20,
            'font-type': 'comic-sans',
            'color': colors.WHITE
        },
        'level-config': {
            'text': 'Level ',
            'font-size': 20,
            'font-type': 'comic-sans',
            'color': colors.WHITE
        },
        'next-config': {
            'text': 'Next ',
            'font-size': 20,
            'font-type': 'comic-sans',
            'color': colors.WHITE
        }
    },
    'levels': [
        "GR,GR,GR,GR,GRY,GRY,GRY,GRY,R,R,R,R;"
        "GR,GR,GR,GRY,GRY,GRY,GRY,R,R,R,R;"
        "BL,BL,BL,-,BL,BL,BL,BL,-,BL,BL,BL;"
        "GR,GRY,R,-,GR,GRY,R,-,GR,GRY,R;"
        "BL,BL,BL,BL,-,BL,BL,-,BL,BL,BL,BL",

        "-,GR,GR,GR,GR,GR,GR,GR,GR,GR,GR,-;"
        "GR,-,GR,Y,Y,BL,Y,Y,GR,-,GR;"
        "-,-,Y,Y,Y,GRY,GRY,Y,Y,Y,-,-;"
        "-,-,-,Y,Y,BL,Y,Y,-,-,-;"
        "-,GR,-,-,GR,Y,Y,GR,-,-,GR,-;"
        "-,GR,GR,GR,GR,GR,GR,GR,GR,GR,-;"
        "BL,BL,-,BL,BL,-,BL,BL,-,BL,BL,-;"
        "-,GRY,GRY,-,GRY,GRY,-,GRY,GRY,-,GRY;"
        "BL,BL,-,BL,BL,-,BL,BL,-,BL,BL,-"
    ]
}

game_in_progress_config['shooting-position'] = (window_config['width'] / 2,
                                                window_config['height'] -
                                                2 * game_in_progress_config[
                                                    'circle']
                                                ['radius'])

game_in_progress_config['line-config'] = {
    'first-position': (
        game_in_progress_config['border-vertical']['width'] +
        game_in_progress_config['line-padding'],
        game_in_progress_config['shooting-position'][1] -
        2 * game_in_progress_config['circle']['radius']),
    'second-position': (window_config['width'] -
                        game_in_progress_config['border-vertical']['width'] -
                        game_in_progress_config['line-padding'],
                        game_in_progress_config['shooting-position'][1] -
                        2 * game_in_progress_config['circle']['radius']),
    'color': colors.BLACK
}
