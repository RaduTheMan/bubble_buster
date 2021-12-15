from bubble_buster import BubbleBuster
import os

if __name__ == '__main__':
    game = BubbleBuster(os.path.join('configs', 'game-config.json'))
    game.run_game()
