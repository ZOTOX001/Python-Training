#Write a function armstrong_series(limit) that returns all Armstrong numbers up to a limit.
def armstrong_series(limit):

    result = []

    for num in range(1, limit + 1):

        digits = str(num)
        power = len(digits)

        total = 0

        for digit in digits:
            total += int(digit) ** power

        if total == num:
            result.append(num)

    return result


print(armstrong_series(1000))