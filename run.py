from random import randint


class Board:
    """
    Main board class. Sets board size, the number of ships,
    the name and board type (computer or player).
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

        # generates a list of all the coords of the player board
        # this is used for computers remaining turns/guesses
        if type == "player":
            self.remaining_player_board = [
                (x, y) for x in range(size) for y in range(size)
                ]

    def print(self):
        """
        Function for printing the board
        """
        for row in self.board:
            print(" ".join(row))

    def guess(self, a_valid_guess):
        """
        Function for adding guesses to the board
        """
        x = a_valid_guess[0]
        y = a_valid_guess[1]

        self.guesses.append((x, y))

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            self.board[x][y] = "X"
            return "Miss"

    def populate_board(self):
        """
        populates ships to the computer's and the player's
        board
        """
        num_of_ships_placed = 0

        while self.num_ships > num_of_ships_placed:

            battleship_row = random_point(self.size)
            battleship_col = random_point(self.size)
            if (battleship_row, battleship_col) not in self.ships:
                self.ships.append((battleship_row, battleship_col))
                num_of_ships_placed += 1
                if self.type == "player":
                    self.board[battleship_row][battleship_col] = "@"

    def check_for_win(self):
        """
        Checks for a winner by checking if all the coordinates of self.ship
        list are in self.guesses list.
        https://thispointer.com/python-check-if-a-list-contains-all-the-elements-of-another-list/
        """
        return all(elm in self.guesses for elm in self.ships)


def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, size - 1)


def invalid_board_size(size):
    """
    Takes a string and checks if it is an invalid board size.
    Returns False if the size is a number between 5 and 10 (inclusive)
    """
    if size.isnumeric() and int(size) > 4 and int(size) < 11:
        return False
    return True


def take_size():
    """
    Takes the board size from the player and uses the returned
    value from invalid_board_size() to determine if its within
    the range and prompts the player until it is.
    Returns the value as an int.
    """
    size = input("BOARD SIZE:\n")
    while invalid_board_size(size):
        size = input(
            "\nYou must enter a number between 5 and 10!\nBOARD SIZE:\n"
            )
    return int(size)


def invalid_ships(ships, min_ships, max_ships):
    """
    Takes a string and checks if it is an invalid number of ships
    returns False (which is = to a Valid num of ships) if the string
    is a number and the value is between the variables "min_ships"
    and "max_ships" (inclusive).
    """
    ship = int(ships)
    if ships.isnumeric() and ship >= min_ships and ship <= max_ships:
        return False
    return True


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
    ships = input(
        f"Minimum Ships = {min_ships} Maximum Ships = {max_ships}\n\nSHIPS:\n"
        )
    while invalid_ships(ships, min_ships, max_ships):
        ships = input(
            f"\nEnter a num between {min_ships} and {max_ships}!\n\nSHIPS:\n"
            )
    return int(ships)


def invalid_coord(coord, size):
    """
    Takes a string (coord) and checks if it is a number and within range
    of the board size. Returns False if it is valid and True if it is
    invalid.
    """
    if coord.isnumeric() and int(coord) > -1 and int(coord) < size:
        return False
    return True


def take_coord(row_column, size):
    """
    Takes the x or the y coord from the player. Then uses the invalid_coord()
    to check if it is a valid coordinates (ie a num and within the range of the
    board size). If it is not valid the player will be prompt to input again.
    Returns the coord as an int.

    """
    coord = input(f"Guess a {row_column}:\n")
    while invalid_coord(coord, size):
        print(f"Values must be between 0 and {size - 1}")
        coord = input(f"Please enter a {row_column}:\n")
    return int(coord)


def invalid_guess(x, y, board):
    """
    Takes an x and a y (coord) and checks if it has already been
    guessed (if it is already present in the board.guesses class
    attribute of the given board (argument)).
    """
    if (x, y) in board.guesses:
        return True
    return False


def take_guess(board):
    """
    When called prompts the player to input their guess which is stored
    as an x and a y variable, respectively. Then uses the invalid_guess() to
    check if the guess is invalid (prompts the player "already guessed
    if it is invalid) and re-askes the player to input until it is
    valid. Then Prints the valid guess to the board.
    """
    x = take_coord("row", board.size)
    y = take_coord("column", board.size)
    while invalid_guess(int(x), int(y), board):
        print("ALREADY GUESSED!")
        x = take_coord("row", board.size)
        y = take_coord("column", board.size)
    print("#" * 35)
    print(f"\nPLAYER: {x, y} {board.guess((x, y))}!")
    player_score = 0
    if board.guess((x, y)) == "Hit":
        print("score:", player_score + 1)
    else:
        print("score:", player_score)


def random_computer_guess(board):
    """
    Used to generate a random guess for the computer. Takes "player board"
    and uses "remaining_player_board" class attribute (witch is a list of
    tuples [all possible coordinates]) and picks a random point along its
    length. Then uses the pop() to pull it out (so it is then no longer
    remaining within in the the list of choices) and stores the val in a
    "xy" var (the computers guess). Then prints the guess to the players
    board.
    """
    # https://www.w3schools.com/Python/python_lists_remove.asp
    x_y = board.remaining_player_board.pop(
        random_point(len(board.remaining_player_board))
        )
    print(f"COMPUTER: {x_y} {board.guess(x_y)}!")
    computer_score = 0
    if board.guess(x_y) == "Hit":
        print("score:", computer_score + 1)
    else:
        print("score:", computer_score)
    input("\nPress enter to continue:\n")
    print("-" * 35)


def play_game(computer_board, player_board):
    """
    Runs the game. Takes the computer board and player board and prints
    them to the terminal. call's the take_guess() (prompts for the
    players move) then call's the random_computer_guess (computers
    move).
    """
    # print(computer_board.guesses, "computerboard guesses" )
    print("Top left corner is row: 0, col: 0\n")
    print("#" * 35)
    print(f"{player_board.name}'s Board:")
    player_board.print()
    print("\nComputer's Board:")
    computer_board.print()
    print(f"{computer_board.guesses}")
    take_guess(computer_board)
    random_computer_guess(player_board)
    if (player_board.check_for_win()):
        print("\n\nCOMPUTER WINS\n\n")
    elif (computer_board.check_for_win()):
        print("\n\nPLAYER WINS\n\n")
    else:
        play_game(computer_board, player_board)

    # print(computer_board.guesses, "computerboard guesses" )


def new_game():
    """
    Starts a new game. Runs take_size() to get the size of the board
    then runs take_ships() to get the number of ships. Creates two
    class instances "computer_board" and "player_board" and then runs
    the populate_board() for the both of them. Then runs them through
    the play_game().
    """

    print("-" * 35)
    print("   Welcome to a Battleships Game\n")
    print("-" * 35)
    print("       Enter a Board Size!\n")
    print(" Minimum Size = 5  Maximum Size = 10 \n")
    size = take_size()
    print("-" * 35)
    print("       Enter Num of Ships!\n")
    num_ships = take_ships(size)
    print("-" * 35)
    print("        Enter Your Name!\n")
    player_name = input("Your Name:\n")
    print("#" * 35)
    print(f"Hello {player_name}!\n")
    print(f"Board size:{size}. Numb of Ships:{num_ships}\n")
    computer_board = Board(
        int(size), int(num_ships), "Computer", type="computer"
        )
    player_board = Board(int(size), int(num_ships), player_name, type="player")

    computer_board.populate_board()
    player_board.populate_board()

    play_game(computer_board, player_board)


new_game()
