class device:
	def __init__(self,name,dev_type,price):
		self.name=name
		self.dev_type=dev_type
		self.price=price
		print(self.name,self.dev_type,self.price)
r=device("name:HP","dev_type:Laptop","price:24000")
