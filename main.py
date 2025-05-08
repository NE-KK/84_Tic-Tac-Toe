# 84 Tic Tac Toe

def print_field(pf_field):
    """
    Print the current field
    Takes field array as input
    :param pf_field:
    """
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


def choose_player_field():
    valid_number = False
    while not valid_number:
        try:
            cpf_player_field = int(input(f"Choose a field 0-8: "))
            if 0 <= cpf_player_field <= 8:
                valid_number = True
                return cpf_player_field
            else:
                print(f"{cpf_player_field} is out of range.")
        except ValueError:
            print("Type a number.")


def check_field() -> bool:
    """
    Checks for empty fields.
    Returns True if empty marks (-) in the field.
    :return:
    """
    if "-" in field:
        return True
    else:
        return False


def check_for_win(cfw_player: str) -> bool:
    """
    Checks if 3 player marks (X or O) are in a row.
    Takes player mark (X or O) as input.
    Returns True if 3 player marks are in a row, otherwise it returns False
    :param cfw_player:
    :return:
    """
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
    is_running = True

    while is_running:
        # Set up the game
        print("Welcome to the Tic Tac Toe game.")
        game_is_on = True
        players = ["X", "O"]
        player = "-"
        game_round = 1
        field = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]

        print_field(field)
        is_free = check_field()


        while game_is_on:
            field_is_free = False
            player = choose_player(game_round, players)
            print(f"Current player {player}")

            while not field_is_free:
                player_field = choose_player_field()

                if field[player_field] == "-":
                    field[player_field] = player
                    field_is_free = True
                else:
                    print("No empty field!")

            print_field(field)
            game_round += 1
            is_won = check_for_win(player)

            if is_won:
                game_is_on = False


        print("-----------------------------------------------------------")
        print(f"Congratulation to {player}. You Won!")
        next_round = input("Play another round y/n: ")
        if next_round == "n":
            is_running = False

        print("Game ends")

