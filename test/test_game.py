import pytest
from board import Board
from game import check_winner

@pytest.fixture
def board():
    return Board()

def test_check_winner_row(board):
    board.mark("a1", "X")
    board.mark("a2", "X")
    board.mark("a3", "X")
    assert check_winner(board, "X") == True

    board.reset()
    board.mark("b1", "O")
    board.mark("b2", "O")
    board.mark("b3", "O")
    assert check_winner(board, "O") == True

def test_check_winner_column(board):
    board.mark("a1", "X")
    board.mark("b1", "X")
    board.mark("c1", "X")
    assert check_winner(board, "X") == True

    board.reset()
    board.mark("a2", "O")
    board.mark("b2", "O")
    board.mark("c2", "O")
    assert check_winner(board, "O") == True

def test_check_winner_diagonal(board):
    board.mark("a1", "X")
    board.mark("b2", "X")
    board.mark("c3", "X")
    assert check_winner(board, "X") == True

    board.reset()
    board.mark("a3", "O")
    board.mark("b2", "O")
    board.mark("c1", "O")
    assert check_winner(board, "O") == True

def test_check_winner_no_winner(board):
    board.mark("a1", "X")
    board.mark("a2", "O")
    assert check_winner(board, "X") == False
    assert check_winner(board, "O") == False