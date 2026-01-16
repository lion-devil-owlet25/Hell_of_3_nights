#Map() function
numbers=[1,2,3,4]
squared=list(map(lambda x:x**2,numbers))
print("Original List = ",numbers)
print("Mapping List = ",squared)
#filter() function
a=[1,2,3,4,5,6]
filtered=list(filter(lambda x:x>3,a))
print("Original List = ",a)
print("Filter List = ",filtered)
#reduce() function
from functools import reduce
b=[1,2,3,4]
total=reduce(lambda x,y:x+y,b)
print("Original List = ",b)
print("Total List = ",total)
