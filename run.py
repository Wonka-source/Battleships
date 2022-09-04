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
    
    def print(self):
        for row in self.board:
            print(" ".join(row))
    
    def guess(self, x, y):
        self.guesses.append((x, y))        

        if(x, y) in self.ships:
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



def play_game(computer_board, player_board):
    print("\n Top left corner is row: 0, col: 0\n")
    print(f"{player_board.name}'s Board:")
    player_board.print()
    print("Computer's Board:")
    computer_board.print()
    print(f"\n{computer_board.guesses}")
    x = input("\nGuess a row:")
    y = input("Guess a column:")
    computer_board.guess(int(x), int(y))
    play_game(computer_board, player_board)





def new_game():
    """
    Starts a new game. Sets the size of the board and the number of ships.
    """

    print("-" * 35) 
    print("   Welcome to a Battleships Game\n")
    print("-" * 35)
    print("       Enter a Board Size!\n")
    print(" Minimum Size= 5  Maximum Size= 10 \n")    
    size = input("Board Size:\n")
    print("-" * 35)
    print("       Enter Num of Ships!\n")
    print(" Minimum Num= 4  Maximum Num= 14 \n")
    num_ships = input("Num of Ships:\n")
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

    play_game(computer_board, player_board)
    
    
new_game()