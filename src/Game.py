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


class GameController:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def select_game_mode(self):
        """ setup mode for player to choose """
        pass

    def play_game(self):
        pass

    def show_main_menu(self):
        """Show the main menu options for the game."""
        while True:
            print(
                """
     +-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+
     |S|C|I|S|S|O|R| |P|A|P|E|R| |R|O|C|K|
     +-+-+-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+
                """
            )
            print("""+ 1 + Show Leaderboard""")
            print("""+ 2 + Show Previous Game Results""")
            print("""+ 3 + Start a New Game""")
            print("""+ 4 + Exit """)

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.db_manager.print_leaderboard()
            elif choice == "2":
                self.db_manager.print_game_results()
            elif choice == "3":
                self.play_game()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please select a valid option.")
