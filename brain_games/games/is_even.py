from random import randint


def get_description():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    
    return description

def get_attributes():
    expression = randint(0, 100)
    correct_answer = 'yes' if expression % 2 == 0 else 'no'
    
    return expression, correct_answer
