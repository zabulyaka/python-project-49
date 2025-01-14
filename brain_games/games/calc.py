from random import choice, randint

OPERATORS = ['+', '-', '*']


def get_simple_expr() -> str:
    number1 = str(randint(1, 100))
    number2 = str(randint(1, 100))
    operator = choice(OPERATORS)
    return f'{number1} {operator} {number2}'


def calc_expr(game_data: str) -> str:
    return str(eval(game_data))