from random import randint


def find_gcd(num1: int, num2: int) -> int:
    return num2 if not num1 % num2 else find_gcd(num2, num1 % num2)


def get_gcd_data() -> tuple:
    two_nums = ''
    gcd = ''
    result = (two_nums, gcd)
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    gcd = find_gcd(num1, num2)
    result = (f'{str(num1)} {str(num2)}', str(gcd))
    return result