#Shallow Copy
original=[1,2,3,4,5,['P','M','Y','J','K',56,63,45],6,7,8]
clone=original[:]
clone.pop(7)
print("Original List = ",original)
print("Cloning List = ",clone)
#Deep Copy
matrix=[[1,2],[3,4]]
import copy
clone1=copy.deepcopy(matrix)
clone2=matrix.copy()
print("Cloning Matrix = ",clone1)
print("Cloning Matrix_2= ",clone2)


