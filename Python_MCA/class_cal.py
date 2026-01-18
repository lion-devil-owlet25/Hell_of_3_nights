class Cal:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def add(a,b):
		return a+b
	def sub(a,b):
		return a-b
	def mul(a,b):
		return a*b
	def div(a,b):
		return a//b
	def modulus(a,b):
		return a%b
a=int(input("Enter the number:-"))
b=int(input("Enter the number:-"))
print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")
print("Press 5 for Modulus")
choice=int(input("Enter your choice:-"))
if choice==1:
	print(Cal.add(a,b))
elif choice==2:
	print(Cal.sub(a,b))
elif choice==3:
	print(Cal.mul(a,b))
elif choice==4:
	print(Cal.div(a,b))
elif choice==5:
	print(Cal.modulus(a,b))
else:
	print("Invaild choice")	
