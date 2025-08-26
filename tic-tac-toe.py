import random

# --- Constants for board mapping ---
ROW_MAP = {'T': 0, 'M': 2, 'B': 4}
COL_MAP = {'L': 0, 'M': 2, 'R': 4}

# --- Board creation ---
def create_board():
    return [
        [' ', '|', ' ', '|', ' '],
        ['-', '+', '-', '+', '-'],
        [' ', '|', ' ', '|', ' '],
        ['-', '+', '-', '+', '-'],
        [' ', '|', ' ', '|', ' ']
    ]

def print_board(board):
    for row in board:
        print("".join(row))

def print_board_key():
    print("Top Left(TL) | Top Middle(TM) | Top Right(TR)")
    print("Middle Left(ML) | Middle Middle(MM) | Middle Right(MR)")
    print("Bottom Left(BL) | Bottom Middle(BM) | Bottom Right(BR)")

# --- Coin flip ---
def flip_coin() -> bool:
    """Return True for heads, False for tails."""
    return random.choice([True, False])

# --- Player input ---
def player_turn(board, player_mark):
    while True:
        choice = input("Where would you like to go?\nYour choice (e.g., TL, MM): ").strip().upper()
        if not valid_string(choice):
            print("Invalid input. Must be two letters (row + column).")
            continue

        row, col = choice[0], choice[1]
        i, j = ROW_MAP.get(row, -1), COL_MAP.get(col, -1)
        if i == -1 or j == -1:
            print("Invalid selection. Try again.")
            continue
        if board[i][j] != ' ':
            print("That spot is already taken. Try again.")
            continue

        board[i][j] = player_mark
        break

def valid_string(choice: str) -> bool:
    return len(choice) == 2 and choice[0].isalpha() and choice[1].isalpha()

# --- Computer AI ---
def computer_turn(board, computer_mark: str, player_mark: str, difficulty):
    if difficulty == "EASY":
        random_move(board, computer_mark)
    else:
        i, j = find_best_move(board, computer_mark, player_mark)
        board[i][j] = computer_mark

def random_move(board, computer_mark):
    empty_positions = [(r, c) for r in range(0, len(board), 2) for c in range(0, len(board[r]), 2) if board[r][c] == ' ']

    if empty_positions:
        r, c = random.choice(empty_positions)
        board[r][c] = computer_mark

def board_empty(board) -> bool:
    return any(board[r][c] == ' ' for r in range(0, len(board), 2) for c in range(0, len(board[r]), 2))

def game_won(board, mark: str) -> bool:
    lines = [
        # Rows
        [(0,0),(0,2),(0,4)], [(2,0),(2,2),(2,4)], [(4,0),(4,2),(4,4)],
        # Columns
        [(0,0),(2,0),(4,0)], [(0,2),(2,2),(4,2)], [(0,4),(2,4),(4,4)],
        # Diagonals
        [(0,0),(2,2),(4,4)], [(0,4),(2,2),(4,0)]
    ]
    return any(all(board[r][c] == mark for r,c in line) for line in lines)

# --- Minimax AI ---
def minimax(board, depth: int, is_max: bool, computer_mark, player_mark) -> int:
    if game_won(board, computer_mark):
        return 10 - depth
    if game_won(board, player_mark):
        return depth - 10
    if not board_empty(board):
        return 0

    best = -1000 if is_max else 1000

    for i in range(0, len(board), 2):
        for j in range(0, len(board[i]), 2):
            if board[i][j] == ' ':
                board[i][j] = computer_mark if is_max else player_mark
                val = minimax(board, depth + 1, not is_max, computer_mark, player_mark)
                board[i][j] = ' '
                best = max(best, val) if is_max else min(best, val)

    return best

def find_best_move(board, computer_mark: str, player_mark: str) -> tuple[int,int]:
    best_val = -1000
    best_move = (-1, -1)

    for i in range(0, len(board), 2):
        for j in range(0, len(board[i]), 2):
            if board[i][j] == ' ':
                board[i][j] = computer_mark
                move_val = minimax(board, 0, False, computer_mark, player_mark)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# --- Main game loop ---
def play_game():
    board = create_board()
    print("Welcome to Tic-Tac-Toe!\nI am the computer. I will be beating you at this game!")

     # Choose difficulty
    difficulty = ""
    while difficulty not in ("1", "2"):
        difficulty = input("Choose difficulty:\n1. Easy\n2. Hard\nChoice: ").strip()
    difficulty = "EASY" if difficulty == "1" else "HARD"

    print("Next, we must flip a coin to determine who goes first.")

    guess = input("Call it! (H/T): ").strip().upper()
    while guess not in ("H", "T"):
        guess = input("Invalid. Call H or T: ").strip().upper()

    side_up = 'H' if flip_coin() else 'T'
    print(f"It landed {'heads' if side_up=='H' else 'tails'} up!")

    player_first = guess == side_up
    player_mark = 'X' if player_first else 'O'
    computer_mark = 'O' if player_first else 'X'
    print("You go first." if player_first else "I go first!")

    print_board_key()

    game_over = False
    player_turn_flag = player_first

    while not game_over:
        print_board(board)

        if player_turn_flag:
            print("\nYour turn:")
            player_turn(board, player_mark)
        else:
            print("\nMy turn:")
            computer_turn(board, computer_mark, player_mark, difficulty)

        current_mark = player_mark if player_turn_flag else computer_mark
        if game_won(board, current_mark):
            print_board(board)
            print("You win!" if player_turn_flag else "I win!")
            game_over = True
        elif not board_empty(board):
            print_board(board)
            print("It's a tie!")
            game_over = True

        player_turn_flag = not player_turn_flag

def main():
    while True:
        play_game()
        again = input("\nDo you want to play again? (Y/N): ").strip().upper()
        if again != 'Y':
            print("Thanks for playing! Goodbye!")
            break

# --- Run the game ---
if __name__ == "__main__":
    main()
