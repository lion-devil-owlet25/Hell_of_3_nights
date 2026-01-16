def min_three(a, b, c):
	m = a
	if b < m:
		m = b
	if c < m:
		m = c
	return m
a=int(input("Enter the number:-"))
b=int(input("Enter the number:-"))
c=int(input("Enter the number:-"))
print("Minimum = ",min_three(a,b,c))
print("Minimum amoung 54,50 and 60 is ",min_three(a=54,b=50,c=60))

