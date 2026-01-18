student = {"name": "Amit", "age": 20, "course": "BCA"}

# a) Add an item
student["marks"] = 85

# b) Modify an item
student["age"] = 21

# c) Delete an item
del student["course"]

# d) Return list of keys
print("Keys:", list(student.keys()))

# e) Return list of values
print("Values:", list(student.values()))

print("Dictionary:", student)

