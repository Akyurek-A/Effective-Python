# Simply made TicTacToe game for Python.

print("\nWelcome to the TicTacToe game!")

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
    print("\n")

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row [0] != "-":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "-":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return board[0][0]

    if board [0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return board[0][2]

    return None

def check_tie(board):
    for row in board:
        if "-" in row:
            return False
    return True

def play_game():
    board= [["-" for _ in range(3)]for _ in range(3)]

    current_player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter the row (1, 2, 3): "))
            col = int(input(f"Player {current_player}, enter the column (1, 2, 3): "))
        except ValueError:
            print("Please enter a valid number(1, 2, 3).")
            continue

        row -= 1
        col -= 1

        if row not in [0,1,2] or col not in [0,1,2]:
            print("Invalid input. Please enter 1, 2 or 3 for both row and column.")
            continue

        if board[row][col] == "-":
            board[row][col] = current_player
        else:
            print("This position is already taken.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        if check_tie(board):
            print_board(board)
            print(f"It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()