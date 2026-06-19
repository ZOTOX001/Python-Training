#Write a function sum_of_series(n) that returns 1 + 1/2 + 1/3 + ... + 1/n
def sum_of_series(n):
    sum=0
    for i in range(1,n+1):
        sum += 1/i
    return sum
print(sum_of_series(5))
