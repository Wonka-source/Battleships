from board import Board


def valid_board_size(size):
    """
    Takes a string and checks if it is an invalid board size.
    Returns False if the size is a number between 5 and 10 (inclusive)
    """
    return (size > 3 and size < 8)


def take_size():
    """
    Takes the board size from the player and uses the returned
    value from invalid_board_size() to determine if its within
    the range and prompts the player until it is.
    Returns the value as an int.
    """
    while True:
        try:
            size = int(input("BOARD SIZE:\n").strip())
            if not valid_board_size(size):
                raise ValueError("Number must be between 4 and 7.")

        except ValueError:
            print("Please enter a number between 4 and 7.")
            continue

        return size


def valid_ships(ships, min_ships, max_ships):
    """
    Takes a string and checks if it is an invalid number of ships
    returns False (which is = to a Valid num of ships) if the string
    is a number and the value is between the variables "min_ships"
    and "max_ships" (inclusive).
    """
    return (ships >= min_ships and ships <= max_ships)


def take_ships(size):
    """
    Using the board size, this calculates the values for "min_ships" and
    "max_ships". Prompts the user to input a number between the min and
    max ships. Then using a while loop, it runs all the values through the
    invalid_ships(). While this function returns True (ships are invalid)
    the player is prompt to input the value again.
    Returns ships as an int.
    """
    min_ships = int(size*size*.2)
    max_ships = int(size*size*.5)
    while True:
        try:
            ships = int(input(
                f"\nEnter a numb between {min_ships}-{max_ships}!\n\nSHIPS:\n"
                ).strip())
            if not valid_ships(ships, min_ships, max_ships):
                raise ValueError(
                    f"Number must be between {min_ships} and {max_ships}."
                    )

        except ValueError:
            continue

        return ships


def play_game(computer_board, player_board, player_score, computer_score):
    """
    Runs the game. Takes the computer board and player board and prints
    them to the terminal. call's the take_guess() (prompts for the
    players move) then call's the random_computer_guess (computers
    move).
    """
    print("Top left corner is row: 0, col: 0")
    print("#" * 35)
    print(f"{player_board.name}'s Board:")
    player_board.print()
    print("\nComputer's Board:")
    computer_board.print()
    player_score = computer_board.take_guess(player_score)
    computer_score = player_board.random_computer_guess(computer_score)
    if (player_board.check_for_win()):
        print("\n\nCOMPUTER WINS\n\n")
        new_game()
    elif (computer_board.check_for_win()):
        print("\n\nPLAYER WINS\n\n")
        new_game()
    else:
        play_game(computer_board, player_board, player_score, computer_score)


def new_game():
    """
    Starts a new game. Runs take_size() to get the size of the board
    then runs take_ships() to get the number of ships. Creates two
    class instances "computer_board" and "player_board" and then runs
    the populate_board() for the both of them. Then runs them through
    the play_game().
    """
    player_score = 0
    computer_score = 0
    print("-" * 35)
    print("   Welcome to a Battleships Game\n")
    print("-" * 35)
    print("       Enter a Board Size!\n")
    print(" Minimum Size = 4  Maximum Size = 7 \n")
    size = take_size()
    print("-" * 35)
    print("       Enter Num of Ships!\n")
    num_ships = take_ships(size)
    print("-" * 35)
    print("        Enter Your Name!\n")
    player_name = input("Your Name:\n").strip()
    print("#" * 35)
    print(f"Board size:{size}. Numb of Ships:{num_ships}\n")
    computer_board = Board(
        int(size), int(num_ships), "Computer", type="computer"
        )
    player_board = Board(int(size), int(num_ships), player_name, type="player")

    computer_board.populate_board()
    player_board.populate_board()

    play_game(computer_board, player_board, player_score, computer_score)


if __name__ == "__main__":
    new_game()
