orders = {
    101: {
        "restaurant": "Pizza House",
        "items": ["Pizza", "Garlic Bread"],
        "total": 500
    }
}


def add_order(orders, order_id, restaurant, items, total):
    orders[order_id] = {
        "restaurant": restaurant,
        "items": items,
        "total": total
    }
    return orders


def update_total(orders, order_id, new_total):
    if order_id in orders:
        orders[order_id]["total"] = new_total
    else:
        print("Order not found!")

    return orders


add_order(orders, 102, "Burger Point", ["Burger", "Fries"], 350)

update_total(orders, 101, 600)

print(orders)