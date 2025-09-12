from random import randint


def get_description():
    description = 'Find the greatest common divisor of given numbers.'
    
    return description

def get_gcd(a, b):
    if b > a:
        a, b = b, a
    while b:
        a, b = b, a % b

    return str(a)

def get_attributes():
    a = randint(0, 50)
    b = randint(0, 50)

    expression = f'{a} {b}'
    correct_answer = get_gcd(a, b)
    
    return expression, correct_answer
