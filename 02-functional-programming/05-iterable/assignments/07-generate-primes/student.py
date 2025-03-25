def is_prime(getal):
    if getal <= 1:
        return False
    for i in range(2, int(getal**0.5) + 1):
        if getal % i == 0:
            return False
    return True

def primes():
    current = 0
    while True:
        if is_prime(current):
            yield current
        current += 1
        