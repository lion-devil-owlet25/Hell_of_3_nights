sd={'ID':1,'NAME':'Aakesh','ROLL':21,'MARKS':70}
print("Student_Details:-",sd)
k=sd.keys()
print("Keys:-",k)
v=sd.values()
print("Values:-",v)
d=sd.get('ID','L')
if d==1:
	print(d)
p=sd.items()
print(p)
l=sd.pop('MARKS')
print(l)
print(sd)
sd1={'ID':1,'NAME':'Aakesh','ROLL':21,'MARKS':80}
sd1.clear()
print(sd1)
d={'ID':1,'NAME':'Aakesh','ROLL':22,'MARKS':80}
del d['ID']
print(d)
sd1.update(d)
print(sd)

