from buttons_layout import Layout
from states.state import State
from pygame.surface import Surface, SurfaceType
from pygame import image, transform
from typing import Union
from text import Text
from button import Button


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
                             'buttons_layout_config.json',
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

    def listen_for_click(self, mouse_position):
        self.layout.listen_for_click(mouse_position)

