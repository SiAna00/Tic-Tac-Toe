print("Welcome to Tic Tac Toe. Let's play a game, shall we?")

board = " 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 \n"

print(board)

players = {
    "Player A" : {
        "sign" : "X",
         "combination" : []
    },
    "Player B" : {
        "sign" : "O",
        "combination" : []
    }
}

winning_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]]

game_on = True

while game_on == True:
    for player in players:

        if player == "Player B" and len(players[player]["combination"]) == 4:
            print("Game over. It's a draw.")
            game_on = False

        else:
            player_input = input(f"{player}: Choose a number: ")

            for character in board:
                if character == player_input:
                    board = board.replace(character, players[player]["sign"])
                    players[player]["combination"].append(int(player_input))

                    if len(players[player]["combination"]) >= 3:
                        players[player]["combination"].sort()

                        for item in winning_combinations:
                            if set(item) <= set(players[player]["combination"]):
                                print(f"Congratulations! {player} is the winner!")
                                game_on = False

            print(board)
