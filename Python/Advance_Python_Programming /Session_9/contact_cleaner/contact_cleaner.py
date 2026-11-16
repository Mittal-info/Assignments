
from format_checker import is_valid_pin, find_mobile


def clean_contacts():

    with open("contacts.txt", "r") as file:
        contacts = file.readlines()

    with open("valid_contacts.txt", "w") as valid_file, \
         open("rejected_contacts.txt", "w") as rejected_file:

        for line in contacts:

            line = line.strip()

            if not line:
                continue

            parts = line.split(",")

            if len(parts) != 3:
                rejected_file.write(line + " - Invalid format\n")
                continue

            name, mobile, pin = parts

            reasons = []

            # Check mobile number
            if find_mobile(mobile) != mobile:
                reasons.append("Invalid mobile number")

            # Check PIN code
            if not is_valid_pin(pin):
                reasons.append("Invalid PIN code")

            # Store valid and rejected contacts
            if len(reasons) == 0:

                valid_file.write(line + "\n")

            else:

                reason = ", ".join(reasons)

                rejected_file.write(
                    line + " - " + reason + "\n"
                )

    print("Contact cleaning completed!")
    print("Check valid_contacts.txt")
    print("Check rejected_contacts.txt")


clean_contacts()
