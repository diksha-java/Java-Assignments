board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(board[i * 3] + " | " + board[i * 3 + 1] + " | " + board[i * 3 + 2])
        if i < 2:
            print("--+---+--")

def check_winner(player):
    win = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for a, b, c in win:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_full():
    return " " not in board

player = "X"

while True:
    print_board()

    try:
        move = int(input(f"Player {player}, enter position (1-9): ")) - 1

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move!")
            continue

        board[move] = player

        if check_winner(player):
            print_board()
            print("Player", player, "wins!")
            break

        if is_full():
            print_board()
            print("Match Draw!")
            break

        player = "O" if player == "X" else "X"

    except ValueError:
        print("Please enter a number!")