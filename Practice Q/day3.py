# create a function named hello and call it:
def hello():
    print("function called")

hello()


#using parameters in function and providing arguments:
def sum(a,b):
    print("Sum =", a + b)
sum(3,5)
sum(10,20)    
sum(7,8)


#create a palindrome checker function:
def palindrome(word):
    rev=""
    for i in range(len(word)-1,-1,-1):
        rev += word[i]

    if rev ==word:
            print("Palindrome")
    else:
            print("Not Palindrome")
            
palindrome("Aniket")
palindrome("naman")


#using return statement in function:
def hello():
    return "hello aniket"
print(hello())


keyword arguments:
def student(name, age):
    print(name, age)

student(age=21, name="Aniket")


# Show difference between local and global variables:
x = 100

def test():
    x = 50
    print("Local:", x)

test()
print("Global:", x)


#Create a list of squares using list comprehension:
squares = [x**2 for x in range(1, 6)]

print(squares)


#Create a dictionary of numbers and squares using dictionary comprehension:
data = {x: x**2 for x in range(1, 6)}

print(data)


#using *args in function (note *args uses tuple to store values):
def info(name, *marks, **details):

    print("Name:", name)

    print("\nMarks:")
    for i in marks:
        print(i)

    print("\nDetails:")
    for key, value in details.items():
        print(key, "=", value)


info(
    "Aniket",
    85, 90, 95,
    age=21,
    city="Delhi"
)


# **kwargs 
# * Keys and values are needed
# * Number of keyword inputs is unknown
# * Flexible dictionary-like input is required
#     ** is mandatory
# * kwargs is variable name
# **kwargs stores data as a dictionary
# code:

def info(course, **students):

    print("Course:", course)

    for key, value in students.items():
        print(key, "=", value)

info("Python", name="Aniket", age=21)


# Combined Example of *args and **kwargs:
def complete_info(*args, **kwargs):

    print("Args:", args)
    print("Kwargs:", kwargs)

complete_info(1, 2, 3, name="Aniket", age=21)