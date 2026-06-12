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

