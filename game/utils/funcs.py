import os
import random
from time import sleep
from colorama import Fore
from game.helper.const import CELLS
from game.models.players import player1, player2



def color_red(word: str) -> str:
    """
    Returns the input string with a red color.

    This function uses the 'colorama' module to add a red color to the input string. # noqa E501

    Args:
    word (str): A string to add color to.

    Returns:
    A string with a red color.
    """
    return Fore.RED + word + Fore.RESET


def color_blue(word: str) -> str:
    """
    Returns the input string with a blue color.

    This function uses the 'colorama' module to add a blue color to the input string. # noqa E501

    Args:
    word (str): A string to add color to.

    Returns:
    A string with a blue color.
    """
    return Fore.BLUE + word + Fore.RESET


def color_black(word: str) -> str:
    """
    Returns the input string with a black color.

    This function uses the 'colorama' module to add a black color to the input string. # noqa E501

    Args:
    word (str): A string to add color to.

    Returns:
    A string with a black color.
    """
    return Fore.BLACK + word + Fore.RESET


def color_green(word: str) -> str:
    """
    Returns the input string with a green color.

    This function uses the 'colorama' module to add a green color to the input string. # noqa E501

    Args:
    word (str): A string to add color to.

    Returns:
    A string with a green color.
    """
    return Fore.GREEN + word + Fore.RESET


def color_blue_light(word: str) -> str:
    """
    Returns the input string with a light blue color.

    This function uses the 'colorama' module to add a light blue color to the input string. # noqa E501

    Args:
    word (str): A string to add color to.

    Returns:
    A string with a light blue color.
    """
    return Fore.LIGHTBLUE_EX + word + Fore.RESET


def clear_screen() -> None:
    """
    Clears the console screen.

    This function uses the 'os' module to determine the current operating system and # noqa E501
    clears the console screen using the appropriate command for that system.

    Args:
    None.

    Returns:
    None.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_map(player1_moves: list[tuple], player2_moves: list[tuple]) -> None:
    """
    Draws the game board with the current moves made by the players.

    Args:
    player1_moves (list[tuple]): A list of tuples representing the moves made by player 1. # noqa E501
    player2_moves (list[tuple]): A list of tuples representing the moves made by player 2. # noqa E501

    Returns:
    None.
    """
    x = 1
    print(color_blue(' _') * 3)
    for row in range(3):
        for col in range(3):
            if (row, col) in player1_moves:
                print(color_blue('|') + color_green('O'), end='')
            elif (row, col) in player2_moves:
                print(color_blue('|') + color_red('X'), end='')
            else:
                print(color_blue('|') + color_black(str(x)), end='')
            x += 1
        print(color_blue('|'))


def check_win(moves: list[tuple]) -> bool:
    """
    Checks if a player has won the game based on their moves.

    Args:
    moves (list[tuple]): A list of tuples representing the moves made by a player. # noqa E501

    Returns:
    A bool indicating whether the player has won the game or not.
    """
    winner_moves = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for win_move in winner_moves:
        if all(move in moves for move in win_move):
            return True
    return False


def game_player1(symbol: str) -> None:
    """
    Plays one turn of the game for player 1.

    Args:
    symbol (str): The symbol used by player 1.

    Returns:
    None.
    """
    while True:
        clear_screen()
        print(color_blue_light('<<< Welcome to the game >>>'))
        draw_map(player1['moves'], player2['moves'])
        choice = input(f'\nEnter move Player {color_green(symbol)}: ')
        if choice in CELLS:
            move = CELLS[choice]
            player1['moves'].append(move)
            CELLS.pop(choice)
            break
        else:
            continue


def game_player2(symbol: str) -> None:
    """
    Plays one turn of the game for player 2.

    Args:
    symbol (str): The symbol used by player 2.

    Returns:
    None.
    """
    clear_screen()
    print(color_blue_light('<<< Welcome to the game >>>'))
    draw_map(player1['moves'], player2['moves'])
    print(f'\nPlaying Player {color_red(symbol)} ...')
    sleep(2)
    choice = random.choice(list(CELLS.keys()))
    move = CELLS[choice]
    player2['moves'].append(move)
    CELLS.pop(choice)


def conditions(o: str, x: str, *players: dict) -> str:
    """
    Determines the game outcome based on the players' states.

    Args:
    o (str): The symbol used by player 1.
    x (str): The symbol used by player 2.
    *players (dict): A variable number of dictionaries representing the state of each player. # noqa E501

    Returns:
    A string representing the game outcome, which could be one of the following: # noqa E501
    - "Player <o> Wins!" if the first player is winning, where <o> is the symbol used by player 1. # noqa E501
    - "Player <x> Wins!" if any other player is winning, where <x> is the symbol used by player 2. # noqa E501
    - "It's a tie!" if no player is winning.
    """
    for index, player in enumerate(players):
        if player['is_winning']:
            if index == 0:
                return f'Player {color_green(o)} Wins!'
            else:
                return f'Player {color_red(x)} Wins!'
    return "It's a tie!"
