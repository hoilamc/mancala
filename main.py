#!`which python`

from lib.game import Game
from lib.view.playboard_renderer import PlayboardRenderer

import time
import textwrap
import math

START_PLAYER = "B"
GREETINGS = """
~~~~~~~~~~~~~~~~~~~~~HELLO~~~~~~~~~~~~~~~~~~~~~
Greetings! Thank you for playing with me.
I will be player A, and you will be player B.

How to play?
There will be a board with numbers indicating
the number of stones in the cell. Like this:

{}

Choose a cell by typing "a", "s" or "d" to
move the stones inside. Each of them will go to
the preceding cells accordingly.

The one who collects the most number of stones
in the goal wins.

You can press enter to start now!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

if __name__ == "__main__":
    game = Game()
    playboard = PlayboardRenderer(game.PLAYERS.values())
    players = list(game.PLAYERS.keys())

    input(GREETINGS.format(playboard.PLAYBOARD))

    current_player = START_PLAYER
    turn = 0

    while True:
        print(textwrap.dedent(f"""\
        ======================================
        turn [{math.floor(turn/2)}]: Player {current_player}
        ======================================
        """))
        print(playboard.render())
        game.PLAYERS[current_player].play()
        game.judge()
        turn += 1
        if current_player != "B":
            time.sleep(1)
        current_player = players[turn % len(players)]
