"""
Program Structure – fest_passes.py
File name: fest_passes.py
1. Base class – FestPass
2. Child classes – StudentPass, AlumniPass, VIPPass
3. Method overriding – price() and perks()
4. Receipt function – print_receipt()
5. Group pricing – group_price()
6. Registration menu using dictionary mapping
7. Calculate per-type total and grand total

"""


# fest_passes.py

# =================================
# 1. BASE CLASS
# =================================

class FestPass:

    def __init__(self, holder_name):
        self.holder_name = holder_name

    def price(self):
        return 500

    def perks(self):
        return "Basic festival entry"

    # Group Price Method
    def group_price(self, count=1, discount_percent=0):
        total = self.price() * count
        discount = total * discount_percent / 100
        return total - discount


# =================================
# 2. CHILD CLASSES
# =================================

class StudentPass(FestPass):

    def price(self):
        return 300

    def perks(self):
        return "Student entry with food coupon"


class AlumniPass(FestPass):

    def price(self):
        return 800

    def perks(self):
        return "Alumni entry with special seating"


class VIPPass(FestPass):

    def price(self):
        return 2000

    def perks(self):
        return "VIP entry with backstage access"


# =================================
# 3. RECEIPT FUNCTION
# =================================

def print_receipt(pass_obj):

    print("\n-----------------------------")
    print("       FEST PASS RECEIPT")
    print("-----------------------------")

    print("Holder Name :", pass_obj.holder_name)
    print("Price       : ₹", pass_obj.price())
    print("Perks       :", pass_obj.perks())

    print("-----------------------------")


# =================================
# 4. TESTING POLYMORPHISM
# =================================

print("\n===== PASS DETAILS =====")

passes = [
    StudentPass("Rahul"),
    StudentPass("Priya"),
    StudentPass("Amit"),
    AlumniPass("Neha"),
    AlumniPass("Karan"),
    VIPPass("Mittal"),
    FestPass("Riya"),
    FestPass("Jay")
]

total = 0

for p in passes:
    print_receipt(p)
    total += p.price()

print("\nTotal Collection: ₹", total)


# =================================
# 5. TEST GROUP PRICE
# =================================

print("\n===== GROUP PRICE TEST =====")

student = StudentPass("Student Group")

print("Student Normal :", student.group_price())
print("Student 4 Pass :", student.group_price(4))
print("Student 4 Pass with 10% discount:",
      student.group_price(4, 10))

alumni = AlumniPass("Alumni Group")

print("Alumni 2 Pass with 25% discount:",
      alumni.group_price(2, 25))


# =================================
# 6. REGISTRATION MENU
# =================================

def registration_menu():

    print("\n===== FEST REGISTRATION =====")

    # Dictionary Mapping
    pass_types = {
        "G": FestPass,
        "S": StudentPass,
        "A": AlumniPass,
        "V": VIPPass
    }

    registrations = []

    type_totals = {
        "G": 0,
        "S": 0,
        "A": 0,
        "V": 0
    }

    grand_total = 0

    while True:

        holder_name = input("\nEnter holder name: ")

        print("\nG - General Pass (₹500)")
        print("S - Student Pass (₹300)")
        print("A - Alumni Pass (₹800)")
        print("V - VIP Pass (₹2000)")

        choice = input("Enter pass type: ").upper()

        if choice not in pass_types:
            print("Invalid pass type!")
            continue

        count = int(input("Enter pass count: "))

        discount_percent = float(
            input("Enter discount percentage: ")
        )

        # Create Object using Dictionary
        pass_obj = pass_types[choice](holder_name)

        # Store registration
        registrations.append(
            (pass_obj, count, discount_percent, choice)
        )

        # Calculate Group Price
        amount = pass_obj.group_price(
            count, discount_percent
        )

        type_totals[choice] += amount
        grand_total += amount

        print("\nRegistration Successful!")
        print("Holder :", holder_name)
        print("Pass   :", pass_obj.perks())
        print("Count  :", count)
        print("Amount : ₹", amount)

        again = input(
            "\nDo you want another registration? (yes/no): "
        ).lower()

        if again != "yes":
            break

    # =================================
    # 7. FINAL SUMMARY
    # =================================

    print("\n========== FINAL SUMMARY ==========")

    print("\nPer Type Collection:")

    print("General Pass : ₹", type_totals["G"])
    print("Student Pass : ₹", type_totals["S"])
    print("Alumni Pass  : ₹", type_totals["A"])
    print("VIP Pass     : ₹", type_totals["V"])

    print("\nGrand Total: ₹", grand_total)

    print("\nTotal Registrations:", len(registrations))


# =================================
# MAIN PROGRAM
# =================================

if __name__ == "__main__":
    registration_menu()
