class PlayerInfo:
    def __init__(self, player_name: str, player_choice: str = None, player_score: int = 0):
        self.player_name = player_name
        self.player_choice = player_choice
        self.player_score = player_score

    def get_info(self) -> list:
        pass

    def get_choice(self):
        pass

    def set_choice(self, choice):
        pass

    def get_score(self):
        pass

    def update_score(self):
        pass
