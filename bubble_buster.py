import pygame
from config_loader import ConfigLoader


class BubbleBuster:

    def __init__(self, file_name_game_config):
        pygame.init()

        self.game_config = ConfigLoader.load_config(file_name_game_config)
        self.window = pygame.display.set_mode((self.game_config['width'],
                                               self.game_config['height']))
        self.is_running = True
        pygame.display.set_caption(self.game_config['caption'])

    def run_game(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            pygame.display.update()
