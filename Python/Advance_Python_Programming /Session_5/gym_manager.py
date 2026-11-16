"""

gym_manager.py
│
├── class Member
│   ├── __init__()
│   ├── total_fee()
│   └── renew()
│
├── Dictionary (Plan Fees)
│
├── Empty List (members)
│
└── Menu Loop
    ├── 1. Add Member
    ├── 2. Show All Members
    ├── 3. Exit
    └── 4. Renew Membership

"""
class Member:

    plan_fees = {
        "Basic": 800,
        "Standard": 1200,
        "Premium": 1800
    }

    def __init__(self, name, plan, months):
        self.name = name
        self.plan = plan
        self.months = months
        self.fee = Member.plan_fees[plan]

    def total_fee(self):
        return self.fee * self.months

    def renew(self, extra_months):
        self.months += extra_months


# Creating member list
members = []


# Menu
while True:

    print("\n===== GYM MANAGEMENT SYSTEM =====")
    print("1. Add Member")
    print("2. Show All Members")
    print("3. Exit")
    print("4. Renew Membership")

    choice = input("Enter your choice: ")

    # Add Member
    if choice == "1":

        name = input("Enter member name: ")

        plan = input("Enter plan (Basic/Standard/Premium): ")

        if plan not in Member.plan_fees:
            print("Invalid Plan!")
            continue

        months = int(input("Enter months (1 to 12): "))

        if months < 1 or months > 12:
            print("Invalid Months! Enter between 1 and 12.")
            continue

        member = Member(name, plan, months)

        members.append(member)

        print("Member Added Successfully!")


    # Show All Members
    elif choice == "2":

        if len(members) == 0:
            print("No Members Found!")

        else:

            total_revenue = 0

            print("\n===== ALL MEMBERS =====")

            for member in members:

                print("Name:", member.name)
                print("Plan:", member.plan)
                print("Monthly Fee: ₹", member.fee)
                print("Months:", member.months)
                print("Total Fee: ₹", member.total_fee())
                print("----------------------")

                total_revenue += member.total_fee()

            print("Total Revenue: ₹", total_revenue)


    # Exit
    elif choice == "3":

        print("Thank You!")
        break


    # Renew Membership
    elif choice == "4":

        name = input("Enter member name to renew: ")

        found = False

        for member in members:

            if member.name.lower() == name.lower():

                extra_months = int(input("Enter extra months: "))

                if extra_months <= 0:
                    print("Invalid Months!")
                    break

                member.renew(extra_months)

                print("Membership Renewed Successfully!")
                print("New Total Fee: ₹", member.total_fee())

                found = True
                break

        if not found and extra_months if False else False:
            pass

        if not found:
            print("Member not found")


    else:
        print("Invalid Choice!")

