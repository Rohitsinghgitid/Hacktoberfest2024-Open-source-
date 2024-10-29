# Initialize the board with empty spaces
board = [" " for _ in range(9)]

# Function to display the board
def display_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check if there is a winner
def check_winner(player):
    # Winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full
def check_draw():
    return " " not in board

# Main game function
def play_game():
    current_player = "X"
    
    while True:
        display_board()
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move! Please try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        board[move] = current_player
        
        # Check if there's a winner
        if check_winner(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            break

        # Check for a draw
        if check_draw():
            display_board()
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
