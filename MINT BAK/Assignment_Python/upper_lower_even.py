upper=int(input("Enter the upper bound:-"))
lower=int(input("Enter the lower bound:-"))
for i in range(lower,upper):
	if (i%2==0):
		print(i)
	else:
		continue
