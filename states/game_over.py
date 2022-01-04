from states.state import State
from pygame.surface import Surface, SurfaceType
from typing import Union
from score_text import ScoreText
from text import Text


class GameOver(State):
    def __init__(self, window: Union[Surface, SurfaceType],
                 game_over_config):
        super().__init__(window)
        self.messages = {
            'WON': "YOU WON",
            'LOST': "GAME OVER"
        }
        self.game_over_config = game_over_config
        self.final_score = ScoreText(game_over_config['score'], self.window.get_height(), self.window.get_width() / 2)
        self.verdict = Text(game_over_config['verdict'])

    def draw_state(self):
        self.initial_drawing()
        self.verdict.set_content(self.messages[self.received_data['verdict']])
        self.window.blit(self.verdict.text, (self.window.get_width() / 2 - self.verdict.text.get_width() / 2, self.final_score.position[1] - self.verdict.text.get_height() - 10))
        self.final_score.set_score(self.received_data['score'])
        y_score = self.final_score.position[1]
        self.final_score.position = (
        self.window.get_width() / 2 - self.final_score.text.get_width() / 2, y_score)
        self.final_score.draw(self.window)

