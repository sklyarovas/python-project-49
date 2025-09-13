def get_progression(start, diff, steps):
    progression = []

    for step in range(steps):
        current_number = start + step * diff
        progression.append(current_number)

    return progression
