import prompt


def welcome() -> None:
    print("Welcome to the Brain Games!")


def get_user_name() -> str:
    name = prompt.string('May I have your name? ')
    return name


def greet(name: str = '') -> None:
    print(f'Hello, {name}!')


def print_rules(rules: str) -> None:
    print(rules)


def get_user_answer() -> str:
    answer = prompt.string('Your answer: ')
    return answer


def print_game_data(data: str = '') -> None:
    print(f'Question: {data}')


def print_round_won() -> None:
    print('Correct!')


def print_win(name: str = '') -> None:
    print(f'Congratulations, {name}!')


def print_loss(name: str = '', answer: str = '', expected: str = '') -> None:
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{expected}'.")
    print(f"Let's try again, {name}!")

