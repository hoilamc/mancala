class PlayboardRenderer:
    def __init__(self, players: list):
        self.PLAYBOARD = \
            "                       A            \n"\
            "          +----+----+----+----+----+\n"\
            "          |    | A2 | A1 | A0 |    |\n"\
            "A GOAL >> | AG |----+----+----| BG | << B GOAL\n"\
            "          |    | B0 | B1 | B2 |    |\n"\
            "          +----+----+----+----+----+\n"\
            "                  |    |    |       \n"\
            "                  a    s    d       \n"\
            "                       B              "
        self.PLAYERS = players

    def render(self) -> str:
        playboard = self.PLAYBOARD
        for player in self.PLAYERS:
            playboard = self.render_player_part(player, playboard)
        return playboard

    def render_player_part(self, player, PLAYBOARD: str) -> str:
        """Render parts of the playboard that the player owns"""
        playboard = self.render_player_goal(player, PLAYBOARD)
        playboard = self.render_player_pots(player, playboard)
        return playboard

    def render_player_goal(self, player, PLAYBOARD) -> str:
        playboard = PLAYBOARD
        playboard = playboard.replace(
            f"{player.CODE}G", self.format_num(player.GOAL))
        return playboard

    def render_player_pots(self, player, PLAYBOARD) -> str:
        playboard = PLAYBOARD
        pot_idx = 0
        for pot in player.POTS:
            playboard = playboard.replace(
                f"{player.CODE}{pot_idx}", self.format_num(pot))
            pot_idx += 1
        return playboard

    def format_num(self, num: int) -> str:
        '''Make sure number returns as a 2 dec string.'''
        if num < 10:
            return f"0{num}"
        return str(num)
