def range_summation(lower, upper):
	evens = sum(i for i in range(lower, upper + 1) if i % 2 == 0)
	odds = sum(i for i in range(lower, upper + 1) if i % 2 != 0)
	return evens, odds
lower=int(input("Enter the lower bound:-"))
upper=int(input("Enter the upper bound:-"))
e,o=range_summation(lower, upper)
print("Summation of all even numbers:-",e)
print("Summation of all odd numbers:-",o)

