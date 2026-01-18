class Allrounder:
	def __init__(self,name,runs,wickets):
		self.name = name
		self.runs = runs
		self.wickets = wickets
	def display(self):
		print(f"Name: {self.name} | Runs: {self.runs} | Wickets: {self.wickets}")
a1 = Allrounder("Hardik", 1200, 85)
a2 = Allrounder("Jadeja", 1500, 120)
print("Allrounder Records:")
a1.display()
a2.display()
if a1.runs > a2.runs:
    print("Highest Run Scorer:",a1.name)
else:
    print("Highest Run Scorer:",a2.name)
