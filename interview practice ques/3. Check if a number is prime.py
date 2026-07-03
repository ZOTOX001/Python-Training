# 3. Check if a number is prime.
def is_prime(s):
    if s <=1:
        return False

    for i in range(2, s):
            if s % i == 0:
                return False
    return True
            
a = int(input("Enter a number: "))        
result= is_prime(a)
if result:
    print("prime number")
else:
    print("not prime")