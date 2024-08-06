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
    """Controlling entire game process"""

    def __init__(self, db_manager):
        self.db_manager = db_manager

    def select_game_mode(self):
        """ setup mode for player to choose """
        print("""+ 1 + Single Round """)
        print("""+ 2 + Best of Three """)
        print("""+ 3 + Best of Five """)
        print("""+ 4 + Best of Seven """)
        while True:
            try:
                mode = int(input("Enter the number of the mode: "))
                if mode in [m for m in range(1, 5)]:
                    return mode
                print("Invalid selection. Please choose a number between 1 and 4")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def play_game(self):
        player1_name = input("Enter the name of Player 1: ").capitalize()

        while True:
            player2_name = input("Enter the name of Player 2: ").capitalize()
            if player1_name != player2_name:
                break
            print("Player 2 name cannot be the same as Player 1. Please enter a different name.")

        # Ensure both players are in the database
        self.db_manager.ensure_player_exists(player1_name)
        self.db_manager.ensure_player_exists(player2_name)

        while True:
            mode = self.select_game_mode()
            rounds = {1: 1, 2: 3, 3: 5, 4: 7}[mode]
            player1 = PlayerInfo(player_name=player1_name, player_score=self.db_manager.get_player_score(player1_name))
            player2 = PlayerInfo(player_name=player2_name, player_score=self.db_manager.get_player_score(player2_name))

            player1_wins = 0
            player2_wins = 0
            for _ in range(rounds):
                # Prompt for player choices
                valid_choices = {"Rock", "Paper", "Scissors"}
                while True:
                    player1_choice = input(f"{player1_name}, enter your choice (Rock, Paper, Scissors): ").capitalize()
                    if player1_choice in valid_choices:
                        player1.set_choice(player1_choice)
                        break
                    print("Invalid choice. Please enter Rock, Paper, or Scissors.")

                while True:
                    player2_choice = input(f"{player2_name}, enter your choice (Rock, Paper, Scissors): ").capitalize()
                    if player2_choice in valid_choices:
                        player2.set_choice(player2_choice)
                        break
                    print("Invalid choice. Please enter Rock, Paper, or Scissors.")

                # Create a game
                game = Game(player1, player2, self.db_manager)

                # Play the game and get the result

                winner = game.compare_choice()
                print(f"The winner of this round is {winner}")

                if winner == player1_name:
                    player1_wins += 1
                elif winner == player2_name:
                    player2_wins += 1

                # Update scores
                player1_score = self.db_manager.get_player_score(player1_name)
                player2_score = self.db_manager.get_player_score(player2_name)

                print(f"{player1_name} score: {player1_score}")
                print(f"{player2_name} score: {player2_score}")

                if player1_wins > (rounds // 2) or player2_wins > (rounds // 2):
                    break

            if player1_wins > player2_wins:
                print(f"\n{player1_name} wins the match!")
            elif player2_wins > player1_wins:
                print(f"\n{player2_name} wins the match!")
            else:
                print("\nThe match is a tie!")

            # Ask if the player wants to play more
            while True:
                replay = input("\nDo you want to play more games? (yes/no): ").strip().lower()
                if replay in ["yes", "no"]:
                    break
                print("Invalid input. Please enter 'yes' or 'no'.")

            if replay == "no":
                self.db_manager.print_leaderboard()
                break

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
