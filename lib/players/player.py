from lib.players.human_player import HumanPlayer
from lib.players.machine_player import MachinePlayer

DEFAULT_PEAS = 3


class Player:
    def __init__(self, code: str, game: object, is_human: bool):
        self.CODE = code
        self.POTS: list[int] = [DEFAULT_PEAS, DEFAULT_PEAS, DEFAULT_PEAS]
        self.GOAL = 0
        self.GAME = game
        self.PLAYER = HumanPlayer() if is_human else MachinePlayer(self.POTS)

    def play(self):
        step = self.PLAYER.get_step()
        self.play_handler(step)

    def play_handler(self, step: int):
        pot_name = f"{self.CODE}{step}"
        num_of_peas = self.POTS[step]
        if num_of_peas == 0:
            print("No peas left. Please choose another pot.")
            return
        self.GAME.distribute_peas(num_of_peas, pot_name)
        self.POTS[step] = 0
