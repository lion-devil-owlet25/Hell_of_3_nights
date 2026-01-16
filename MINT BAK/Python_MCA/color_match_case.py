color=str(input("Enter name of the color:-"))
a=int(input("Enter your choice:-"))
match(a):
    case 1:
        if color == "red":
            print("Stop")
    case 2:
        if color == "yellow":
            print("Caution")
    case _:
        print("Go")
