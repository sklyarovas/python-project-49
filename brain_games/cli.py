import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name

def game_description(description):
    print(description)

def dialogue(expression):
    print(f'Question: {expression}')
    user_answer = prompt.string('Your answer: ')
    return user_answer

def success():
    print('Correct!')

def fail(user_answer, correct_answer, name):
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n"
    f"Let's try again, {name}!")

def congratulations(name):
    print(f'Congratulations, {name}!')
    