import os
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLAlchemy config
Base = declarative_base()
db_path = os.path.join(os.path.dirname(__file__), "game.sqlite")
engine = sa.create_engine(f"sqlite:///{db_path}")


class DatabaseManager:
    """Manage and interaction with SQL based on ORM"""

    def __init__(self, engine):
        self.engine = engine
        self.Session = sessionmaker(bind=self.engine)
        self.check_or_create_db()

    def check_or_create_db(self):
        """Check if database exists, and create it if it does not."""
        if not os.path.exists(db_path):
            print("Database does not exist. Creating a new one.")
            Base.metadata.create_all(self.engine)
        else:
            print("Database already exists. Ensuring schema is up-to-date.")
            Base.metadata.create_all(self.engine)

    def ensure_player_exists(self, player_name):
        """Ensure a player exists in the database with a score of 0 if not present."""
        with self.Session() as session:
            player = session.query(Player).filter_by(name=player_name).first()
            if not player:
                player = Player(name=player_name, score=0)
                session.add(player)
                session.commit()

    def get_player_score(self, player_name):
        """Get the player's score from the database."""
        with self.Session() as session:
            player = session.query(Player).filter_by(name=player_name).first()
            if player:
                return player.score
            return 0


class GameResult(Base):
    """Creat table for log of player"""
    __tablename__ = 'game_results'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    player_name = sa.Column(sa.String, nullable=False)
    opponent_name = sa.Column(sa.String, nullable=False)
    winner_name = sa.Column(sa.String, nullable=False)

    def __repr__(self):
        return (f"<GameResult(player_name={self.player_name}, "
                f"opponent_name={self.opponent_name}, winner_name={self.winner_name})>")


class Player(Base):
    """Create tabel for showing score of each player """
    __tablename__ = 'players'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False, unique=True)
    score = sa.Column(sa.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Player(name={self.name}, score={self.score})>"
