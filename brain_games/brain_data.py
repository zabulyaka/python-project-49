from brain_games.games.calc import calc_expr, get_simple_expr
from brain_games.games.even import eval_even, get_small_int

RULES_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'
RULES_CALC = 'What is the result of the expression?'
GAME_ERROR = "Error: game doesn't match"


def get_rules(game: str) -> str:
    result = ''
    match game:
        case 'even':
            result = RULES_EVEN
        case 'calc':
            result = RULES_CALC
        case _:
            result = GAME_ERROR
    return result


def get_game_data(game: str) -> str:
    result = ''
    match game:
        case 'even':
            result = get_small_int()
        case 'calc':
            result = get_simple_expr()
        case _:
            result = GAME_ERROR
    return result


def get_expected_answer(game: str, game_data: str) -> str:
    result = ''
    match game:
        case 'even':
            result = eval_even(game_data)
        case 'calc':
            result = calc_expr(game_data)
        case _:
            result = GAME_ERROR
    return result