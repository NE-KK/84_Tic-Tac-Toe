# 84 Tic Tac Toe

def print_field(pf_field):
    print(pf_field[0:3])
    print(pf_field[3:6])
    print(pf_field[6:9])


def choose_player(cp_round: int, cp_players: list) -> str:
    """
    Returns the current player depending on played rounds.
    :param cp_round:
    :param cp_players:
    :return:
    """
    if cp_round % 2 == 1:
        return cp_players[0]
    else:
        return cp_players[1]


def check_field() -> bool:

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

    print_field(field)
    is_free = check_field()


    while is_running:
        player = choose_player(game_round, players)
        print(f"Current player {player}")
        player_field = int(input(f"Choose a field 0-8: "))
        field[player_field] = player
        print_field(field)
        next_round = input("Play another round y/n: ")
        game_round += 1
        if next_round == "n":
            is_running = False

    print("Game ends")
