#Write a function fibonacci_range(start, limit) that returns Fibonacci numbers within a given range.
def fibonacci_range(start, limit):
    range=[]
    a,b = 0,1
    while a <= limit:
        if a >= start:
            range.append(a)
        a,b = b,a+b
    return range
print(fibonacci_range(10,100))
