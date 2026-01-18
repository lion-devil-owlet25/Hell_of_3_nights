def volume(b,l=10,h=5):
	return l * b * h
print("When the user is given the vaule of the breadth")
b=int(input("Enter the breadth:- "))
print("Volumn:- ",volume(b))
print("When the user is given the values of the new length,breadth and height.")
l=int(input("Enter the length:- "))
b=int(input("Enter the breadth:- "))
h=int(input("Enter the height:- "))
print("Volumn:- ",volume(l,b,h))


