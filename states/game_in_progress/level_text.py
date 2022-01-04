from shared.text import Text


class LevelText(Text):

    def __init__(self, text_config, height, padding, window):
        super().__init__(text_config)
        self.content = self.text_config['text']
        self.set_level(0)
        self.__adjust_position(height, padding, window)

    def __adjust_position(self, height, padding, window):
        self.position = (
            window.get_width() - self.text.get_width() - padding,
            height / 2 - self.text.get_height() / 2)

    def set_level(self, level):
        self.text = self.font.render(self.content + str(level), True,
                                     self.text_config['color'])

    def draw(self, window):
        window.blit(self.text, self.position)
