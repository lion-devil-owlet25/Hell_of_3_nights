import numpy as n
import random
f=n.array([[52,45,520],[45,10,50],[69,62,5]])
r=n.array([[2,5,20],[57,10,5],[9,6,50]])
p=n.linalg.inv(f)
l=n.linalg.matrix_rank(f)
print("Rank=",l)
print(f)
print("Inverse Matrix \n",p)
m=f.T
print("Transpose:-\n",m)
b=n.linalg.det(f)
print("Determinant:-\n",b)
j=n.matmul(f,r)
print("Multiplication:-\n",j)
k=n.dot(f,r)
print("Dot Product:-\n",k)
#to create a 3×2 matrix whose every element is  filled with the number 2.
a=n.full((3,2),2)
print(a)
ad=n.random.randint(5,10,size=(3,3))
print(ad)


