# Tris

Educational: a simple command-line Tic-Tac-Toe game in Python to introduce coding to kids. 

## Features

- Two-player gameplay (X and O)
- 3x3 grid with labeled columns (A, B, C) and rows (1, 2, 3)
- Win detection for rows, columns, and diagonals
- Draw detection
- Quit option during gameplay

## Usage

```bash
python game.py
```

Enter your move using the position format: `a1`, `b2`, `c3`, etc.
Type `quit` to exit the game.

## Project Structure

- `board.py` - Board class managing game state
- `game.py` - Game logic and player interaction
- `test/` - Unit tests

## Requirements

Python 3.6+
