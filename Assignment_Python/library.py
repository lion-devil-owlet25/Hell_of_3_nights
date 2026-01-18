days = int(input("Enter number of days late: "))
if days <= 0:
    fine = 0
elif days <= 5:
    fine = days * 0.50
elif days <= 10:
    fine = 5 * 0.50 + (days - 5) * 1
elif days <= 30:
    fine = 5 * 0.50 + 5 * 1 + (days - 10) * 5
else:
    fine = None

if fine is None:
    print("Membership will be cancelled")
else:
    print("Fine =", fine, "rupees")
