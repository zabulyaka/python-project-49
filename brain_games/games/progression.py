from random import randint


def get_progression_data() -> tuple:
    progression = ''
    missing_num = ''
    result = (progression, missing_num)
    progression_length = randint(5, 10)
    progression_start = randint(1, 10)
    progression_step = randint(1, 10)
    progression = [str(progression_start)]
    elem = progression_start
    for i in range(1, progression_length):
        elem += progression_step
        progression.append(str(elem))
    missing_num_pos = randint(0, progression_length - 1)
    missing_num = progression[missing_num_pos]
    progression[missing_num_pos] = '..'
    result = (' '.join(progression), missing_num)
    return result