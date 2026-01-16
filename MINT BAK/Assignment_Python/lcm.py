import math
def get_lcm(a, b, c):
	def lcm_two(x, y):
		return abs(x * y) // math.gcd(x, y)
	return lcm_two(a, lcm_two(b, c))
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
print("LCM of three number is ",get_lcm(a,b,c))

