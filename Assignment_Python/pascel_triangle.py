def factorial(n):
	if n == 0 or n == 1:
		return 1
	return n * factorial(n - 1)
rows = int(input("Enter number of rows: "))
for i in range(rows):
	print("" * (rows - i), end="")
	for j in range(i + 1):
		value = factorial(i) // (factorial(j) * factorial(i - j))
		print(value, end=" ")
	print()
