from game.models.players import (
    player1,
    player2
)
from game.utils.funcs import (
    game_player1,
    game_player2,
    check_win,
    draw_map,
    clear_screen,
    conditions
)


def play_game() -> None:
    """
    Plays a game of Tic Tac Toe between two players.

    This function starts a game between two players, represented by the 'player1' and 'player2' global dictionaries. # noqa E501
    The game alternates between each player, with 'O' representing the first player and 'X' representing the second. # noqa E501
    The function checks for a win or a tie after each move, and ends the game when one of these conditions is met. # noqa E501
    The function then prints the final game state, including the moves made by each player and the game outcome. # noqa E501

    Args:
    None.

    Returns:
    None.
    """
    o, x = 'O', 'X'
    while True:
        clear_screen()
        game_player1(o)
        if check_win(player1['moves']):
            player1['is_winning'] = True
            break
        if len(player1['moves']) + len(player2['moves']) == 9:
            break
        game_player2(x)
        if check_win(player2['moves']):
            player2['is_winning'] = True
            break
    clear_screen()
    draw_map(player1['moves'], player2['moves'])
    print(conditions(o, x, player1, player2))
