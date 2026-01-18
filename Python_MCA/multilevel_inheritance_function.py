class device:
	def c(self,name,price):
		print(name,price,end="")
class laptop(device):
	def d(self,model):
		print(model)
class HP(laptop):
	def a(self,dev_type):
		print(dev_type,end="")
r=HP()
r.c("Name:Dell|| ","Price:582230 || ")
r.a("Device:LAPTOP || ")
r.d("Model:Pallivion")
