import random

ALLOWED_STEP_KEYS = [0, 1, 2]


class MachinePlayer:

    def __init__(self, pots: list):
        self.POTS = pots

    def rnd_think(self, valid_steps: list) -> int:
        """Get a step randomly."""
        if len(valid_steps) == 1:
            idx = 0
        else:
            max_step_idx = len(valid_steps) - 1
            idx = random.randrange(0, max_step_idx)
        return valid_steps[idx]

    def get_step(self) -> int:
        """Get the step to move by thinking carefully."""
        valid_steps = list(filter(
            lambda step: self.POTS[step] != 0, ALLOWED_STEP_KEYS))
        if len(valid_steps) == 0:
            return 0
        step = self.rnd_think(valid_steps)
        return step
