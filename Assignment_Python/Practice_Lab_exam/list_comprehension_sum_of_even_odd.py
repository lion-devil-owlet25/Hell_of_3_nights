res=[(e**2 + o**2) 
for e in range(1,6) if e%2 == 0 
for o in range(6,11) if o%2 != 0]
print(res)
