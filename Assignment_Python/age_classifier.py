def classify_age(age):
	if age <= 12:
		return "Child"
	elif 13 <= age <= 19:
		return "Teenager"
	elif 20 <= age <= 35:
		return "Young"
	elif 36 <= age <= 60:
		return "Middle Aged"
	else:
		return "Senior Citizen"
age=int(input("Enter the age of a student:-"))
print("Age Classifier:-",classify_age(age))
