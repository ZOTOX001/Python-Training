#Write a function collatz(n) that returns the Collatz sequence (if even, halve it; if odd, 3n+1; until it reaches 1).
def collatz(n):

    sequence = []

    while True:

        sequence.append(n)

        if n == 1:
            break

        elif n % 2 == 0:
            n = n // 2

        else:
            n = 3 * n + 1

    return sequence
print(collatz(6))
