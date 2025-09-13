def get_gcd(a, b):
    if b > a:
        a, b = b, a
    while b:
        a, b = b, a % b

    return str(a)

def get_progression(start, diff, steps):
    progression = []

    for step in range(steps):
        current_number = start + step * diff
        progression.append(current_number)

    return progression
