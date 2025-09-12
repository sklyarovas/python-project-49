import prompt
from random import randint


def is_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}\n'
    f'Answer "yes" if the number is even, otherwise answer "no".')

    correct_unswer = ''

    for i in range(3):
        number = randint(0,100)
        correct_unswer = 'yes' if number % 2 == 0 else 'no'

        print(f'Question: {number}')
        unswer = prompt.string('Your answer: ')

        if correct_unswer == unswer.lower(): # Приводим ответ к нижнему регистру
            print('Correct!')
        else:
            print(f"'{unswer}' is wrong answer ;(. Correct answer was '{correct_unswer}'.\n"
            f"Let's try again, Bill!")
            return

    print('Congratulations, Bill!')
