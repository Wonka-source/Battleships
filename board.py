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

    def valid_guess(self, x, y):
        """
        Takes an x and a y (coord) and checks if it has already been
        guessed (if it is listed among the board.guesses of the given
        board class).
        """
        return ((x, y) not in self.guesses)

    def take_guess(self, player_score):
        """
        Prompts the player for an x and a y coord. Then uses the valid_guess()
        to check if it is a valid coordinates (one that has not already been
        guessed). If it is not valid it will rase a value error until a
        valid coord is entered.
        """
        while True:
            try:
                x = take_coord("row", self.size)
                y = take_coord("column", self.size)
                if not self.valid_guess(x, y):
                    raise ValueError("Must be a new guess.")

            except ValueError:
                print("ALREADY GUESSED!")
                continue

            print("#" * 35)
            hit_miss = self.guess((x, y))
            print(f"\nPLAYER: {x, y} {hit_miss}!")
            if hit_miss == "Hit":
                player_score += 1

            print("score:", player_score)
            return player_score

    def random_computer_guess(self, computer_score):
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
        x_y = self.remaining_player_board.pop(
            random_point(len(self.remaining_player_board))
            )
        hit_miss = self.guess(x_y)
        print(f"\nCOMPUTER: {x_y[0], x_y[1]} {hit_miss}!")
        if hit_miss == "Hit":
            computer_score = computer_score + 1
        print("score:", computer_score)
        input("\nPress enter to continue:\n")
        print("-" * 35)
        return computer_score


def valid_coord(coord, size):
    """
    Takes a string (coord) and checks if it is a number and within range
    of the board size. Returns True if it is valid and False if it is
    invalid.
    """
    return (coord > -1 and coord < size)


def take_coord(row_column, size):
    """
    Takes the x or the y coord from the player. Then uses the valid_coord()
    to check if it is a valid coordinates (a num and within the range of the
    board size). If it is not valid will rase a value error until a valid
    coord is entered.

    """
    while True:
        try:
            coord = int(input(f"Guess a {row_column}:\n").strip())
            if not valid_coord(coord, size):
                raise ValueError(f"Values must be between 0 and {size - 1}")

        except ValueError:
            print(f"Values must be between 0 and {size - 1}")
            continue

        return coord


def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, size - 1)
