
# Rock, Paper, Scissors Game with Database Integration

## Overview

This repository contains a Rock, Paper, Scissors game implemented in Python with a SQLite database backend. The game tracks player scores and game results using SQLAlchemy for ORM (Object-Relational Mapping) and PrettyTable for displaying results in a tabular format.

## Features

- Track player scores and game results.
- Print leaderboard and previous game results.
- Play different game modes (Single Round, Best of Three, Best of Five, Best of Seven).
- Ensure the database schema is up-to-date.
- Add new players or update existing player scores.
- Display results in a readable table format using PrettyTable.

## Setup

### Prerequisites

- Python 3.x
- SQLite

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ialirezaesrafili/rock-scissors-paper.git
    ```

2. Install required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

The game uses a SQLite database named `game.sqlite` stored in the same directory as the script.

## Usage

To start the game, run the `main.py` script:

```bash
python main.py
```

Follow the on-screen prompts to navigate through the game options.

## Code Explanation

### Database Setup

#### `DatabaseManager` Class

Manages the database connection, checks if the database exists, creates tables, and provides methods for interacting with the database.

- **Attributes:**
  - `engine`: SQLAlchemy engine instance for connecting to the SQLite database.
  - `Session`: SQLAlchemy session maker bound to the engine.

- **Methods:**
  - `__init__(self, engine)`: Initializes the database engine and session. Calls `check_or_create_db` to ensure the database and schema are set up.
  - `check_or_create_db(self)`: Checks if the database file exists. If not, it creates a new one. Ensures the schema is up-to-date.
  - `add_game_result(self, player_name, opponent_name, winner_name)`: Adds a game result to the database.
  - `add_or_update_player(self, player_name)`: Adds a new player to the database or updates their score if they already exist.
  - `get_player_score(self, player_name)`: Retrieves the score of a specified player from the database.
  - `ensure_player_exists(self, player_name)`: Ensures a player exists in the database with a score of 0 if not present.
  - `print_leaderboard(self)`: Prints the leaderboard using PrettyTable.
  - `print_game_results(self)`: Prints previous game results using PrettyTable.

**Example Usage:**

```python
db_manager = DatabaseManager(engine)
db_manager.add_game_result("player", "opponents", "winner")
db_manager.add_or_update_player("player")
score = db_manager.get_player_score("player")
db_manager.print_leaderboard()
db_manager.print_game_results()
```

### Models

#### `GameResult` Class

Represents a game result with player names and the winner.

- **Attributes:**
  - `id`: Integer, primary key, auto-incremented.
  - `player_name`: String, name of the player.
  - `opponent_name`: String, name of the opponent.
  - `winner_name`: String, name of the winner.

**Example Usage:**

```python
result = GameResult(player_name="player1", opponent_name="player2", winner_name="player2")
```

#### `Player` Class

Represents a player with a unique name and score.

- **Attributes:**
  - `id`: Integer, primary key, auto-incremented.
  - `name`: String, name of the player, unique.
  - `score`: Integer, score of the player, default is 0.

**Example Usage:**

```python
player = Player(name="player", score=10)
```

### Game Logic

#### `PlayerInfo` Class

Stores information about a player, including their name, choice, and score.

- **Attributes:**
  - `player_name`: String, name of the player.
  - `player_choice`: String, choice of the player (Rock, Paper, Scissors).
  - `player_score`: Integer, score of the player.

- **Methods:**
  - `__init__(self, player_name: str, player_choice: str = None, player_score: int = 0)`: Initializes the player information.
  - `get_info(self) -> list`: Returns the player's name and choice as a list.
  - `get_choice(self)`: Returns the player's choice.
  - `set_choice(self, choice)`: Sets the player's choice.
  - `get_score(self)`: Returns the player's score.
  - `update_score(self)`: Increments the player's score by 1 and returns the updated score.

**Example Usage:**

```python
player_info = PlayerInfo(player_name="player1")
player_info.set_choice("Rock")
choice = player_info.get_choice()
score = player_info.update_score()
```

#### `Game` Class

Contains the logic for determining the winner of a Rock, Paper, Scissors game.

- **Attributes:**
  - `player`: PlayerInfo instance representing the player.
  - `opponent`: PlayerInfo instance representing the opponent.
  - `rules`: Dictionary defining the rules of the game.
  - `db_manager`: DatabaseManager instance for interacting with the database.

- **Methods:**
  - `__init__(self, player: PlayerInfo, opponent: PlayerInfo, db_manager: DatabaseManager)`: Initializes the game with two players and the game rules.
  - `determine_winner(self)`: Determines the winner based on the choices of the players.
  - `compare_choice(self)`: Compares the choices of the players, determines the winner, updates the database with the result, and updates the winner's score.

**Example Usage:**

```python
game = Game(player_info, opponent_info, db_manager)
winner = game.compare_choice()
```

#### `GameController` Class

Handles user interaction, game modes, and menu navigation.

- **Attributes:**
  - `db_manager`: DatabaseManager instance for interacting with the database.

- **Methods:**
  - `__init__(self, db_manager)`: Initializes the game controller with the database manager.
  - `select_game_mode(self)`: Prompts the user to select a game mode.
  - `show_main_menu(self)`: Displays the main menu options for the game.
  - `play_game(self)`: Handles the main game logic, including player prompts, game rounds, and updating scores.

**Example Usage:**

```python
game_controller = GameController(db_manager)
game_controller.show_main_menu()
```

### Main Script

The main script initializes the database manager and game controller, then displays the main menu.

**Example Script:**

```python
    if __name__ == "__main__":
        db_manager = DatabaseManager(engine, db_path)
        game_controller = GameController(db_manager)
        game_controller.show_main_menu()
```
