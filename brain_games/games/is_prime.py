from brain_games.utils.math import is_prime
from brain_games.utils.randomizer import get_number


def get_description():
    description = (
        'Answer "yes" if given number is prime. '
        'Otherwise answer "no".'
        )
    
    return description


def get_attributes():
    num_range = [1, 100]

    expression = get_number(*num_range)
    correct_answer = 'yes' if is_prime(expression) is True else 'no'
    
    return expression, correct_answer