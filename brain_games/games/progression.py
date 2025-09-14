from brain_games.utils.math import get_progression
from brain_games.utils.randomizer import get_number


def get_description():
    description = 'What number is missing in the progression?'
    input_type = 'int'
    
    return description, input_type


def mask_progression(progression, masked_step):
    tmp = progression.copy()
    tmp[masked_step] = '..'
    masked = ' '.join(map(str, tmp))

    return masked


def get_attributes():
    start_range = [1, 20]
    diff_range = [1, 10]
    steps_range = [5, 10]

    start = get_number(*start_range)
    diff = get_number(*diff_range)
    steps = get_number(*steps_range)
    masked_step = get_number(0, steps - 1)
    progression = get_progression(start, diff, steps)

    expression = mask_progression(progression, masked_step)
    correct_answer = progression[masked_step]
    
    return expression, correct_answer
