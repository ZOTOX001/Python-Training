#Write a function perfect_numbers(limit) that returns all perfect numbers up to a limit (a number equal to the sum of its divisors, e.g. 6 = 1+2+3).
def perfect_numbers(limit):

    result = []

    for num in range(1, limit + 1):

        divisor_sum = 0

        for i in range(1, num):

            if num % i == 0:
                divisor_sum += i

        if divisor_sum == num:
            result.append(num)

    return result


print(perfect_numbers(1000))