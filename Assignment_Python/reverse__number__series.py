n=int(input("Enter the number:-"))
for i in range(1,n+1):
	x=n
	for j in range(1,i+1):
		print(x,end="")
		x-=1
	print("")
