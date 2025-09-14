from brain_games.utils.randomizer import get_number, make_choice


def get_description():
    description = 'What is the result of the expression?'
    
    return description


def get_attributes():
    operand_range = [0, 10]
    operators = ['+', '-', '*']

    operator = make_choice(operators)
    operand1 = get_number(*operand_range)
    operand2 = get_number(*operand_range)

    expression = f'{operand1} {operator} {operand2}'
    
    match operator:
        case '+':
            correct_answer = str(operand1 + operand2)
        case '-':
            correct_answer = str(operand1 - operand2)
        case '*':
            correct_answer = str(operand1 * operand2)
    
    return expression, correct_answer
