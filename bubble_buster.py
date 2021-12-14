import pygame
from config_loader import ConfigLoader
from states_provider import get_states_registry


class BubbleBuster:

    def __init__(self, file_name_game_config):
        pygame.init()
        pygame.font.init()

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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.active_state = next(self.possible_states_iter)
            self.states_registry[self.active_state].draw_state()
            pygame.display.update()
