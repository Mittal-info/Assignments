import math

prices = [199.1, 349.8, 599.3]

rounded_prices = []

for price in prices:
    rounded_prices.append(math.ceil(price))

print("Original prices:", prices)
print("Rounded prices:", rounded_prices)