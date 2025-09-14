from brain_games.utils.math import get_gcd
from brain_games.utils.randomizer import get_number


def get_description():
    description = 'Find the greatest common divisor of given numbers.'
    
    return description


def get_attributes():
    num_range = [0, 50]

    num1 = get_number(*num_range)
    num2 = get_number(*num_range)

    expression = f'{num1} {num2}'
    correct_answer = get_gcd(num1, num2)
    
    return expression, correct_answer
