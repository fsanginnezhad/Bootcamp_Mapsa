# Tik Tok game project

This is a Python project that implements a tic-tac-toe game. The game allows two players to take turns placing their symbol (X or O) on a 3x3 board. The first player to get three of their symbols in a row (horizontal, vertical or diagonal) wins the game. If the board is filled without any player winning, the game ends in a draw.

## Project structure

This project is organized into several folders and files, which are described below:

- `core/`:
     - `app.py`: This file contains the main logic of the game. It handles player inputs, calls the necessary functions from the "utils" folder, and displays the output to the user.

- `game/`':
     - `utils/`: This folder contains all the functions used in the game, such as checking the win bet, displaying the game screen and receiving player input.

     - `models/`: This folder contains the definition of two players in the game. Each player is defined by his name and symbol.

     - `helper/`: This folder specifies the coordinates of the game screen. Used to map player inputs to the corresponding cell on the board.

- `run.py`: This is the main file that runs the program. Each command is sent to the desired file and the program executes the corresponding function.

## How to run the program

To run the program, follow the steps below:

1. Clone the repository from GitHub: `git clone https://github.com/fsanginnezhad/Tic-Tac-Toe---Functional.git`.

2. Go to the project directory: "cd Tic-Tac-Toe---Functional".

3. Install the required dependencies: pip install -r requirements.txt

4. Run the program: "python run.py".

## Use

When you run the program, you are then prompted to take turns placing your symbol (X or O) on the game board. Here is an overview of the available commands:

![Capture](https://github.com/fsanginnezhad/Tic-Tac-Toe---Functional/assets/73942999/936d91e9-9a73-438b-a7e3-5414760e34ec)

To place your icon on the board, enter the cell number where you want to place your icon. For example, to place your icon in the middle, enter the number '5'. The game will continue until someone wins or the board is full.

## Credits

This project was created by `Farshad Sanginnezhad`. If you have any questions or feedback, please contact me.
