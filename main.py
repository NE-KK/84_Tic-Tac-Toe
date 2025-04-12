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


def check_for_win(cfw_player: str) -> bool:
    # check horizontal fields
    if field[0] == cfw_player and field[1] == cfw_player and field[2] == cfw_player:
        return True
    elif  field[3] == cfw_player and field[4] == cfw_player and field[5] == cfw_player:
        return True
    elif  field[6] == cfw_player and field[7] == cfw_player and field[8] == cfw_player:
        return True
    # check vertical fields
    elif field[0] == cfw_player and field[3] == cfw_player and field[6] == cfw_player:
        return True
    elif field[1] == cfw_player and field[4] == cfw_player and field[7] == cfw_player:
        return True
    elif field[2] == cfw_player and field[5] == cfw_player and field[8] == cfw_player:
        return True
    # check diagonal fields
    elif field[0] == cfw_player and field[4] == cfw_player and field[8] == cfw_player:
        return True
    elif field[2] == cfw_player and field[4] == cfw_player and field[6] == cfw_player:
        return True
    else:
        return False


if __name__ == "__main__":
    print("Welcome to the Tic Tac Toe game.")
    is_running = True

    while is_running:
        is_won = False
        players = ["X", "O"]
        game_round = 1
        field = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]

        print_field(field)
        is_free = check_field()


        while not is_won:
            player = choose_player(game_round, players)
            print(f"Current player {player}")
            player_field = int(input(f"Choose a field 0-8: "))
            field[player_field] = player
            print_field(field)
            game_round += 1

            is_won = check_for_win(player)


        next_round = input("Play another round y/n: ")
        if next_round == "n":
            is_running = False

        print("Game ends")

