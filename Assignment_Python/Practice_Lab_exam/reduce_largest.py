from functools import reduce
a=[1,2,5,4,9,10,55,41]
b=reduce(lambda x,y:x if x>y else y,a)
print("Largest element in the list = ",b)

