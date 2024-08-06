class PlayerInfo:
    """create base class for player and opponents"""

    def __init__(self, player_name: str, player_choice: str = None, player_score: int = 0):
        self.player_name = player_name
        self.player_choice = player_choice
        self.player_score = player_score

    def get_info(self) -> list:
        return [self.player_name, self.player_choice]

    def get_choice(self):
        return self.player_choice

    def set_choice(self, choice):
        self.player_choice = choice

    def get_score(self):
        return self.player_score

    def update_score(self):
        self.player_score += 1
        return self.player_score
