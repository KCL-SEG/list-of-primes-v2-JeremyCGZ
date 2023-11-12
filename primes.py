"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    candidate = 2
    if number_of_primes <= 0 :
        raise ValueError("input must be bigger than 0")
    while len(list) < number_of_primes:
        is_prime = True
        for i in range(2, int(candidate**0.5) + 1):
            if candidate % i == 0:
                is_prime = False
                break
        if is_prime:
            list.append(candidate)
        candidate += 1
    return list
