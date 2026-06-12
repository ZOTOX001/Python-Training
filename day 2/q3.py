#Greatest of 2 numbers using if else statements:
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
if n1 > n2:
    print("Greater number is:", n1)
elif n2 > n1:
    print("Greater number is:", n2)
else:
    print("Both numbers are equal")
