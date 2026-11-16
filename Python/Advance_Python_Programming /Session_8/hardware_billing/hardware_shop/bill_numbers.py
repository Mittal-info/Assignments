
# bill_numbers.py

import random

# Store generated numbers
generated_numbers = []


def new_bill_number():

    while True:

        number = random.randint(1000, 9999)

        if number not in generated_numbers:

            generated_numbers.append(number)

            return f"HW-{number}"
