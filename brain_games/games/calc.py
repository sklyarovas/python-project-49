from random import choice, randint


def get_description():
    description = 'What is the result of the expression?'
    
    return description

def get_attributes():
    operators = ['+', '-', '*']
    operator = choice(operators)
    operand1 = randint(0, 10)
    operand2 = randint(0, 10)

    expression = f'{operand1} {operator} {operand2}'
    
    match operator:
        case '+':
            correct_answer = str(operand1 + operand2)
        case '-':
            correct_answer = str(operand1 - operand2)
        case '*':
            correct_answer = str(operand1 * operand2)
    
    return expression, correct_answer
