import matplotlib.pyplot as plt
hours= [1, 2, 3, 4, 5, 6, 7]
scores = [40, 45, 55, 65, 70, 80, 90]
plt.scatter(hours, scores)
plt.xlabel("Hours of Practice")
plt.ylabel("Test Scores")
plt.title("Practice Hours vs Coding Scores")
plt.show()

