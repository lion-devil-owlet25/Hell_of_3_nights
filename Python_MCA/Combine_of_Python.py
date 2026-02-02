user = {"name": "Alice", "role": "Scientist"}
print(user["name"])        # Output: Alice
print(user.get("id", 0))   # Returns 0 if "id" is not found
user["lab"] = "Bio-Chem"   # Adds new key
user["role"] = "Senior Scientist" # Updates existing key
user.pop("lab")           # Removes 'lab' and returns its value
del user["name"]          # Removes 'name'
user.clear()              # Empties the dictionary
extra_info = {"OS": "WSL", "Language": "C++"}
user.update(extra_info)
squares = {x: x**2 for x in range(1, 6)}
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
# Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
original = {"a": 1, "b": 2}
swapped = {v: k for k, v in original.items()}
# Output: {1: "a", 2: "b"}
if "OS" in user:
    print("System info available.")
# Standard tuple
system_info = ("Windows", "WSL", 11)

# Singleton tuple (requires a trailing comma)
favorite_lang = ("C++",)
os_name = system_info[0]  # "Windows"
last_item = system_info[-1] # 11
sub_tuple = system_info[0:2] # ("Windows", "WSL")
# Unpacking
os, subsystem, version = system_info
print(len(system_info)) # Output: 3
data = (1, 2, 2, 3)
print(data.count(2)) # Output: 2
print(system_info.index("WSL")) # Output: 1
def get_coordinates():
    return (10.5, 20.3)
print(get_coordinates()) # Output: (10.5, 20.3)
import numpy as np

# Creating arrays
arr = np.array([1, 2, 3, 4], dtype='float64')
matrix = np.zeros((3, 3))  # 3x3 matrix of zeros
linspace = np.linspace(0, 10, 100) # 100 points between 0 and 10

# Mathematical operations (Vectorized)
result = arr * 2 + 10
sin_values = np.sin(linspace)

# Slicing and Indexing
print(arr[1:3]) # Elements at index 1 and 2
import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create the plot
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='Sine Wave', color='blue', linestyle='--')

# Adding metadata
plt.title("Scientific Plotting Example")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Save or Show
# plt.savefig('plot.png')
plt.show()
import numpy as np

# Create a 3x3 identity matrix
id_matrix = np.identity(3)

print(id_matrix)
# Create a 4x4 matrix with ones on the first upper diagonal
upper_diag = np.eye(4, k=1)
int_identity = np.identity(3, dtype=int)
A = np.array([[1, 2], [3, 4]])
I = np.identity(2)

result = A @ I  # Result is equal to A
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# a) Union: All unique elements from both sets
print(set_a.union(set_b))          # {1, 2, 3, 4, 5, 6}

# b) Intersection: Elements common to both
print(set_a.intersection(set_b))   # {3, 4}

# c) Difference: Elements in A but not in B
print(set_a.difference(set_b))     # {1, 2}

# d) issubset: Check if all elements of A are in B
print({3, 4}.issubset(set_a))      # True

# e) issuperset: Check if A contains all elements of another set
print(set_a.issuperset({1, 2}))    # True

data = {"language": "C++", "tool": "WSL"}

# a) Add an item
data["os"] = "Windows"

# b) Modify an item
data["language"] = "Python"

# c) Delete an item
del data["tool"]

# d) Return a list of keys
keys_list = list(data.keys())

# e) Return a list of values
values_list = list(data.values())

# Creates cubes for 1, 3, 5, 7, 9
odd_cubes = {x: x**3 for x in range(1, 11) if x % 2 != 0}
print(odd_cubes)

# 4. Reverse a string
text = "scientist"
reversed_text = text[::-1]

# 5. Check Palindrome
def is_palindrome(s):
        clean_s = s.lower()
        return clean_s == clean_s[::-1]

print(is_palindrome("Radar")) # True

s = "Python3"

print(s.isalnum())      # True (Contains only letters and numbers)
print(s.upper())        # "PYTHON3"
print(s.lower())        # "python3"
print(s.startswith("Py")) # True
print(s.endswith("on"))   # False

import numpy as np

A = np.array([[6, 1], [2, 3]])
B = np.array([[1, 2], [3, 4]])

# a) Inverse
print(np.linalg.inv(A))

# b) Rank
print(np.linalg.matrix_rank(A))

# c) Transpose
print(A.T)

# d) Multiplication
print(np.matmul(A, B)) # or A @ B

# e) Determinant
print(np.linalg.det(A))

# 8. 3x3 Identity Matrix
identity_mtx = np.identity(3)

# 9. 3x2 Matrix filled with 2
twos_mtx = np.full((3, 2), 2)

# 10. 3x3 Matrix with random integers (5 to 9 inclusive)
random_mtx = np.random.randint(5, 10, size=(3, 3))

import matplotlib.pyplot as plt

activities = ['Sleeping', 'Eating', 'Working', 'Playing']
hours = [8, 2, 10, 4]

plt.pie(hours, labels=activities, autopct='%1.1f%%', startangle=90)
plt.title('Daily Activities')
plt.show()

hours_spent = [5, 10, 15, 20, 25, 30, 35]
test_scores = [50, 65, 70, 85, 88, 92, 95]

plt.scatter(hours_spent, test_scores, color='blue')
plt.title('Study Hours vs Coding Scores')
plt.xlabel('Hours Spent Practicing')
plt.ylabel('Test Score')
plt.grid(True)
plt.show()

subjects = ['English', 'Math', 'Science', 'History', 'CompSci']
marks = [85, 92, 78, 88, 95]

plt.bar(subjects, marks, color='green')
plt.title('Student Performance')
plt.xlabel('Subjects')
plt.ylabel('Marks Obtained')
plt.show()

import numpy as np

# 1D Vectors (Inner Product)
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
inner_prod = np.dot(v1, v2)  # (1*4) + (2*5) + (3*6) = 32

# 2D Matrices (Matrix Multiplication)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
matrix_prod = np.dot(A, B)

# Using the @ operator (Cleanest syntax)
result = A @ B

# Using matmul
result_matmul = np.matmul(A, B)

# Example for a 3x3 matrix multiplication
X = np.random.randint(1, 5, (3, 3))
Y = np.random.randint(1, 5, (3, 3))

dot_result = X @ Y
