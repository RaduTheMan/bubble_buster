import os
import pygame
import colors

NEXT_STATE = pygame.USEREVENT + 1

state_config = {'background': os.path.join('Resources', 'background.png')}
menu_config = {
    'title': {
        'text': 'Bubble Buster',
        'font-size': 50,
        'font-type': 'comic-sans',
        'color': colors.WHITE
    },
    'buttons': [
        {
            'title': {
                'text': 'Play',
                'font-size': 16,
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
                'font-size': 16,
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
