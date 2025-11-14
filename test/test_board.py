import pytest
from board import Board

@pytest.fixture
def board():
    return Board()

def test_initial_board_state(board):
    assert board.board == [" "] * 9

def test_reset_board(board):
    board.mark("a1", "X")
    board.reset()
    assert board.board == [" "] * 9

def test_mark_valid_position(board):
    assert board.mark("a1", "X")
    assert board.board[0] == "X"

def test_mark_invalid_position(board):
    with pytest.raises(ValueError) as cm:
        board.mark("z9", "X")
    assert str(cm.value) == "Invalid position"

def test_mark_taken_position(board):
    board.mark("a1", "X")
    with pytest.raises(ValueError) as cm:
        board.mark("a1", "O")
    assert str(cm.value) == "Position already taken"

def test_compact_str(board):
    board.mark("a1", "X")
    board.mark("b2", "O")
    assert board.compact_str() == "X   O    "

def test_str_representation(board):
    board.mark("a1", "X"); board.mark("a2", "O"); board.mark("a3", "X")
    board.mark("b1", "O"); board.mark("b2", "X"); board.mark("b3", "O")
    board.mark("c1", "X"); board.mark("c2", "O"); board.mark("c3", "X")
    expected_str = "X | O | X\n--+---+--\nO | X | O\n--+---+--\nX | O | X"
    assert str(board) == expected_str