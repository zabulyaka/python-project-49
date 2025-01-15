from random import randint


def find_smallest_div(num, div=2) -> int:
    if not num % div:
        return div
    else:
        if div == 2:
            div -= 1
        return find_smallest_div(num, div + 2)


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    return num == find_smallest_div(num)


def get_prime_data() -> tuple:
    num = ''
    num_is_prime = ''
    result = (num, num_is_prime)
    num = randint(1, 100)
    num_is_prime = 'yes' if is_prime(num) else 'no'
    result = (str(num), num_is_prime)
    return result