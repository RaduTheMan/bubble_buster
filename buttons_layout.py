from configs.config_loader import ConfigLoader
from pygame.surface import Surface, SurfaceType
from typing import Union


class Layout:
    def __init__(self, buttons, file_name_layout_config,
                 window: Union[Surface, SurfaceType]):
        self.layout_config = ConfigLoader.load_config(file_name_layout_config)
        self.buttons = buttons
        self.drawed_buttons_rects = []
        self.window = window

    def draw_buttons(self):
        nr_buttons = len(self.buttons)
        x = self.window.get_width() / 2 - self.buttons[0].background.get_width() / 2
        y = self.window.get_height() / 2 - self.buttons[0].background.get_height() / 2
        first_position = (x, y)
        self.drawed_buttons_rects = []
        self.drawed_buttons_rects.append(self.window.blit(self.buttons[0].background, first_position))
        for i in range(1, nr_buttons):
            button = self.buttons[i]
            x = self.window.get_width() / 2 - button.background.get_width() / 2
            y = y + self.buttons[i-1].background.get_height() + \
                self.layout_config['distance-between-buttons']
            self.drawed_buttons_rects.append(self.window.blit(button.background, (x, y)))

    def listen_for_click(self, mouse_position):
        for drawed_button_rect, button in zip(self.drawed_buttons_rects, self.buttons):
            if drawed_button_rect.collidepoint(mouse_position):
                button.action()


