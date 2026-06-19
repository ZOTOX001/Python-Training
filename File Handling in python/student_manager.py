# FILE HANDLING COMPLETE EXAMPLE

# 1. Write Mode (creates file / overwrites old data)
with open("students.txt", "w") as file:
    file.write("Aniket,85\n")
    file.write("Rahul,90\n")
    file.write("Priya,78\n")

print("Initial records written.")

# 2. Append Mode
with open("students.txt", "a") as file:
    file.write("Aman,88\n")

print("New record appended.")

# 3. Read Entire File
print("\n--- Complete File Data ---")

with open("students.txt", "r") as file:
    data = file.read()

print(data)

# 4. Read Line by Line
print("--- Line By Line Reading ---")

with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())

# 5. Readlines()
print("\n--- Using readlines() ---")

with open("students.txt", "r") as file:
    lines = file.readlines()

print(lines)

# 6. Search Student
search_name = "Rahul"
found = False

with open("students.txt", "r") as file:
    for line in file:

        name, marks = line.strip().split(",")

        if name == search_name:
            print("\nStudent Found")
            print("Name:", name)
            print("Marks:", marks)
            found = True
            break

if not found:
    print("Student Not Found")

# 7. Count Records
with open("students.txt", "r") as file:
    total_students = len(file.readlines())

print("\nTotal Students:", total_students)