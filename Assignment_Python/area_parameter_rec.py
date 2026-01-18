class Rectangle:
	def __init__(self,l,b):
		self.l = l
		self.b = b
	def area(self):
		return self.l * self.b
	def perimeter(self):
		return 2 * (self.l + self.b)
l=int(input("Enter the lenght of rectangle:- "))
b=int(input("Enter the breadth of rectangle:- "))
r=Rectangle(l,b)
print("Area of Rectangle:-",r.area())
print("Perimeter of Rectangle:-",r.perimeter())
