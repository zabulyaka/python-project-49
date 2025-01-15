from random import randint


def is_odd(num: int) -> bool:
    return bool(num % 2)


def get_even_data() -> tuple:
    num = ''
    num_is_even = ''
    result = (num, num_is_even)
    num = randint(1, 10)
    num_is_even = 'no' if is_odd(num) else 'yes'
    result = (str(num), num_is_even)
    return result