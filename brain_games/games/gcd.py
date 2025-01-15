from random import randint


def find_gcd(num1: int, num2: int) -> int:
    return num2 if not num1 % num2 else find_gcd(num2, num1 % num2)


def get_two_ints() -> str:
    num1 = str(randint(1, 100))
    num2 = str(randint(1, 100))
    return f'{num1} {num2}'


def get_gcd(game_data) -> str:
    (num1, num2) = game_data.split(' ')
    num1 = int(num1)
    num2 = int(num2)
    gcd = find_gcd(num1, num2)
    return str(gcd)