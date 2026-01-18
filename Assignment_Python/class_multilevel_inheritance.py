class GrandParent:
	def feature(self):
		return "GrandParent feature: wisdom"
class Parent(GrandParent):
	def feature_parent(self):
		return "Parent feature: responsibility"
class Child(Parent):
	def feature_child(self):
		return "Child feature: curiosity"
# Test multilevel inheritance
if __name__ == "__main__":
	c = Child()
	print(c.feature_child())
	print(c.feature_parent())
	print(c.feature())
	
