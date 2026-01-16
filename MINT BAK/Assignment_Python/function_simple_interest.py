def simple_interest(p=1000, r=10, t=5):
	return ((p * r * t) / 100)
a=int(input("Enter the principle:- "))
b=int(input("Enter the rate:- "))
c=int(input("Enter the time:- "))
print("Performing all the new values that you have given ")
print("Simple interest = ",simple_interest(a,b,c))
print("When the time is not given")
d=int(input("Enter the principle:- "))
e=int(input("Enter the rate:- "))
print("Simple interest = ",simple_interest(d,e))
print("When all the values are not given by the user")
print("Simple interest = ",simple_interest())


