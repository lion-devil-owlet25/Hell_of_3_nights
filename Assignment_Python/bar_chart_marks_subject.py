import matplotlib.pyplot as plt
subjects = ['English', 'Math', 'Science', 'History', 'Computer']
marks = [70, 85, 78, 68, 90]
plt.bar(subjects, marks)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()

