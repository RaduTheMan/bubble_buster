from score_text import ScoreText
from level_text import LevelText
from next_circle_text import NextCircleText
import colors
from circle import Circle


class StatusArea:

    def __init__(self, status_area_config, window, circle_config):
        self.height = status_area_config['height']
        self.padding = status_area_config['padding']
        self.score_config = status_area_config['score-config']
        self.level_config = status_area_config['level-config']
        self.next_config = status_area_config['next-config']
        self.score_text = ScoreText(self.score_config, self.height, self.padding)
        self.level_text = LevelText(self.level_config, self.height, self.padding, window)
        self.next_circle = Circle(circle_config['radius'] * 3 / 4, (0, 0), colors.DEFAULT)
        self.next_circle_text = NextCircleText(self.next_config, self.height, self.score_text.position[0] + self.score_text.text.get_width(), self.level_text.position[0], self.next_circle)

    def draw(self, window):
        self.score_text.draw(window)
        self.next_circle_text.draw(window)
        self.level_text.draw(window)

