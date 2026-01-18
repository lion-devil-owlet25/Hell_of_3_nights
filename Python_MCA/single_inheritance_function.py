class device:
	def c(self,name,dev_type,price):
		print(name,dev_type,price)
class laptop(device):
	def d(self,model):
		print(model)
r=laptop()
r.c("HP","LAPTOP",582230)
r.d("Pallivion")
