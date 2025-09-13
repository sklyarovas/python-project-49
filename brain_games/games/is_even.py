from brain_games.utils.randomizer import get_number


def get_description():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    
    return description

def get_attributes():
    expression = get_number(0, 100)
    correct_answer = 'yes' if expression % 2 == 0 else 'no'
    
    return expression, correct_answer
