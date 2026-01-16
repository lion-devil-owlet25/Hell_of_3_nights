#List Cloning
a=[1,2,3,5,6,4,5,6,8]
b=a.copy()
print("Using copy method")
print("Original List =" ,a)
b.append(56)
print("List Cloning = ",b)
#List Aliasing
c=[5,6,10,12,13]
v=c
v[3]=200
print("Original List = ",c)
print("List Aliasing = ",v)
