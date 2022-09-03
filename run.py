from random import randint

class Board:

    def __init__(self, size, num_ships, name):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.guesses = []
        self.ships = []

    




def play_game(computer_board, player_board):

    print(f"{player_board.name}'s Board:")
    print("Computer's Board:")
    x = input("Guess a row:")
    y = input("Guess a column:")





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
    computer_board = Board(int(size), int(num_ships), "Computer")
    player_board = Board(int(size), int(num_ships), player_name)

    play_game(computer_board, player_board)
    
new_game()