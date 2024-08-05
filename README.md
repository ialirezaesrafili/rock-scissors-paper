# rock-scissors-paper
This "Rock, Paper, Scissors" game is a Python console app using SQLAlchemy for ORM


## PlayerInfo Class

---

The `PlayerInfo` class manages player data in the game. 

### Attributes
- **`player_name`** (str): The name of the player.
- **`player_choice`** (str, optional): The choice made by the player (default is `None`).
- **`player_score`** (int, default is `0`): The score of the player.

### Methods
- **`get_info()`**: Returns a list with the player's name, choice, and score.
- **`get_choice()`**: Retrieves the current choice of the player.
- **`set_choice(choice)`**: Sets the player's choice to the specified value.
- **`get_score()`**: Retrieves the player's score.
- **`update_score()`**: Updates the player's score based on the game's logic.
