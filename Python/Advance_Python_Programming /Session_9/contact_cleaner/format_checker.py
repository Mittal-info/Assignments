
import re


# 1. Check valid PIN code
def is_valid_pin(text):
    pattern = r'^[1-9][0-9]{5}$'

    if re.match(pattern, text):
        return True
    else:
        return False


print("PIN CODE CHECKING")

pins = ["380015", "110001", "056001",
        "38001", "3800155", "38O015"]

for pin in pins:
    print(pin, ":", is_valid_pin(pin))


# 2. Find mobile number
def find_mobile(text):
    pattern = r'(?<![0-9])(?:\+91)?[6-9][0-9]{9}(?![0-9])'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


print("\nMOBILE NUMBER CHECKING")

print(find_mobile("Call 9000012345 after 6 pm"))
print(find_mobile("Reach me on +919000012345"))
print(find_mobile("Flat 5000012345"))
print(find_mobile("Ring 900001234"))


# 3. Count PIN codes from addresses.txt
def count_pins():

    pin_count = {}

    with open("addresses.txt", "r") as file:

        for line in file:

            pins = re.findall(r'\b[1-9][0-9]{5}\b', line)

            for pin in pins:

                if pin in pin_count:
                    pin_count[pin] += 1
                else:
                    pin_count[pin] = 1

    print("\nPIN CODE COUNT")

    for pin, count in pin_count.items():
        print(pin, ":", count)


count_pins()
