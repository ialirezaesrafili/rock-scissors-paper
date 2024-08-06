
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
    git clone https://github.com/yourusername/rock-paper-scissors-game.git
    cd rock-paper-scissors-game
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
