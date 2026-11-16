
# Function 1: Add Payment

def add_payment():

    flat = input("Enter flat number: ")
    owner = input("Enter owner name: ")
    month = input("Enter month: ")
    amount = input("Enter maintenance amount: ")

    f = open(r"C:\Users\rabar\OneDrive\Desktop\18-june-2026\Assignments\Python\Advance Python Programing\Session_1\Society\payments.txt", "a")

    f.write(flat + "|" + owner + "|" + month + "|" + amount + "\n")

    f.close()

    print("Payment added successfully!")


# Function 2: View All Payments

def view_all():

    f = open(r"C:\Users\rabar\OneDrive\Desktop\18-june-2026\Assignments\Python\Advance Python Programing\Session_1\Society\payments.txt", "r")

    text = f.read()

    f.close()

    total = 0

    print("\n")
    print("-" * 65)
    print(f"{'Flat':<12}{'Owner':<18}{'Month':<12}{'Amount (₹)':>12}")
    print("-" * 65)

    lines = text.split("\n")

    for line in lines:

        if line == "":
            continue

        data = line.split("|")

        flat = data[0]
        owner = data[1]
        month = data[2]
        amount = int(data[3])

        total += amount

        print(f"{flat:<12}{owner:<18}{month:<12}{amount:>12}")

    print("-" * 65)
    print("Total Collected: ₹", total)


# Function 3: Write Summary

def write_summary():

    f = open("C:\Users\rabar\OneDrive\Desktop\18-june-2026\Assignments\Python\Advance Python Programing\Session_1\Society\payments.txt", "r")

    text = f.read()

    f.close()

    monthly_total = {}

    lines = text.split("\n")

    for line in lines:

        if line == "":
            continue

        data = line.split("|")

        month = data[2]
        amount = int(data[3])

        if month in monthly_total:
            monthly_total[month] += amount
        else:
            monthly_total[month] = amount

    # Write summary file

    f = open("summary.txt", "w")

    for month, total in monthly_total.items():

        f.write(f"{month}: Rs.{total}\n")

    f.close()

    print("Summary created successfully!")


# Main Menu

menu = """
========= SOCIETY REGISTER =========

1. Add Payment
2. View All
3. Write Summary
4. Exit

====================================
"""

status = True

while status:

    print(menu)

    choice = input("Enter your choice: ")

    if choice == "1":

        add_payment()

    elif choice == "2":

        view_all()

    elif choice == "3":

        write_summary()

    elif choice == "4":

        print("Thank you! Exiting Society Register.")
        status = False

    else:

        print("Invalid choice! Please try again.")
