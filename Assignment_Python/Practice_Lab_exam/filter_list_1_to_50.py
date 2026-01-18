a=[]
for i in range(1,51):
	a.append(i)
b=filter(lambda x:(x%3==0 or x%6==0),a)
print("Original List = ",a)
print("Filter List = ",list(b))
