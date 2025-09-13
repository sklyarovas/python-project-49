from brain_games.utils.math import get_progression
from brain_games.utils.randomizer import get_number


def get_description():
    description = 'What number is missing in the progression?'
    
    return description


def mask_progression(progression, masked_step):
    tmp = progression.copy()
    tmp[masked_step] = '..'
    masked = ' '.join(map(str, tmp))

    return masked


def get_attributes():
    start = get_number(1, 20)
    diff = get_number(1, 10)
    steps = get_number(5, 10)
    masked_step = get_number(0, steps - 1)
    progression = get_progression(start, diff, steps)

    expression = mask_progression(progression, masked_step)
    correct_answer = str(progression[masked_step])
    
    return expression, correct_answer
