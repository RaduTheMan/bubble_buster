from text import Text
from circle import Circle


class NextCircleText(Text):

    def __init__(self, text_config, height, lower_width, uppper_width, next_circle):
        super().__init__(text_config)
        self.next_circle = next_circle
        self.__adjust_position(height, lower_width, uppper_width)

    def __adjust_position(self, height ,lower_width, upper_width):
        x = (lower_width + upper_width) / 2 - (self.text.get_width() + 2 * self.next_circle.radius) / 2
        y = height / 2 - self.text.get_height() / 2
        self.position = (x, y)
        self.next_circle.position = (x + self.text.get_width() + self.next_circle.radius, height / 2)
        self.next_circle.update_rect_position()

    def draw(self, window):
        window.blit(self.text, self.position)
        self.next_circle.draw(window)

