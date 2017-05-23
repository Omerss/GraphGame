import os

from GameHandler import GameHandler


game = GameHandler()
game.run_single_game(None, "{}\GraphsData\config.ini".format(os.getcwd()))
