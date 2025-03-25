# 84 Tic Tac Toe

def print_field():
    print(field[0:3])
    print(field[3:6])
    print(field[6:9])


def choose_player(cp_round, cp_players):
    if cp_round % 2 == 1:
        return cp_players[0]
    else:
        return cp_players[1]


def free_field():
    if "-" in field:
        return True
    else:
        return False



if __name__ == "__main__":
    print("Welcome to the Tic Tac Toe game.")
    is_running = True
    players = ["X", "O"]
    game_round = 1
    field = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

    player = choose_player(game_round, players)

    print(f"Player 1: {players[0]}, Player 2: {players[1]},")
    print_field()
    print(free_field())

    while is_running:
        player = choose_player(game_round, players)
        print(f"Current player {player}")

        next_round = input("Play another round y/n: ")
        game_round += 1
        if next_round == "n":
            is_running = False

    print("Game ends")
