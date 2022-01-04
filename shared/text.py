import pygame


class Text:
    def __init__(self, text_config):
        self.text_config = text_config
        self.font = pygame.font.SysFont(text_config['font-type'],
                                        text_config['font-size'])
        self.text = self.font.render(text_config['text'],
                                     True, text_config['color'])

    def set_content(self, content):
        self.text = self.font.render(content, True, self.text_config['color'])
