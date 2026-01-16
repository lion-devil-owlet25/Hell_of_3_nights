def series(n):
	t = 0
	for i in range(1, n + 1):
		m = i * (i + 1)
		if i % 2 == 0:
			t -= m
		else:
			t += m
	return t
n=int(input("Enter the number of rows:-"))
print("Sum of the series =", series(n))

