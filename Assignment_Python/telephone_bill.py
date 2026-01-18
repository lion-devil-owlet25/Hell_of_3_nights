calls = int(input("Enter number of calls: "))
if calls <= 100:
    bill = 100
elif calls <= 500:
    bill = 100 + ((calls - 100) // 50) * 5
else:
    bill = 100 + ((500 - 100) // 50) * 5 + (calls - 500) * 1.25

print("Telephone bill =", bill, "rupees")
