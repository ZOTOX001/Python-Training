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
