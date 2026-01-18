def string_palindrome(s):
	rev=s[::-1]
	if (s==rev):
		print(s," is Palindrome ")
	else:
		print(s," is not Palindrome")
def num_palindrome(n):
	rev=0
	a=n
	while a > 0:
		l=a%10
		rev=(rev*10)+l
		a=a//10
	if (n==rev):
		print(n," is Palindrome number")
	else:
		print(n," is not Palindrome number")
s=input("Enter a string:-")
string_palindrome(s)
n=int(input("Enter the number:-"))
num_palindrome(n)
		
		
