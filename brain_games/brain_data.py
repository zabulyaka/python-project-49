from brain_games.games.calc import calc_expr, get_simple_expr
from brain_games.games.even import eval_even, get_small_int
from brain_games.games.gcd import get_gcd, get_two_ints

ROUNDS = 3
RULES_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'
RULES_CALC = 'What is the result of the expression?'
RULES_GCD = 'Find the greatest common divisor of given numbers.'
GAME_ERROR = "Error: game doesn't match"


def get_rules(game: str) -> str:
    rules = ''
    match game:
        case 'even':
            rules = RULES_EVEN
        case 'calc':
            rules = RULES_CALC
        case 'gcd':
            rules = RULES_GCD
        case _:
            rules = GAME_ERROR
    return rules


def get_rounds() -> int:
    rounds = ROUNDS
    return rounds


def get_data(game: str) -> tuple:
    game_data = ''
    expected_answer = ''
    match game:
        case 'even':
            game_data = get_small_int()
            expected_answer = eval_even(game_data)
        case 'calc':
            game_data = get_simple_expr()
            expected_answer = calc_expr(game_data)
        case 'gcd':
            game_data = get_two_ints()
            expected_answer = get_gcd(game_data)
        case _:
            game_data = GAME_ERROR
            expected_answer = GAME_ERROR
    return (game_data, expected_answer)
