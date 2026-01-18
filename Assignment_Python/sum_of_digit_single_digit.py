num = int(input("Enter a number: "))

while num > 9:
    s = 0
    temp = num
    while temp > 0:
        s += temp % 10
        temp //= 10
    num = s

print("Single digit sum =", num)

