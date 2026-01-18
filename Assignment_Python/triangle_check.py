a=int(input("Enter the first side of the triangle:-"))
b=int(input("Enter the second side of the triangle:-"))
c=int(input("Enter the third side of the triangle:-"))
if(a==b==c):
	print("Equilateral Triangle")
elif(a==b or a==c or b==c or a==b):
	print("Isosceles Triangle")
else:
	print("Scalene Triangle")
