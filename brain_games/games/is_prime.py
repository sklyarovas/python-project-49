from brain_games.utils import get_number, is_prime


def get_description():
    description = (
        'Answer "yes" if given number is prime. '
        'Otherwise answer "no".'
        )
    input_type = 'str'
    
    return description, input_type


def get_attributes():
    num_range = [1, 100]

    expression = get_number(*num_range)
    correct_answer = 'yes' if is_prime(expression) is True else 'no'
    
    return expression, correct_answer