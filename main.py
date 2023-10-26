import random


def clear_screen():
    print("\n" * 20)


# Let's define a function that clear the screen and show the board to user:
def display_board(board1):
    clear_screen()

    print(" _________________ ")
    print("|     |     |     |")
    print(f"|  {board[7]}  |  {board[8]}  |  {board[9]}  |")
    print(" _________________ ")
    print("|     |     |     |")
    print(f"|  {board[4]}  |  {board[5]}  |  {board[6]}  |")
    print(" _________________ ")
    print("|     |     |     |")
    print(f"|  {board[1]}  |  {board[2]}  |  {board[3]}  |")
    print(" _________________ ")


# Function that takes an index from user ands change the board value to sign and display board and win_check():
def user_choice(user_sign):
    global board
    if has_empty(board):
        print(f"Player {user_sign}:")
        index = input("Enter an index: ")
        if board[int(index)] == " ":
            board[int(index)] = user_sign
        display_board(board)


# Randomly returns a sign so we assign to first player
def give_sign():
    sign_list = ["X", "O"]
    return random.choice(sign_list)


# Let's assign sign to players:
def player_sign():
    global player1, player2
    player1 = give_sign()
    if player1 == "X":
        player2 = "O"
        print(f"Player 1 have this sign: {player1}")
        print(f"Player 2 have this sign: {player2}")
    else:
        player2 = "X"
        print(f"Player 1 have this sign: {player1}")
        print(f"Player 2 have this sign: {player2}")


# Function that check for winner with specified sign:
def win_check(sign):
    return ((board[1] == board[2] == board[3] == sign) or (board[4] == board[5] == board[6] == sign)
            or (board[7] == board[8] == board[9] == sign) or (board[1] == board[4] == board[7] == sign)
            or (board[2] == board[5] == board[8] == sign) or (board[3] == board[6] == board[9] == sign))


# Function that checks for empty space in board and return True or False:
def has_empty(board1):
    return " " in board


# Function that welcome players and tell which one should start and show the board:
def introduction():
    display_board(board)
    print("Welcome to tic tac toe")
    player_sign()


# Full game:
def game():
    introduction()
    while win_check(player1) == False and win_check(player2) == False and has_empty(board):
        user_choice(player1)
        if win_check(player1) == False:
            user_choice(player2)
    if win_check(player1):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

    y_or_n = input("Do you want to play again? y or n: ").lower()
    if y_or_n == "y":
        game()


player1, player2 = 0, 0
board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

game()
