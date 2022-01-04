from shared.text import Text


class ScoreText(Text):
    """
    This class represents a text with a score value.
    It extends the base Text class.
    """

    def __init__(self, text_config, height, padding):
        super().__init__(text_config)
        self.content = self.text_config['text']
        self.__adjust_position(height, padding)
        self.value = 0
        self.add_score(self.value)

    def __adjust_position(self, height, padding):
        """

        :param height: the height of the area in which the text will be
        drawn
        :param padding: left padding value
        :return:
        """
        self.position = (padding, height / 2 - self.text.get_height() / 2)

    def add_score(self, score):
        """

        :param score: The score which will be added into the current score
        :return:
        """
        self.value += score
        self.text = self.font.render(self.content + str(self.value), True,
                                     self.text_config['color'])

    def set_score(self, score):
        """

        :param score: The new score which will overwrite the current score
        :return:
        """
        self.value = score
        self.text = self.font.render(self.content + str(self.value), True,
                                     self.text_config['color'])

    def draw(self, window):
        """
        This method will draw the text into the window.

        :param window: The main window of the game
        :return:
        """
        window.blit(self.text, self.position)
