
# stock.py

# Custom Exception
class OutOfStockError(Exception):
    pass


# Hardware Stock Dictionary
hardware_stock = {

    "Cement": {
        "quantity": 20,
        "price": 450
    },

    "Paint": {
        "quantity": 10,
        "price": 800
    },

    "Hammer": {
        "quantity": 15,
        "price": 250
    },

    "Drill": {
        "quantity": 5,
        "price": 1500
    },

    "Screws": {
        "quantity": 30,
        "price": 100
    },

    "Nails": {
        "quantity": 25,
        "price": 120
    },

    "Tiles": {
        "quantity": 12,
        "price": 600
    },

    "Pipe": {
        "quantity": 8,
        "price": 350
    }
}


# Check Stock Function
def check_stock(item):

    if item not in hardware_stock:
        raise OutOfStockError("Item not found!")

    return hardware_stock[item]


# Reduce Stock Function
def reduce_stock(item, qty):

    if item not in hardware_stock:
        raise OutOfStockError("Item not found in stock!")

    if qty <= 0:
        raise OutOfStockError("Quantity must be greater than zero!")

    available = hardware_stock[item]["quantity"]

    if qty > available:
        raise OutOfStockError(
            f"Only {available} boxes available for {item}!"
        )

    hardware_stock[item]["quantity"] -= qty

    return hardware_stock[item]["quantity"]
