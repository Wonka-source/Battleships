# A Battleships Game

A Battleships Game is a Python terminal game which runs in Heroku on the Code Institute mock terminal.

The users can play a battleships game against the computer. Users can try to beat the computer by finding all of the computer's battleships before the computer finds theirs. Each battleship occupies one square on the board.

[Heres a link to the live verson](https://abattleship.herokuapp.com/ "Heres a link to the live verson")[![Am i responsive ](https://i.imgur.com/7BgrvWJ.jpeg "Am i responsive ")](https://i.imgur.com/7BgrvWJ.jpeg "Am i responsive ")

## How to play
You can read about battleships here: [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game) "Wikipedia").

The player is first prompt to input a grid size between the values 4 and 7 to set the board. This value then determines the minimum and maximum values the player can choose from, as the number of ships on the boards; This is achieved by: size x size x .2 for the minimum and size x size .5 for the maximum. The player is then prompt to enter their name. Two boards are generated for each the player and the computer with their ships randomly placed. The player able to see where their ships are, indicated by an @ sign while the computer's are hidden from the player. Guesses are marked on the board by an X, and hits are indicated by a *.

## Features 
### Existing Features
- Board size selection
- Ship amount selection with a minimum and maximum depending on the board size
- Ships are randomly placed on the player's board and the computers.
- The player cannot see where the computer's ships are.

[![Comp board and player board](https://i.imgur.com/yEJs8va.jpeg "Comp board and player board")](https://i.imgur.com/yEJs8va.jpeg "Comp board and player board")

- Play against the computer
- Accepts user input
- maintains scores

[![Scores](https://i.imgur.com/jVM9GbT.jpeg "Scores")](https://i.imgur.com/jVM9GbT.jpeg "Scores")

- Input validation
	- You cannot enter coordinates outside the size of the grid
	- You must enter numbers
	- You cannot enter the same guess twice
  
[![Validation ](https://i.imgur.com/8ZsHwXo.jpeg "Validation ")](https://i.imgur.com/8ZsHwXo.jpeg "Validation ")

- Data maintained in class instances

## Future Features
- Boards have indexing to make it easier to pick a move
- Boards printed horizontally to utilise free space and then would also be able to make the boards bigger.
- Allow the player to place the ships themselves
- Have ships larger than 1x1

## Data Model
I decided to use a board class as my model. The game creates two instances of the Board class to hold the player's and the computer's board. The Board class stores the board size, the number of ships, position of the ships, guesses against that board, and details such as the board type (player's board or computer), the players name and the remaining board (if == player and used to determine what remaining coordinances the computer has left to pick form).

The class also has methods to help play the game, such as a print method to print the current board, populate_board to populate the board, and check_for_win to determine if there is a winner. take_coord, valid_coord, take_guess, valid_guess to validate guesses and a random_computer_guess to pick a random coordinance remaining on the player's board.

## Testing
I have manually tested this project by:
- Passing the code through PEP 8 linter and confirmed no problems.
- Giving invalid inputs: strings when numbers are expected, out-of-bounds inputs, same input twice.
- Tested on my local terminal and the Code Institute Heroku terminal.

## Bugs 
- No bugs remaining

## Validator testing
- PEP 8
 - No errors were returned from PEP8online.com
 
## Deployment
- Add newline (/n) to all input methods
- Save the file
- Create a list of dependencies and add them to a requirements.txt file 
- In the terminal: "pip3 freeze > requirements.txt"
- Push the changes up to GitHub
- Go to Heroku's website and log in
- On the Heroku dashboard, click the create new app button
- Name the app a unique name 
- Select Region
- Click Create app
- Select the setting tab
-  Scroll to the Config Var section and add:
   - Config Var: PORT. _______ Set it to:8000
- add two buildpacks in this order:
  1. `heroku/python`
  1.  `heroku/nodejs`
- Select the Deploy tab
- Then select Github and confirm connect to GitHub
- Search for the repository name
- Then click connect
- Select either manual or automatic deploy
- Click view to view  

##  Credits
-  Code Institute for the deployment terminal
-  My mentor Brian for guidance
- Wschools for tutorials
- StackOverflow for coding methods
- Wikipedia for the details of the battleship game
