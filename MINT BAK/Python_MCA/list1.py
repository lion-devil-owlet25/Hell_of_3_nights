mylist=[1,2,3,4,5,"Hello",'c']
print(len(mylist))
print(*mylist)
list2=[1,5,4,7,8,6,"hi",'f',2.6]
mylist.append(list2)
print(mylist)
print(mylist[7])
mylist.extend(list2)
print(mylist)
print(mylist[8])
mylist.pop()
print(mylist)
print(list2.index('hi'))
list2.remove('hi')
print(list2)

