def find(x,y):
	if(x>y):
		return x
	elif(y>x):
		return y
	else:
		return x
x=int(input("Enter the number:-"))
y=int(input("Enter the number:-"))
print("Maximum",x,"and",y,"=",find(x,y))
a=int(input("Enter the number:-"))
b=int(input("Enter the number:-"))
print("Maximum",a,"and",b,"=",find(a,b))
