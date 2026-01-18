def fib_pat(n):
	fib = [1, 1]
	for i in range(n - 2):
		fib.append(fib[-1] + fib[-2])
	for i in range(n, 0, -1):
		for j in range(i):
			print(fib[j], end="")
		print()
n=int(input("Enter the number of rows:-"))
fib_pat(n)

