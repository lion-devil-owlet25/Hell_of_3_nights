class device:
	def c(self,name,price):
		print(name,price,end="")
class digital:
	def a(self,dev_type):
		print(dev_type,end="")
class laptop(device,digital):
	def d(self,model):
		print(model)
r=laptop()
r.c("Name:HP || ","Price:582230 || ")
r.a("Device:LAPTOP || ")
r.d("Model:Pallivion")
