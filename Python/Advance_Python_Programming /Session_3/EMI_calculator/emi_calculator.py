
# Task 1: EMI Calculator

def calculate_emi(principal, annual_rate, months):

    r = annual_rate / 12 / 100

    emi = (principal * r * (1 + r) ** months) / ((1 + r) ** months - 1)

    total_payable = emi * months

    total_interest = total_payable - principal

    return emi, total_payable, total_interest


# Taking input

principal = float(input("Enter loan amount: "))

annual_rate = float(input("Enter annual interest rate: "))

months = int(input("Enter loan duration in months: "))


# Function call

emi, total_payable, total_interest = calculate_emi(
    principal, annual_rate, months
)


# Display output

print("\n----- EMI DETAILS -----")

print(f"Monthly EMI: Rs. {emi:.2f}")

print(f"Total Payable: Rs. {total_payable:.2f}")

print(f"Total Interest: Rs. {total_interest:.2f}")
