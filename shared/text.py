import pygame


class Text:
    """
    This class represents a basic text.
    """
    def __init__(self, text_config):
        self.text_config = text_config
        self.font = pygame.font.SysFont(text_config['font-type'],
                                        text_config['font-size'])
        self.text = self.font.render(text_config['text'],
                                     True, text_config['color'])

    def set_content(self, content):
        """

        :param content: The content which will overwrite the current text.
        :return:
        """
        self.text = self.font.render(content, True, self.text_config['color'])
