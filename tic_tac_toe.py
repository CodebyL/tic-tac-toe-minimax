import math

# Initialize the board as a 2D list
board = [[" " for _ in range(3)] for _ in range(3)]

def print_board():
    """Displays the Tic-Tac-Toe board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner():
    """Checks for a winner and returns 'X', 'O', or None."""
    # Rows and Columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]  # Row winner
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]  # Column winner

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None  # No winner yet

def is_board_full():
    """Checks if the board is full."""
    for row in board:
        if " " in row:
            return False  # Empty space found, game continues
    return True  # No empty spaces, it's a draw

def minimax(is_maximizing):
    """Minimax algorithm for AI decision-making."""
    winner = check_winner()
    if winner == "X":  # Human wins
        return -1
    elif winner == "O":  # AI wins
        return 1
    elif is_board_full():  # It's a draw
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"  # AI move
                    score = minimax(False)  # Recursively check next move
                    board[i][j] = " "  # Undo move
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"  # Human move
                    score = minimax(True)
                    board[i][j] = " "  # Undo move
                    best_score = min(best_score, score)
        return best_score

def best_move():
    """Finds the best move for the AI using Minimax."""
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(False)
                board[i][j] = " "  # Undo move
                if score > best_score:
                    best_score = score
                    move = (i, j)
    board[move[0]][move[1]] = "O"  # AI makes the best move

def player_move():
    """Allows the player to input a move."""
    while True:
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Enter numbers between 1 and 3.")

def play_game():
    """Main game loop."""
    print("Welcome to Tic-Tac-Toe! You are 'X' and the AI is 'O'.")
    print_board()

    while True:
        player_move()  # Human move
        print_board()

        if check_winner() == "X":
            print("You win! Congratulations!")
            break
        if is_board_full():
            print("It's a draw!")
            break

        print("AI is making a move...")
        best_move()  # AI move
        print_board()

        if check_winner() == "O":
            print("AI wins! Better luck next time.")
            break
        if is_board_full():
            print("It's a draw!")
            break

# Run the game
play_game()