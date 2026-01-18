class device:
	def __init__(self,name,dev_type,price):
		self.name=name
		self.dev_type=dev_type
		self.price=price
r=device("name:HP","dev_type:Laptop","price:24000")
x=device("name:Iphone","dev_type:Phone","price:80000")
print(r.name)
print(x.name,x.dev_type)
