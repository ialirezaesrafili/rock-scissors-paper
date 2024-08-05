import os
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLAlchemy config
Base = declarative_base()
db_path = os.path.join(os.path.dirname(__file__), "game.sqlite")
engine = sa.create_engine(f"sqlite:///{db_path}")


class DatabaseManager:
    """Manage and interaction with SQL based on ORM"""
    pass


class GameResult(Base):
    """Creat table for log of player"""
    pass


class Player(Base):
    """Create tabel for showing score of each player """
    pass
