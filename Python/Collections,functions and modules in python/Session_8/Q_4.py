def apply_coupon(amount, coupon_code=None):
    if coupon_code == "SAVE10":
        discount = amount * 10 / 100
        return amount - discount
    else:
        return amount


print(apply_coupon(1000))
print(apply_coupon(1000, "SAVE10"))