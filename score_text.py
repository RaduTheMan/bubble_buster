from text import Text


class ScoreText(Text):

    def __init__(self, text_config, height, padding):
        super().__init__(text_config)
        self.content = self.text_config['text']
        self.__adjust_position(height, padding)
        self.value = 0
        self.add_score(self.value)

    def __adjust_position(self, height, padding):
        self.position = (padding, height / 2 - self.text.get_height() / 2)

    def add_score(self, score):
        self.value += score
        self.text = self.font.render(self.content + str(self.value), True,
                                     self.text_config['color'])

    def draw(self, window):
        window.blit(self.text, self.position)
