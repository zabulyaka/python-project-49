from brain_games.games.calc import get_calc_data
from brain_games.games.even import get_even_data
from brain_games.games.gcd import get_gcd_data
from brain_games.games.prime import get_prime_data
from brain_games.games.progression import get_progression_data

ROUNDS = 3
RULES_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'
RULES_CALC = 'What is the result of the expression?'
RULES_GCD = 'Find the greatest common divisor of given numbers.'
RULES_PROGRESSION = 'What number is missing in the progression?'
RULES_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
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
        case 'progression':
            rules = RULES_PROGRESSION
        case 'prime':
            rules = RULES_PRIME
        case _:
            rules = GAME_ERROR
    return rules


def get_rounds() -> int:
    rounds = ROUNDS
    return rounds


def get_data(game: str) -> tuple:
    game_data = ''
    expected_answer = ''
    result = (game_data, expected_answer)
    match game:
        case 'even':
            result = get_even_data()
        case 'calc':
            result = get_calc_data()
        case 'gcd':
            result = get_gcd_data()
        case 'progression':
            result = get_progression_data()
        case 'prime':
            result = get_prime_data()
        case _:
            result = (GAME_ERROR, GAME_ERROR)
    return result
