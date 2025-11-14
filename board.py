class Board:
    board = []
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [" "] * 9

    def mark(self, position: str, symbol: str) -> bool:
        positions = {
            "a1": 0, "a2": 1, "a3": 2,
            "b1": 3, "b2": 4, "b3": 5,
            "c1": 6, "c2": 7, "c3": 8
        }
        if position in positions:
            if self.board[positions[position]] != " ":
                raise ValueError("Position already taken")
            self.board[positions[position]] = symbol
            return True
        raise ValueError("Invalid position")
    
    def compact_str(self) -> str:
        return ''.join(self.board)

    def __str__(self) -> str:
        return f"{self.board[0]} | {self.board[1]} | {self.board[2]}\n" \
               f"--+---+--\n" \
               f"{self.board[3]} | {self.board[4]} | {self.board[5]}\n" \
               f"--+---+--\n" \
               f"{self.board[6]} | {self.board[7]} | {self.board[8]}"


if __name__ == "__main__":
    b = Board()
    b.mark("a1", "X")
    b.mark("a2", "O")
    b.mark("a3", "X")
    b.mark("b1", "O")
    b.mark("b2", "X")
    b.mark("b3", "O")
    b.mark("c1", "X")
    b.mark("c2", "O")
    b.mark("c3", "X")
    print(b)