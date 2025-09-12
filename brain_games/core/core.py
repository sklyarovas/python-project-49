from brain_games.cli import welcome_user, game_description, dialogue, success, fail, congratulations
from brain_games.games import is_even, calc


def core(game_name):
    name = welcome_user()

    match game_name:
        case 'is_even':
            description = is_even.get_description()
        case 'calc':
            description = calc.get_description()
        case _:
            return

    game_description(description)

    for _ in range(3):
        match game_name:
            case 'is_even':
                value, correct_answer = is_even.get_attributes()
            case 'calc':
                value, correct_answer = calc.get_attributes()
        answer = dialogue(value)
        if correct_answer == answer:
            success()
        else:
            fail(answer, correct_answer, name)
            return

    congratulations(name)
