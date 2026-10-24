import math

bill = float(input("Enter your order bill amount: "))

discount = bill * 10 / 100
final_bill = bill - discount

rounded_bill = math.floor(final_bill)

print("Original bill:", bill)
print("10% discount:", discount)
print("Final bill after discount:", rounded_bill)