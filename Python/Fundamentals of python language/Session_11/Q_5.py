def update_cart(cart, item, qty):
    if item in cart:
        cart[item] += qty
    else:
        cart[item] = qty

    return cart


cart = {
    "Shoes": 1,
    "T-Shirt": 2
}

updated_cart = update_cart(cart, "Shoes", 2)
print(updated_cart)

updated_cart = update_cart(cart, "Watch", 1)
print(updated_cart)