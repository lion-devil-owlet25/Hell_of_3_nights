lst = [10, 20, 10, 30, 10, 40]
value = 10
indices = [i for i in range(len(lst)) if lst[i] == value]
print("Indices:", indices)
print("Count:", len(indices))
