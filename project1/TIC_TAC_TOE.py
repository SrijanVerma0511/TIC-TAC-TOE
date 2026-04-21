import random

# Create empty board
board = [" " for i in range(9)]

# Function to print board
def print_board():
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
    print("\n")

# Function to check winner
def check_winner(player):

    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True

    return False


# Player move
def player_move():
    pos = int(input("Enter position (0-8): "))
    board[pos] = "X"

    # while True:

    #     try:
    #         pos = int(input("Enter position (1-9): ")) - 1

    #         if pos >= 0 and pos <= 8 and board[pos] == " ":
    #             board[pos] = "X"
    #             break

    #         else:
    #             print("Invalid position! Try again.")

    #     except:
    #         print("Please enter a number between 1 and 9.")


# Computer move
def computer_move():

    empty = [i for i in range(9) if board[i] == " "]

    if empty:
        pos = random.choice(empty)
        board[pos] = "O"


# Check draw
def check_draw():

    if " " not in board:
        return True

    return False


# Game Loop
while True:

    print_board()

    # Player turn
    player_move()

    if check_winner("X"):
        print_board()
        print("🎉 Player Wins!")
        break

    if check_draw():
        print_board()
        print("Game Draw!")
        break


    # Computer turn
    computer_move()

    if check_winner("O"):
        print_board()
        print("💻 Computer Wins!")
        break

    if check_draw():
        print_board()
        print("Game Draw!")
        break


print("Game Over")