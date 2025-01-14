from random import randint


def is_odd(num: int) -> bool:
    return bool(num % 2)


def get_small_int() -> str:
    return str(randint(1, 10))


def eval_even(game_data: str) -> str:
    return 'no' if is_odd(int(game_data)) else 'yes'