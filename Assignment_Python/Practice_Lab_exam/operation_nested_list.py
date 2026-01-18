a=[1,2,5,6,['M','L','K','N'],10]
print("Nested List = ",a)
a.append(50)
print("Append List = ",a)
a[2]=20
print("Modify List = ",a)
print("Inner List = ",a[4])
a[4].insert(0,'O')
print("Modify Inner List = ",a)
a.pop(3)
print("Remove an element by index in list = ",a)
a.clear()
print("Remove all object",a)
