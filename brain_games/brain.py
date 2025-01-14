from brain_games.brain_data import get_expected_answer, get_game_data, get_rules
from brain_games.brain_io import (
    get_user_answer,
    get_user_name,
    greet,
    print_game_data,
    print_loss,
    print_round_won,
    print_rules,
    print_win,
    welcome,
)

ROUNDS = 3


def run_game(game: str) -> None:
    welcome()
    user_name = get_user_name()
    greet(user_name)
    rules = get_rules(game)
    print_rules(rules)
    game_rounds = ROUNDS
    game_end = False
    while not game_end:
        game_data = get_game_data(game)
        print_game_data(game_data)
        user_answer = get_user_answer()
        expected_answer = get_expected_answer(game, game_data)
        round_won = user_answer == expected_answer
        if round_won:
            print_round_won()
            game_rounds -= 1
        else:
            print_loss(user_name, user_answer, expected_answer)
            break
        game_end = game_rounds < 1
    if not game_rounds:
        print_win(user_name)