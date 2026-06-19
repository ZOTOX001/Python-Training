#Write a function fibonacci(n) that returns the first n numbers of the Fibonacci series.
def fibonacci(n):
    series = []
    a,b = 0,1
    for i in range(n):
        series.append(a)
        a,b = b,a+b    
    return series
print(fibonacci(10))