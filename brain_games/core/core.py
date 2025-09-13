from brain_games.cli import (
    congratulations,
    dialogue,
    fail,
    game_description,
    success,
    welcome_user,
    )
from brain_games.games import calc, gcd, is_even, is_prime, progression


def get_data(game_name, data_type):
    funcs = {
        "calc_description": calc.get_description(),
        "calc_attributes": calc.get_attributes(),
        "gcd_description": gcd.get_description(),
        "gcd_attributes": gcd.get_attributes(),
        "is_even_description": is_even.get_description(),
        "is_even_attributes": is_even.get_attributes(),
        "is_prime_description": is_prime.get_description(),
        "is_prime_attributes": is_prime.get_attributes(),
        "progression_description": progression.get_description(),
        "progression_attributes": progression.get_attributes()
    }

    choice = f'{game_name}_{data_type}'
    func = funcs.get(choice, None)

    return func


def core(game_name):
    name = welcome_user()
    description = get_data(game_name, 'description')

    game_description(description)

    for _ in range(3):
        expression, correct_answer = get_data(game_name, 'attributes')
        user_answer = dialogue(expression)

        if correct_answer == user_answer:
            success()
        else:
            fail(user_answer, correct_answer, name)
            return

    congratulations(name)
