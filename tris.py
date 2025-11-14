import os


a1 = a2 = a3 = " "
b1 = b2 = b3 = " "
c1 = c2 = c3 = " "


def draw():
    board = [
        "    A   B   C ",
        "",
        f"1   {a1} | {b1} | {c1}",
        "   -----------",
        f"2   {a2} | {b2} | {c2}",
        "   -----------",
        f"3   {a3} | {b3} | {c3}",
        ""
    ]
    os.system("clear")
    for row in board:
        print(row)


def checkTris(move):
    if move == "a1":
        if a1 == a2 == a3:
            return True
        if a1 == b1 == c1:
            return True
        if a1 == b2 == c3:
            return True
    if move == "a2":
        if a1 == a2 == a3:
            return True
        if a2 == b2 == c2:
            return True
    if move == "a3":
        if a1 == a2 == a3:
            return True
        if a3 == b3 == c3:
            return True
        if a3 == b2 == c1:
            return True
    if move == "b1":
        if b1 == b2 == b3:
            return True
        if a1 == b1 == c1:
            return True
    if move == "b2":
        if b1 == b2 == b3:
            return True
        if a2 == b2 == c2:
            return True
        if a1 == b2 == c3:
            return True
        if a3 == b2 == c1:
            return True
    if move == "b3":
        if b1 == b2 == b3:
            return True
        if a3 == b3 == c3:
            return True
    if move == "c1":
        if c1 == c2 == c3:
            return True
        if a1 == b1 == c1:
            return True
        if c1 == b2 == a3:
            return True
    if move == "c2":
        if a2 == b2 == c2:
            return True
        if c1 == c2 == c3:
            return True
    if move == "c3":
        if a3 == b3 == c3:
            return True
        if c1 == c2 == c3:
            return True
        if a1 == b2 == c3:
            return True
    return False


draw()


player = "X"
turn = 1
while turn <= 9:
    move = input(f"{player} inserisci casella: ")
    if move == "a1" and a1 == " ":
        a1 = player
        turn = turn + 1
    elif move == "a2" and a2 == " ":
        a2 = player
        turn = turn + 1
    elif move == "a3" and a3 == " ":
        a3 = player
        turn = turn + 1
    elif move == "b1" and b1 == " ":
        b1 = player
        turn = turn + 1
    elif move == "b2" and b2 == " ":
        b2 = player
        turn = turn + 1
    elif move == "b3" and b3 == " ":
        b3 = player
        turn = turn + 1
    elif move == "c1" and c1 == " ":
        c1 = player
        turn = turn + 1
    elif move == "c2" and c2 == " ":
        c2 = player
        turn = turn + 1
    elif move == "c3" and c3 == " ":
        c3 = player
        turn = turn + 1
    else:
        continue
    draw()
    if checkTris(move):
        print(f"{player} ha vinto!")
        exit(0)

    if player == "X":
        player = "O"
    else:
        player = "X"


print("pareggio!")
