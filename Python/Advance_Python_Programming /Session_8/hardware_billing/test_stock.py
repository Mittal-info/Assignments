


# test_stock.py

import hardware_shop.stock as stock

try:

    # Check Stock
    print("Available Stock:")

    print(stock.check_stock("Cement"))

    # Reduce Stock
    stock.reduce_stock("Cement", 5)

    print("\nAfter Reducing Stock:")

    print(stock.check_stock("Cement"))

    # Failing Request
    stock.reduce_stock("Drill", 10)

except stock.OutOfStockError as e:

    print("\nStock Error:", e)
