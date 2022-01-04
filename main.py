import os
from bubble_buster import BubbleBuster

if __name__ == '__main__':
    game = BubbleBuster(os.path.join('configs', 'window-config.json'))
    game.run_game()
