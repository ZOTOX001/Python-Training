# creata a dictonary of a student:
student = {
    "name": "Aniket Singh",
    "age": 20,
    "grade": "A"
}
print(student["age"])


# check for even or odd using if else:
n= int(input("Enter a number: "))
if n % 2==0:
    print("even")
else:
    print("odd")


#Greatest of 2 numbers using if else statements:
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
if n1 > n2:
    print("Greater number is:", n1)
elif n2 > n1:
    print("Greater number is:", n2)
else:
    print("Both numbers are equal")


#grade calculator:
n= int(input("Enter marks: "))
if n >= 90:
    print("Grade: A")
elif n >= 80:
    print("Grade: B")
elif n >= 70:
    print("Grade: C")
elif n >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# number 1 to 10 using for loop:
for i in range(1,11,1):
        print(i)


# Print multiplication table of a number using for loop:
n= int(input("Enter a number: "))
for i in range(n,n*10+1,n):
        print(i)


# Sum of first n numbers
n= int(input("Enter a number: "))
total = 0
for i in range(1,n+1):
    total += i
print("Sum =", total)


#while Loop:
i = 1

while i <= 5:
    print(i)
    

# Break statement:
for i in range(1, 10):
    if i == 5:
        break
    print(i)


# Continue statement:
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# Number Guessing Game:
secret = 7

while True:
    guess = int(input("Guess number: "))

    if guess == secret:
        print("Correct!")
        break
    else:
        print("Try Again")


# Password Checker using while loop:
password = "python123"

while True:
    user = input("Enter password: ")

    if user == password:
        print("Access Granted")
        break
    else:
        print("Wrong Password")


# Countdown Timer using while loop:
i = 5

while i >= 1:
    print(i)
    i -= 1

print("Blast Off!")