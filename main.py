#!`which python`

from lib.game import Game
from lib.view.playboard_renderer import PlayboardRenderer

import time

START_PLAYER = "B"

if __name__ == "__main__":
    game = Game()
    playboard = PlayboardRenderer(game.PLAYERS.values())
    players = list(game.PLAYERS.keys())
    print(f"Players: {players}")

    current_player = START_PLAYER
    turn = 0

    while True:
        print(playboard.render())
        print(f"turn [{turn}]: Player {current_player}")
        game.PLAYERS[current_player].play()
        game.judge()
        turn += 1
        if current_player != "B": time.sleep(1)
        current_player = players[turn % len(players)]
