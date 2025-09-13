def get_gcd(a, b):
    if b > a:
        a, b = b, a
    while b:
        a, b = b, a % b

    return str(a)
