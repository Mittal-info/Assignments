


# pricing.py

import math


# Calculate GST
def gst_amount(amount, rate=18):
    return amount * rate / 100


# Calculate required boxes
def boxes_needed(quantity, box_size):
    return math.ceil(quantity / box_size)


# Round amount down to multiple of 5
def round_down_to_five(amount):
    return math.floor(amount / 5) * 5
