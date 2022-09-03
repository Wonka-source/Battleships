from random import randint

class Board:
    


# def setup():


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


    
new_game()