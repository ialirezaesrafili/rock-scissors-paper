from src import DatabaseManager
from src.Player import PlayerInfo


class Game:
    """Game class provides the instance for playing """

    def __init__(self, player: PlayerInfo, opponent: PlayerInfo, db_manager: DatabaseManager):
        self.player = player
        self.opponent = opponent
        self.rules = {
            "Rock": "Scissors",
            "Paper": "Rock",
            "Scissors": "Paper"
        }
        self.db_manager = db_manager

    def determine_winner(self):
        """
        checking which player name is winner
        meanwhile if they have same input return Tie
        """
        player_choice = self.player.get_choice()
        opponent_choice = self.opponent.get_choice()

        if player_choice == opponent_choice:
            return "Tie"
        if self.rules[player_choice] == opponent_choice:
            return self.player.player_name
        return self.opponent.player_name

    def compare_choice(self):
        """
        compare the choices between each player
        and using the determine_winner method then save it in DB
        """
        winner = self.determine_winner()

        # Save the game result
        self.db_manager.add_game_result(self.player.player_name, self.opponent.player_name, winner)

        # Ensure both players are in the database
        self.db_manager.ensure_player_exists(self.player.player_name)
        self.db_manager.ensure_player_exists(self.opponent.player_name)

        # Update the winner's score in the players table
        if winner != "Tie":
            self.db_manager.add_or_update_player(winner)
