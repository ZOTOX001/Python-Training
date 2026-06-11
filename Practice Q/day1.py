#temp converter:
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)



#palindrome check:
n = input("Enter a word: ")

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


#word counter:
sentence = input("Enter a sentence: ")

words = sentence.split()

print("Number of words:", len(words))




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


#to do list:
tasks = []

task1 = input("Enter first task: ")
tasks.append(task1)

task2 = input("Enter second task: ")
tasks.append(task2)

print("Your Tasks:")
for task in tasks:
    print(task)