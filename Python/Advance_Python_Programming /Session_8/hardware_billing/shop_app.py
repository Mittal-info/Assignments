
# shop_app.py

# Import Style 1
import hardware_shop.pricing as pricing

# Import Style 2
from hardware_shop.stock import reduce_stock, OutOfStockError
from hardware_shop.stock import check_stock

# Import Style 3
from hardware_shop import new_bill_number


# Three Customers
customers = [
    {
        "name": "Rahul",
        "item": "Cement",
        "boxes": 3
    },

    {
        "name": "Priya",
        "item": "Paint",
        "boxes": 2
    },

    {
        "name": "Amit",
        "item": "Drill",
        "boxes": 10
    }
]


# Billing Process
for customer in customers:

    print("\n================================")
    print("       HARDWARE SHOP BILL")
    print("================================")

    bill_number = new_bill_number()

    name = customer["name"]
    item = customer["item"]
    boxes = customer["boxes"]

    print("Bill Number :", bill_number)
    print("Customer    :", name)
    print("Item        :", item)
    print("Boxes       :", boxes)

    try:

        # Get Item Details
        item_details = check_stock(item)

        price = item_details["price"]

        # Calculate Amount
        amount = price * boxes

        # Calculate GST
        gst = pricing.gst_amount(amount)

        # Calculate Final Total
        total = amount + gst

        # Round Down to Multiple of 5
        final_total = pricing.round_down_to_five(total)

        # Reduce Stock
        remaining = reduce_stock(item, boxes)

        # Print Bill
        print("Price       : ₹", amount)
        print("GST (18%)   : ₹", gst)
        print("Total       : ₹", final_total)

        print("Status      : BILL SUCCESSFUL")
        print("Remaining Stock:", remaining, "boxes")

    except OutOfStockError as e:

        print("GST         : Not charged")
        print("Total       : Not billed")
        print("Status      : BILL FAILED")
        print("Message     :", e)

    print("================================")
