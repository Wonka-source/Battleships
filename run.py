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

        if type == "player":
            self.remaining_computer_guesses = [(x, y) for x in range(size) for y in range(size)]
            # print(self.remaining_computer_guesses)
    def print(self):
        for row in self.board:
            print(" ".join(row))
    
    def guess(self, a_valid_guess):
        x = a_valid_guess[0]
        y = a_valid_guess[1]
        # list.append(a_valid_guess)
        self.guesses.append((x, y))        
        # print(self.guesses, "guess(self, a_valid_guess):")
        # print("a_valid_guess", x, y)
        if(x, y) in self.ships:
            self.board[x][y]= "*"
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
            
            # print("num of ships", num_of_ships_placed)
            # print("board num of ships", self.num_ships)
            # print("battle row ", battleship_row)
            # print("battle col", battleship_col)
            # print("board ships", self.ships)
            # print("#" * 25)


def random_point(size):
    """
    Helper function to return a random integer between 0 and size
    """
    return randint(0, size -1)

def invalid_board_size(size):
    if size.isnumeric() and int(size) > 4 and int(size) < 11:
        return False
    return True

def invalid_ships(ships, min_ships, max_ships):
    if ships.isnumeric() and int(ships) >= min_ships and int(ships) <= max_ships:
        return False
    return True

def take_size():
    size = input(f"BOARD SIZE:\n")
    while invalid_board_size(size):
        size = input("\nYou must enter a number between 5 and 10!\nBOARD SIZE:\n")
    return int(size)

def take_ships(size):
    min_ships = int(size*size*.2)
    max_ships = int(size*size*.5)
    ships = input(f"Minimum Ships = {min_ships} Maximum Ships = {max_ships}\n\nSHIPS:\n")
    while invalid_ships(ships, min_ships, max_ships):
        ships = input(f"\nYou must enter a number {min_ships} and {max_ships}!\n\nSHIPS:\n")
    return int(ships)


def take_coord(row_column, size):
    coord = input(f"\nGuess a {row_column}:")
    while invalid_coord(coord, size):
        print(f"Values must be between 0 and {size - 1}")
        coord = input(f"Please enter a {row_column}:\n")
    return int(coord)

def invalid_coord(coord, size):
    if coord.isnumeric() and int(coord) > -1 and int(coord) < size:
        return False
    return True

# def valid_guess(x, y, board):
#     coord = (x, y)    
#     print(coord, "guessed")
#     guesses = board.guesses
#     # print(guesses, "gusses")
#     if coord in guesses:
#         return False
#     return True

def invalid_guess(x, y, board):
    if (x, y) in board.guesses:
        return True
    return False

def take_guess(board):
    x = take_coord("row", board.size)
    y = take_coord("column", board.size)
    while invalid_guess(int(x), int(y), board):
        print("ALREADY GUESSED!")
        x = take_coord("row", board.size)
        y = take_coord("column", board.size)
    print(board.guess((x, y)))





def play_game(computer_board, player_board, size):
    # print(computer_board.guesses, "computerboard guesses" )
    print("#" * 35)
    print("\n Top left corner is row: 0, col: 0\n")
    print("#" * 35)
    print(f"{player_board.name}'s Board:")
    player_board.print()
    print("\nComputer's Board:")
    computer_board.print()
    print(f"\n{player_board.guesses}")
    take_guess(computer_board)
    play_game(computer_board, player_board, size)
    # print(computer_board.guesses, "computerboard guesses" )




def new_game():
    """
    Starts a new game. Sets the size of the board and the number of ships.
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
    print("-" * 35)
    print(f" Hello {player_name}!\n")    
    print(f" Board size:{size}. Numb of Ships:{num_ships}\n")    
    print(" Top left corner is row: 0, col: 0")
    print("-" * 35) 
    computer_board = Board(int(size),int(num_ships), "Computer", type="computer")
    player_board = Board(int(size), int(num_ships), player_name, type="player")

    computer_board.populate_board()
    player_board.populate_board()

    play_game(computer_board, player_board, int(size))
    
    
new_game()