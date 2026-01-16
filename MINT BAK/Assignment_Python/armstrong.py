n = int(input("Enter a number: "))
s = 0
t = n
digits = len(str(n))

while t > 0:
    d = t % 10
    s += d ** digits
    t //= 10

if s == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")

