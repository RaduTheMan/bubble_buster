from pygame import image
from shared.text import Text


class Button:
    def __init__(self, button_config):
        self.text_wrapper = Text(button_config['title'])
        self.action = button_config['action']
        self.background = image.load(button_config['background'])
        self.width = button_config['width']
        self.height = button_config['height']
        self.__create_button()

    def __create_button(self):
        x = self.width / 2 - self.text_wrapper.text.get_width() / 2
        y = self.height / 2 - self.text_wrapper.text.get_height() / 2
        self.background.blit(self.text_wrapper.text, (x, y))
