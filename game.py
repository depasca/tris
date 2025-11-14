import os
from board import Board


def check_winner(board, symbol: str) -> bool:
    winning_combinations_ind = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in winning_combinations_ind:
        if all(board.board[i] == symbol for i in combo):
            return True
    return False

def play():
    board = Board()
    player = "X"
    turn = 1
    while turn <= 9:
        os.system("clear")
        print(board)
        move = input(f"{player} place your mark: ")
        board.mark(move, player)
        os.system("clear")
        print(board)
        if check_winner(board, player):
            print(f"{player} wins!")
            return
        player = "O" if player == "X" else "X"
        turn += 1
    print("It's a draw!")

    
def test_board_winner():
    board = Board()
    board.mark("a1", "X")
    board.mark("a2", "X")
    board.mark("a3", "X")
    check = check_winner(board, "X")  # Should return True
    print("X wins:", check)
    
if __name__ == "__main__":
    play()
    # test_board_winner()