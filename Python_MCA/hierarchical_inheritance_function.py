class device:
	def c(self,name,price):
		print(name,price,end="")
class Phone(device):
	def a(self,model):
		print(model)
class laptop(device):
	def d(self,model):
		print(model)
r=laptop()
b=Phone()
r.c("Name:Vivo || ","Price:58223|| ")
b.a("Model_Phone:VS22 || ")
r.c("Name:HP || ","Price:582230 || ")
r.d("Model:Pallivion")
