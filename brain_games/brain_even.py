from random import randint

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
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_odd(num: int) -> bool:
    return bool(num % 2)


def guess_even():
    welcome()
    user_name = get_user_name()
    greet(user_name)
    print_rules(RULES)
    game_rounds = ROUNDS
    game_end = False
    while not game_end:
        game_data = randint(1, 100)
        print_game_data(str(game_data))
        user_answer = get_user_answer()
        expected_answer = 'no' if is_odd(game_data) else 'yes'
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