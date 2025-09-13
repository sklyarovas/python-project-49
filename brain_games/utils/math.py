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


def is_prime(num):
    if num in [2, 3]:
        return True
    if num < 2 or num % 2 == 0:
        return False

    for i in range(3, num - 1, 2):
        if num % i == 0:
            return False
    
    return True
