#Write a function prime_series(n) that returns the first n prime numbers.
def prime_series(n):

    primes = []
    num = 2

    while len(primes) < n:

        is_prime = True

        for i in range(2, num):

            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

        num += 1

    return primes


print(prime_series(10))