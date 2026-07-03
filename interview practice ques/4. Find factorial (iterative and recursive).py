# Find factorial (iterative and recursive).

# Iterative Approach (Using a Loop)
def factorial_iterative(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    result = 1    
    for i in range(1,n+1):
        result *= i
    return result
    
m= int(input("enter the num: "))
k= factorial_iterative(m)
print(k)

# Recursive Approach
def factorial_recursive(n):
    if n < 0:
        return "invalid"
    if n==0 or n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
    
    
a= int(input("enter the number: "))
r= factorial_recursive(a)
print(r)
    