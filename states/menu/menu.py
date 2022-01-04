from pygame import image, transform
from pygame.surface import Surface, SurfaceType
import os
from typing import Union

from states.state import State
from states.menu.button import Button
from states.menu.buttons_layout import Layout

from shared.text import Text


class Menu(State):
    def __init__(self, window: Union[Surface, SurfaceType], menu_config):
        super().__init__(window)
        self.title = Text(menu_config['title'])
        self.title_image_config = menu_config['title-image']
        self.title_image = transform.scale(image.load
                                           (self.title_image_config['path']),
                                           (self.title_image_config['width'],
                                            self.title_image_config['height']))
        self.buttons = []
        buttons_config = menu_config['buttons']
        for button_config in buttons_config:
            self.buttons.append(Button(button_config))
        self.layout = Layout(self.buttons,
                             os.path.join('configs',
                                          'buttons_layout_config.json'),
                             self.window)

    def draw_state(self):
        self.initial_drawing()
        self.window.blit(self.title_image,
                         (self.window.get_width() / 2 -
                          self.title_image.get_width() / 2,
                          self.window.get_height() / 2 -
                          self.title_image.get_height() / 2 ))
        self.window.blit(self.title.text, (self.window.get_width() / 2 -
                                           self.title.text.get_width() / 2, 40))
        self.layout.draw_buttons()


