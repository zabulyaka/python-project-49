from random import choice, randint

OPERATORS = ['+', '-', '*']


def get_calc_data() -> tuple:
    expr = ''
    expr_res = ''
    result = (expr, expr_res)
    num1 = str(randint(1, 20))
    num2 = str(randint(1, 20))
    operator = choice(OPERATORS)
    expr = f'{num1} {operator} {num2}'
    expr_res = str(eval(expr))
    result = (expr, expr_res)
    return result