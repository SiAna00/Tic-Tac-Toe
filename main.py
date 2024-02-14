print("Welcome to Tic Tac Toe. Let's play a game, shall we?")

board = " 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 \n"

print(board)

players = {
    "player_a" : "X",
    "player_b" : "O"
}

for player in players:
    player_input = input("Choose a number: ")

    for character in board:
        if character == player_input:
            board = board.replace(character, players[player])

    print(board)


""" player_a = input("Choose a number: ")

for character in board:
    if character == player_a:
        board = board.replace(character, "X")

print(board)

player_b = input("Choose a number: ")

for character in board:
    if character == player_b:
        board = board.replace(character, "O")

print(board) """