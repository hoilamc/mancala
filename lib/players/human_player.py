EXIT_CODE = "q"
ALLOWED_STEP_KEYS = ['a', 's', 'd']


class HumanPlayer:

    def get_input(self) -> str:
        """Gets a step from the human player."""
        message = f"Choose your step {ALLOWED_STEP_KEYS} ({EXIT_CODE} to quit): "
        step = input(message)
        if step == EXIT_CODE:
            exit("Bye!")
        return step

    def validate_step(self, step) -> bool:
        if step not in ALLOWED_STEP_KEYS:
            print(
                f"Error: Unrecognised step: {step}. "
                f"Please choose from {ALLOWED_STEP_KEYS}.")
            return False
        return True

    def get_step(self) -> int:
        """Get the pot to move from the user."""
        have_valid_input = False
        while not have_valid_input:
            step = self.get_input()
            if self.validate_step(step):
                return ALLOWED_STEP_KEYS.index(step)
