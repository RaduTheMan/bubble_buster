import pygame

from configs.config_loader import ConfigLoader
from configs.states_config import NEXT_STATE

from states.states_provider import get_states_registry


class BubbleBuster:

    def __init__(self, file_name_game_config):
        pygame.init()
        pygame.font.init()
        pygame.mouse.set_visible(True)

        self.game_config = ConfigLoader.load_config(file_name_game_config)
        self.window = pygame.display.set_mode((self.game_config['width'],
                                               self.game_config['height']))
        pygame.display.set_caption(self.game_config['caption'])
        self.possible_states = ['menu', 'game_in_progress', 'game_over']
        self.possible_states_iter = iter(self.possible_states)
        self.active_state = next(self.possible_states_iter)
        self.states_registry = get_states_registry(self.window)
        self.is_running = True

    def run_game(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.MOUSEMOTION:
                    mouse_position = pygame.mouse.get_pos()
                    if self.active_state == 'menu':
                        self.states_registry['menu']\
                            .layout\
                            .listen_for_mouse_movement(mouse_position)
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_position = pygame.mouse.get_pos()
                    if self.active_state == 'menu':
                        self.states_registry[self.active_state].layout\
                            .listen_for_click(mouse_position)
                    if self.active_state == 'game_in_progress':
                        self.states_registry[self.active_state]\
                            .listen_for_click(mouse_position)
                if event.type == NEXT_STATE:
                    next_state = next(self.possible_states_iter)
                    if self.states_registry[self.active_state].has_data_to_send:
                        self.states_registry[next_state].received_data = \
                            self.states_registry[self.active_state].send_data()
                    self.active_state = next_state
            self.states_registry[self.active_state].draw_state()
            pygame.display.update()
