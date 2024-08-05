# Database
import os
import sqlalchemy as sa

from src.DatabaseManager import DatabaseManager
from src.Game import GameController

db_path = os.path.join(os.path.dirname(__file__), "game.sqlite")
engine = sa.create_engine(f"sqlite:///{db_path}")


if __name__ == "__main__":
    db_manager = DatabaseManager(engine, db_path)
    game_controller = GameController(db_manager)
    game_controller.show_main_menu()

