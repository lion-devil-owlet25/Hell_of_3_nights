def rec_gcd(a, b):
	if b == 0:
		return a
	return rec_gcd(b, a % b)
a=int(input("Enter the number:-"))
b=int(input("Enter the number:-"))
print("GCD of ",a,"and",b,"is ",rec_gcd(a,b))
