def ADD(a,b=3):
	return a+b
print("Positional Argument:-",ADD(1,2))
print("Default Argument:-",ADD(10))
print("Keyword Argument:-",ADD(a=10,b=12))
def ADD_list(args):
	sum=0
	for i in range(0,len(args)):
		sum+=args[i]
	return sum
print("Arbitary/Variable Length Argument:",ADD_list([1,5,8,9,6,10]))
