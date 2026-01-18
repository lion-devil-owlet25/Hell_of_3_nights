def fav_sports(name, *sports):
	return name, list(sports)
name=input("Enter your name:-")
sports=input("Enter your favourite sports:-").split()
print(fav_sports(name,*sports))

