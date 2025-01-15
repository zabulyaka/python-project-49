from random import choice, randint

OPERATORS = ['+', '-', '*']


def get_simple_expr() -> str:
    num1 = str(randint(1, 100))
    num2 = str(randint(1, 100))
    operator = choice(OPERATORS)
    return f'{num1} {operator} {num2}'


def calc_expr(game_data: str) -> str:
    return str(eval(game_data))