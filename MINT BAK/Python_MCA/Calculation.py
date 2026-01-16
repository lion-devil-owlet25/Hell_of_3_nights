a=int(input("Enter the first number:-"))
b=int(input("Enter the second number:-"))
print("\t Menu\t")
print("Press 1 to Add")
print("Press 2 to Subtract")
print("Press 3 to Multiply")
print("Press 4 to Divide")
print("Press 5 to Find remainder")
c=int(input("Enter your choice:-"))
def Add(a,b):
    return a+b
def Subtract(a,b):
    return a-b
def Multiply(a,b):
    return a*b
def Divide(a,b):
    return a/b
def Modulus(a,b):
    return a%b
match(c):
    case 1:
        print(a,"+",b,"=",Add(a,b))
    case 2:
        print(a,"-",b,"=",Subtract(a,b))
    case 3:
        print(a,"*",b,"=",Multiply(a,b))
    case 4:
        print(a,"/",b,"=",Divide(a,b))
    case 5:
        print(a,"%",b,"=",Modulus(a,b))
    case _:
        print("Invaild choice")
        
        
