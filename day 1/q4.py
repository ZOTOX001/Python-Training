#min,max,average:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

maximum = num1
if num2 > maximum:
    maximum = num2
if num3 > maximum:
    maximum = num3

minimum = num1
if num2 < minimum:
    minimum = num2
if num3 < minimum:
    minimum = num3

average = (num1 + num2 + num3) / 3

print("Maximum =", maximum)
print("Minimum =", minimum)
print("Average =", average)
