sub1=int(input("Enter the marks of first subject:-"))
sub2=int(input("Enter the marks of the second subject:-"))
sub3=int(input("Enter the marks of the third subject:-"))
per=((sub1+sub2+sub3)/300)*100
if (per>=60):
	print(f"Your percentage of marks:-{per:.2f}%")
	print("First Division")
if(per==50 and per>=59):
	print(f"Your percentage of marks:-{per:.2f}%")
	print("Second Division")
if(per==40 and per>=49):
	print(f"Your percentage of marks:-{per:.2f}%")
	print("Third Division")
if(per<40):
	print(f"Your percentage of marks:-{per:.2f}%")
	print("Fail")
	
