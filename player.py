import random

DEFAULT_PEAS = 3
EXIT_CODE = "q"


class Player:
    def __init__(self, code: str, game: object, is_human: bool):
        self.CODE = code
        self.POTS: list[int] = [DEFAULT_PEAS, DEFAULT_PEAS, DEFAULT_PEAS]
        self.GOAL = 0
        self.GAME = game
        self.IS_HUMAN = is_human

    def render_playboard(self, PLAYBOARD: str) -> str:
        playboard = PLAYBOARD
        playboard = playboard.replace(
            f"{self.CODE}G", self.format_num(self.GOAL))
        pot_idx = 0
        for pot in self.POTS:
            playboard = playboard.replace(
                f"{self.CODE}{pot_idx}", self.format_num(pot))
            pot_idx += 1
        return playboard

    def format_num(self, num: int) -> str:
        '''Make sure number returns as a 2 dec string.'''
        if num < 10:
            return f"0{num}"
        return str(num)

    def play(self):
        if self.IS_HUMAN:
            step = self.get_step()
        else:
            step = self.get_rnd_step()
        self.play_handler(step)

    def get_step(self):
        """Get the pot to move from the user."""
        allowed_inputs = ['a', 's', 'd']
        message = f"Choose your step {allowed_inputs} ({EXIT_CODE} to quit): "
        step = input(message)
        if step == EXIT_CODE:
            exit("Bye!")
        if step not in allowed_inputs:
            print(
                f"Error: Unrecognised step: {step}. "
                "Please choose from {allowed_inputs}.")
        else:
            return allowed_inputs.index(step)

    def get_rnd_step(self) -> int:
        """Get a non-zero random step."""
        allowed_inputs = list(filter(
            lambda step: self.POTS[step] != 0, [0, 1, 2]))
        if len(allowed_inputs) == 1:
            idx = 0
        elif len(allowed_inputs) == 0:
            return 0
        else:
            idx = random.randrange(0, len(allowed_inputs) - 1)
        step = allowed_inputs[idx]
        return step

    def play_handler(self, step: int):
        pot_name = f"{self.CODE}{step}"
        num_of_peas = self.POTS[step]
        if num_of_peas == 0:
            print("No peas left. Please choose another pot.")
            return
        self.GAME.distribute_peas(num_of_peas, pot_name)
        self.POTS[step] = 0
