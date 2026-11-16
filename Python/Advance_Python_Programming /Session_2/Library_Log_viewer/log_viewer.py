
# Library Log Viewer

# Step 1: Open the file
file = open(r"C:\Users\rabar\OneDrive\Desktop\18-june-2026\Assignments\Python\Advance Python Programing\Session_2\Library_Log_viewer\issue_log.txt", "r")

# Step 2: Create line index
line_index = []
line_number = 1

while True:

    position = file.tell()

    line = file.readline()

    if line == "":
        break

    line_index.append((line_number, position))

    line_number += 1


# Step 3: Create Menu
menu = """
========== LIBRARY LOG VIEWER ==========

A. Show All Records
J. Jump to a Line
R. Show Last 3 Entries
Q. Quit

========================================
"""

# Step 4: Menu Loop
while True:

    print(menu)

    choice = input("Enter your choice: ").upper()

    # A: Show All Records
    if choice == "A":

        file.seek(0)

        while True:

            line = file.readline()

            if line == "":
                break

            print(line.strip())


    # J: Jump to a particular line
    elif choice == "J":

        number = int(input("Enter line number: "))

        found = False

        for line_no, position in line_index:

            if line_no == number:

                file.seek(position)

                line = file.readline()

                print("Selected Line:", line.strip())

                found = True
                break

        if not found:
            print("No such line")


    # R: Show Last 3 Entries
    elif choice == "R":

        if len(line_index) == 0:

            print("No records found")

        else:

            last_three = line_index[-3:]

            file.seek(last_three[0][1])

            print("\nLast 3 Entries:")

            while True:

                line = file.readline()

                if line == "":
                    break

                print(line.strip())


    # Q: Quit
    elif choice == "Q":

        print("Thank you for using Library Log Viewer!")

        break

    else:

        print("Invalid choice! Please try again.")


# Step 5: Close file
file.close()
