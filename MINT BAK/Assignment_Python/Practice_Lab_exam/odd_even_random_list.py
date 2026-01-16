import random
a=[random.randint(1,10) for i in range(10)]
odd=[]
even=[]
for i in a:
	if i % 2 ==0:
		even.append(i)
	else:
		odd.append(i)
print("Odd List = ",odd)
print("Even List = ",even)
