from brain_games.cli import welcome_user, game_description, dialogue, success, fail, congratulations
from brain_games.games import calc, gcd, is_even, progression


def get_game_data(game_name, data_type):
    match game_name, data_type:
        case 'is_even', 'description':
            return is_even.get_description()
        case 'is_even', 'attributes':
            return is_even.get_attributes()

        case 'calc', 'description':
            return calc.get_description()
        case 'calc', 'attributes':
            return calc.get_attributes()

        case 'gcd', 'description':
            return gcd.get_description()
        case 'gcd', 'attributes':
            return gcd.get_attributes()

        case 'progression', 'description':
            return progression.get_description()
        case 'progression', 'attributes':
            return progression.get_attributes()
        case _:
            return

def core(game_name):
    name = welcome_user()
    description = get_game_data(game_name, 'description')

    game_description(description)

    for _ in range(3):
        expression, correct_answer = get_game_data(game_name, 'attributes')
        user_answer = dialogue(expression)

        if correct_answer == user_answer:
            success()
        else:
            fail(user_answer, correct_answer, name)
            return

    congratulations(name)
