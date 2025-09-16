from brain_games.scripts.utils import get_number


def get_description():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    input_type = 'str'
    
    return description, input_type


def get_attributes():
    num_range = [0, 100]

    expression = get_number(*num_range)
    correct_answer = 'yes' if expression % 2 == 0 else 'no'
    
    return expression, correct_answer
