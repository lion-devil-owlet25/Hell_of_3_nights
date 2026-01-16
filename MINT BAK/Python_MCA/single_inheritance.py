class device:
	def __init__(self,name,dev_type,price):
		self.name=name
		self.dev_type=dev_type
		self.price=price
class laptop(device):
	def __init__(self,name,dev_type,price,model):
		super().__init__(name,dev_type,price)
		self.model=model
		print(self.name,self.dev_type,self.price,self.model)
r=laptop("Name:Dell || ","Dev_type:Laptop || ","Price:50000 ||","Model:Pavillion")
