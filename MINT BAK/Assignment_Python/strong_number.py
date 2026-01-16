a=int(input("Enter a number:-"))
b=a
sum_digits=0
def fact(n):
    fact=1
    for i in range(1, n + 1):
    	fact *= i
    return fact
while a>0:
	digit=a%10
	sum_digits+=fact(digit)
	a=a//10
if (sum_digits == b):
	print(b,"is strong number")
else:
	print(b,"is not strong number")
