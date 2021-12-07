#!`which python`

from player import Player

MACHINE_PLAYER_CODE = "A"
HUMAN_PLAYER_CODE = "B"
START_PLAYER = "A"
SEQUENCE = ["A0", "A1", "A2", "AG", "B0", "B1", "B2", "BG"]
PLAYBOARD = "            *A*           \n"\
            "+----+----+----+----+----+\n"\
            "|    | A2 | A1 | A0 |    |\n"\
            "| AG |----+----+----| BG |\n"\
            "|    | B0 | B1 | B2 |    |\n"\
            "+----+----+----+----+----+\n"\
            "        |    |    |       \n"\
            "        a    s    d       \n"\
            "            *B*             "


class Game:
    def __init__(self):
        self.PLAYERS = {
            HUMAN_PLAYER_CODE: Player(HUMAN_PLAYER_CODE, self, is_human=True),
            MACHINE_PLAYER_CODE: Player(
                MACHINE_PLAYER_CODE, self, is_human=False)
        }

    def distribute_peas(self, num_of_peas: int, chosen_pot_name: str):
        """Distribute given number of peas to the preceding pots after the chosen pot."""
        chosen_pot_id = SEQUENCE.index(chosen_pot_name)
        for i in range(num_of_peas):
            rewarded_pot_id = (chosen_pot_id + (i + 1)) % len(SEQUENCE)
            [rewarded_player, rewarded_pot_name] = SEQUENCE[rewarded_pot_id]
            if rewarded_pot_name == "G":
                self.PLAYERS[rewarded_player].GOAL += 1
            else:
                self.PLAYERS[rewarded_player].POTS[int(rewarded_pot_name)] += 1

    def judge(self):
        if sum(self.PLAYERS[HUMAN_PLAYER_CODE].POTS) == 0 and \
                sum(self.PLAYERS[MACHINE_PLAYER_CODE].POTS) == 0:
            human_goal = self.PLAYERS[HUMAN_PLAYER_CODE].GOAL
            machine_goal = self.PLAYERS[MACHINE_PLAYER_CODE].GOAL
            if human_goal > machine_goal:
                exit(f"Player {HUMAN_PLAYER_CODE} WINS!")
            elif machine_goal > human_goal:
                exit(f"Player {MACHINE_PLAYER_CODE} WINS!")
            else:
                exit("DRAW!")

    def render_playboard(self) -> str:
        playboard = self.PLAYERS[HUMAN_PLAYER_CODE].render_playboard(PLAYBOARD)
        playboard = self.PLAYERS[MACHINE_PLAYER_CODE].render_playboard(
            playboard)
        return playboard


game = Game()

current_player = START_PLAYER
while True:
    print(game.render_playboard())
    game.PLAYERS[HUMAN_PLAYER_CODE].play()
    game.PLAYERS[MACHINE_PLAYER_CODE].play()
    game.judge()
