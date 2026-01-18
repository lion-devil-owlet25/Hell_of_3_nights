def rec_factorial(n):
	if n == 0 or n == 1:
		return 1
	return n * rec_factorial(n - 1)
n=int(input("Enter a number:-"))
print("Factorial (using recursion) = ",rec_factorial(n))
